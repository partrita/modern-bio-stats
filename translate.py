
import sys
import time
import bs4
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def translate_text_chunk(text, translator):
    try:
        return translator.translate(text)
    except Exception as e:
        print(f"Could not translate text: {text}", file=sys.stderr)
        print(e, file=sys.stderr)
        return text

def translate_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    translator = GoogleTranslator(source='auto', target='ko')

    for element in soup.find_all(string=True):
        if element.parent.name in ['script', 'style', '[document]', 'head', 'title']:
            continue

        if isinstance(element, bs4.element.Comment):
            continue

        if not element.strip():
            continue

        text = str(element)
        if len(text) > 1000:
            translated_text = ""
            for i in range(0, len(text), 1000):
                chunk = text[i:i+1000]
                translated_chunk = translate_text_chunk(chunk, translator)
                translated_text += translated_chunk if translated_chunk else ""
                time.sleep(0.1)
        else:
            translated_text = translate_text_chunk(text, translator)
            time.sleep(0.1)
        
        if translated_text:
            element.replace_with(translated_text)


    new_file_path = file_path.replace('.html', '.ko.html')
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Translated {file_path} to {new_file_path}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python translate.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    translate_html_file(file_path)
