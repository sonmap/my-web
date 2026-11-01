# 이 저장소의 규칙

- 프로젝트: Cloud Run으로 돌아가는 간단한 웹페이지
- GCP 프로젝트 ID: (3단계에서 채움)
- 리전: asia-northeast3
- Cloud Run 서비스 이름: my-web

## 꼭 지킬 것
- 브랜치 이름은 agent/<이슈번호>-<짧은설명>
- main 브랜치에 직접 커밋하지 말 것. 반드시 PR로
- gcloud 명령을 직접 실행하지 말 것. 배포는 GitHub Actions만
- 서비스 계정 키 파일을 저장소에 넣지 말 것
- requirements.txt에 새 패키지를 추가할 때는 PR 설명에 이유를 쓸 것
