import sys
import html2text
from bs4 import BeautifulSoup

def convert_html_to_qmd(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    main_content = soup.find('main')

    if main_content:
        # Remove the header within the main content as it's redundant
        header = main_content.find('header')
        if header:
            header.decompose()
            
        html_for_markdown = str(main_content)
    else:
        html_for_markdown = html_content

    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown_content = h.handle(html_for_markdown)

    new_file_path = file_path.replace('.html', '.qmd')
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"Converted {file_path} to {new_file_path}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python html_to_qmd.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    convert_html_to_qmd(file_path)