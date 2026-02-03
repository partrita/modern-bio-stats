# Modern Statistics for Modern Biology (한국어 번역 프로젝트)

이 리포지토리는 **"Modern Statistics for Modern Biology"** (Susan Holmes & Wolfgang Huber 저) 의 한국어 번역 프로젝트입니다.

## 원본 책 정보
- **제목**: Modern Statistics for Modern Biology
- **저자**: Susan Holmes, Wolfgang Huber
- **출판사**: Cambridge University Press (2019)
- **라이센스**: [CC BY-NC-SA 2.0](https://creativecommons.org/licenses/by-nc-sa/2.0/)
- **웹사이트**: [https://www.huber.embl.de/msmb/](https://www.huber.embl.de/msmb/)

## 프로젝트 구조

```
├── book/               # Quarto book 소스 파일 (.qmd, .css, 이미지 등)
│   ├── index.qmd       # 메인 페이지 및 소개
│   ├── 00-chap.qmd     # 각 챕터 소스
│   ├── ...
│   └── _quarto.yml     # Quarto 설정 파일
├── .github/
│   └── workflows/      # GitHub Actions 워크플로우
│       └── deploy.yml  # GitHub Pages 배포 설정
└── README.md           # 프로젝트 소개 (이 파일)
```

## 빌드 및 실행 방법

이 프로젝트는 [Quarto](https://quarto.org/)를 사용하여 만들어졌습니다.

### 로컬에서 실행하기

1. **Quarto 설치**: [Quarto 다운로드 페이지](https://quarto.org/docs/get-started/)에서 Quarto CLI를 설치하세요.
2. **패키지 설치**: 책의 예제 코드를 실행하려면 R 패키지 설치가 필요할 수 있습니다. `book/index.qmd`의 안내를 참고하세요.
3. **미리보기**: 터미널에서 `book` 디렉터리로 이동하지 않고, 프로젝트 루트에서 다음 명령어를 실행하여 책을 미리볼 수 있습니다. (설정에 따라 `cd book` 후 실행해야 할 수도 있습니다)

```bash
quarto preview book
```

### 배포

GitHub Actions를 통해 `gh-pages` 브랜치로 자동 배포됩니다. `main` 브랜치에 푸시하면 `.github/workflows/deploy.yml` 워크플로우가 실행되어 `book` 디렉터리의 내용을 빌드하고 배포합니다.

## 기여하기

번역 오류 제보나 기여는 Issue 또는 Pull Request를 통해 환영합니다.
