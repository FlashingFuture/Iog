# 커밋 메시지 및 브랜치명 컨벤션

## 배경

여러 세션/여러 작업자(Claude Code 포함)가 이어서 작업해도 히스토리만 보고 "무엇을, 왜" 했는지 파악할 수 있도록, 지금까지 이 저장소에서 실제로 사용해온 패턴을 정리한다.

## 브랜치명

**형식**: `<type>/<kebab-case-scope>`

기존 히스토리에서 관찰되는 실제 사용 예:

- `chore/monorepo-setup`
- `chore/coderabbit-auto-review`
- `feature/client-ui`

**scope는 넓은 이름 대신 실제 작업 단위를 구체적으로 반영한다.** 예를 들어 `feature/client`처럼 뭉뚱그리지 않고, 지금 하는 작업이 client의 UI 부분이면 `feature/client-ui`, 나중에 백그라운드 트래커 작업을 하면 `feature/client-tracker`처럼 분리한다. 작업 단위가 명확히 나뉘어 있어야 리뷰/병합 단위도 그만큼 작고 명확해진다.

## 커밋 메시지

**형식**: Conventional Commits 스타일, `<type>: <제목>`

**지금까지 사용한 type**:

| type | 의미 | 예 |
|---|---|---|
| `feat` | 새로운 기능/코드 추가 | `feat: scaffold pywebview client UI shell` |
| `chore` | 빌드/툴링/설정 등 기능 외 변경 | `chore: set up root uv workspace and pytest scaffold`, `chore: coderabbit auto review yaml` |

필요시 표준 Conventional Commits type도 함께 쓴다: `fix`(버그 수정), `docs`(문서만 변경), `test`(테스트 추가/수정), `refactor`(동작 변화 없는 구조 변경).

**본문 작성 원칙**: 제목은 간결한 요약(영어)으로, 본문은 **"무엇을 했는지"가 아니라 "왜 했는지"를 한글로** 설명한다. 코드 diff만 봐도 무엇이 바뀌었는지는 알 수 있으므로, 커밋 로그에는 그 변경의 배경/의도를 남긴다.

예 (`1b3795f`):
```
chore: set up root uv workspace and pytest scaffold

apps/client/ui의 개별 venv/lockfile을 루트 uv workspace로 통합해,
apps/client 하위에 Python 앱(백그라운드 프로세스 등)이 늘어나도
하나의 환경/락파일로 관리되도록 한다. pytest를 워크스페이스 dev
의존성으로 추가하고 apps/client/ui/tests에 스모크 테스트를 둔다.
```

**Claude Code로 작업한 커밋에는 아래 트레일러를 포함한다**:
```
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```
