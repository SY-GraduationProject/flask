# Darkflow
- darkflow를 이용해 학습한 모델로 detection한다.
- 현재 검출할 수 있는 재료는 egg, onion, orange, cabbage, cucumber이다.


# 사용법
- 본인 가상환경의 darkflow 폴더에 flask.py파일을 넣고 flask 서버를 열어둔다.
- 웹 캠을 이용해 캡쳐한 이미지는 data - testset 폴더에 저장된다.

# 로직
### React_native -> Spring
- React_native에서 reload 버튼을 누르면 이미지 detection을 Spring에 요청

### Spring -> Flask
- Spring에서 Flask서버에 이미지 detection을 요청

### Flask
- 웹 캠이 이미지를 캡쳐 후 data - testdata - demo.jpeg 파일로 저장
- 저장된 이미지를 detection

### Flask -> Spring
- detection한 결과값에서 label만 파싱해 JSON으로 spring서버에 응답

### Spring -> React_native
- 응답받은 결과값을 db에 저장후 JSON형식으로 React_native에 응답
