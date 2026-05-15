# 테스트 자동화 포트폴리오

QA 자동화 직무 지원을 위해 테스트 자동화 연습용 웹사이트인 [Automation Exercise](https://automationexercise.com/)를 대상으로 Playwright와 pytest-bdd 기반의 E2E 테스트 자동화 구조를 구현한 포트폴리오 프로젝트입니다.


## 프로젝트 개요

QA 자동화 직무에서 요구되는 테스트 설계, 자동화 구현, 실패 분석 흐름을 고려해 구성한 E2E 테스트 자동화 프로젝트입니다.

테스트 대상은 테스트 자동화 연습용 웹사이트 Automation Exercise이며, 사용자의 주요 서비스 이용 흐름을 Playwright 기반의 브라우저 자동화로 검증합니다. 테스트 시나리오는 pytest-bdd를 사용해 Gherkin 문법으로 작성하여 테스트 의도를 명확히 표현하고, Page Object Model(POM) 패턴을 적용해 코드의 재사용성과 확장성을 높였습니다.

또한 API 응답 데이터와 UI 표시 데이터 간의 일관성을 검증하고, 테스트 실패 시 분석에 필요한 artifacts를 저장하도록 구성했습니다.


## 기술 스택

| 구분 | 기술 | 사용 목적 |
| --- | --- | --- |
| Language | Python | 테스트 코드 작성 |
| Test Framework | pytest | 테스트 실행 및 fixture 관리 |
| BDD Framework | pytest-bdd | Gherkin 기반 테스트 시나리오 작성 |
| Browser Automation | Playwright | 브라우저 기반 E2E 테스트 자동화 |
| API Client | requests | API 요청/응답 데이터 조회 및 UI 표시 데이터와의 일관성 검증 |
| Design Pattern | Page Object Model | 페이지별 동작과 검증 로직 분리 |

pytest의 fixture와 pytest-bdd의 시나리오 매핑 기능을 활용해 테스트 실행 흐름을 구성했으며, Playwright를 통해 실제 브라우저 환경에서 사용자 동작을 검증하고,
Python requests로 API 응답 데이터를 조회해 UI 데이터와 비교했습니다.


## 주요 구현 포인트

### Page Object Model 기반 구조화

페이지별 동작과 요소 접근 로직을 Page Object로 분리하여 테스트 시나리오 코드가 검증 흐름에 집중할 수 있도록 구성했습니다. 이를 통해 동일한 페이지 동작을 여러 테스트에서 재사용할 수 있고, UI 변경이 발생했을 때 수정 범위를 줄일 수 있도록 했습니다.

### Gherkin 기반 BDD 테스트

pytest-bdd를 사용해 테스트 시나리오를 Given-When-Then 형식의 Gherkin 문법으로 작성했습니다. 테스트의 사전 조건, 사용자 행동, 기대 결과를 명확히 구분하여 테스트 의도를 쉽게 파악할 수 있도록 했습니다.

### API/UI 데이터 일관성 검증

Python requests를 사용해 상품 검색 API의 응답 데이터를 조회하고, 동일한 검색 조건으로 UI에 표시되는 상품 데이터와 비교했습니다. 이를 통해 API 응답과 실제 화면 표시 데이터가 일관되게 제공되는지 검증했습니다.

### 실패 분석을 위한 artifacts 저장

테스트 실패 시 스크린샷과 Playwright trace를 artifacts 디렉터리에 저장하도록 구성했습니다. 실패 시점의 화면 상태와 실행 흐름을 확인할 수 있도록 하여 테스트 실패 원인을 더 빠르게 추적할 수 있도록 했습니다.

## 프로젝트 구조

```text
test_automation/
├── common/
│   ├── action_base.py
│   ├── base.py
│   └── expect_base.py
├── components/
│   ├── cart_modal.py
│   └── product_card.py
├── pages/
│   ├── home_page.py
│   ├── login_page.py
│   ├── products_page.py
│   └── view_cart_page.py
├── tests/
│   ├── api/
│   │   └── clients/
│   │       └── product_api_client.py
│   ├── integration/
│   │   └── test_product_search_consistency.py
│   └── ui/
│       ├── features/
│       ├── steps/
│       └── test_*.py
├── conftest.py
├── requirements.txt
└── README.md
```

이 프로젝트는 POM 패턴을 기반으로 UI 조작 로직과 테스트 시나리오를 분리했습니다.  
`pages` 디렉터리에는 화면 단위의 Page Object를 배치하고, `components` 디렉터리에는 product card, cart modal처럼 여러 페이지에서 재사용될 수 있는 UI 컴포넌트 객체를 분리했습니다.

`tests/ui/features`에는 Gherkin 문법으로 작성한 BDD 시나리오를 두고, `tests/ui/steps`에는 각 시나리오와 매핑되는 step 구현을 배치했습니다.  
또한 `tests/api/clients`에는 API 응답 데이터를 조회하기 위한 클라이언트를 두고, `tests/integration`에서는 API 응답 데이터와 UI 표시 데이터 간의 일관성을 검증합니다.


## 테스트 시나리오

### UI 테스트

| Feature | 검증 내용 |
| --- | --- |
| Login | 올바른 계정으로 로그인 성공 여부와 잘못된 계정 입력 시 로그인 실패 여부 검증 |
| Navigation | 홈 화면에서 Login, Products, Cart 페이지로 정상 이동하는지 검증 |
| Products | 상품 추가 버튼 동작, 상품 추가 확인 modal 표시, Continue Shopping/View Cart 버튼 동작 검증 |
| Cart | 단일 상품 및 여러 상품의 장바구니 추가 여부와 장바구니 내 상품 삭제 동작 검증 |

### Integration 테스트

| 테스트 | 검증 내용 |
| --- | --- |
| 상품 검색 결과 일관성 검증 | 동일한 검색어로 조회한 UI 상품 목록과 API 응답 상품 목록을 비교하여 UI에 표시된 상품 ID와 API 응답 데이터에서 추출한 ID가 일치하는지 검증 |

UI 테스트는 `tests/ui/features`의 Gherkin 시나리오를 기준으로 작성했으며, 각 시나리오는 `tests/ui/steps`의 step 구현과 매핑됩니다.  
Integration 테스트에서는 Python `requests` 기반 API 클라이언트를 사용해 상품 검색 API 응답을 조회하고, Playwright로 수집한 UI 상품 데이터와 비교합니다.


## 실행 방법

### 1. 저장소 클론

```bash
git clone https://github.com/HwangMinHyeok/test_automation.git
cd test_automation
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. 테스트 실행

전체 테스트 실행:

```bash
pytest
```

UI 테스트 실행:

```bash
pytest tests/ui
```

Integration 테스트 실행:

```bash
pytest tests/integration
```

테스트는 기본적으로 Chromium 브라우저를 headless 모드로 실행합니다.  
테스트 실패 시 `artifacts/screenshots`와 `artifacts/traces` 디렉터리에 실패 분석을 위한 파일이 저장됩니다.


## 실패 분석 자료

테스트 실패 시 실패 원인을 분석할 수 있도록 스크린샷과 Playwright trace 파일을 저장합니다.

```text
artifacts/
├── screenshots/
│   └── {test_nodeid}.png
└── traces/
    └── {test_nodeid}.zip
```

| 저장 항목 | 경로 | 설명 |
| --- | --- | --- |
| Screenshot | `artifacts/screenshots/` | 실패 시점의 전체 화면 캡처 |
| Playwright trace | `artifacts/traces/` | 테스트 실행 흐름, DOM snapshot, 네트워크 요청 등을 확인할 수 있는 trace 파일 |

Playwright trace 파일은 아래 명령어로 확인할 수 있습니다.

```bash
playwright show-trace artifacts/traces/{trace_file}.zip
```


## 테스트 실행 결과

전체 테스트는 아래 명령어로 실행했습니다.

```bash
pytest
```

![pytest 실행 결과](docs/images/pytest-result.png)

전체 테스트가 정상적으로 통과하는 것을 확인했습니다.


## 향후 개선 사항

현재 프로젝트는 UI E2E 테스트와 API/UI 데이터 일관성 검증에 초점을 맞추고 있습니다.  
CI 환경에서의 자동 실행, 테스트 결과 리포트 생성, 테스트 데이터 관리 방식 개선 등을 통해 테스트 자동화 환경을 더 실무적인 형태로 확장할 수 있습니다.

- GitHub Actions 기반 CI 테스트 실행
- pytest-html을 활용한 테스트 결과 리포트 생성 및 시각화
- 테스트 데이터 및 계정 정보 외부화를 통한 관리 방식 개선
- 상품 검색 외 주요 사용자 흐름에 대한 API/UI 데이터 일관성 검증 시나리오 확대

