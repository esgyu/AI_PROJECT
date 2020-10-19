# 포스코 청년 AI 빅데이터 아카데미 11기 최강 2조 마지막 AI 프로젝트
----
  1. stream.py : flask 서버를 8787포트로 열어줌. 명령어 프롬프트에서 ipconfig 하면 자기 아이피 (192.168.0.x) 주소 볼 수 있음. 다른 컴퓨터에서 사용하고 싶으면 우리 공유기 게이트웨이 주소(192.168.0.1)로 로그인 후 고급설정 -> NAT/라우터 관리 -> 포트포워드 수정 메뉴에서 아이피주소 및 포트번호 설정(겹치면 안됨). stream.py의 app.run의 port부분을 설정한 포트번호로 수정하게 되면 stream.py 실행 시 http://posproject201013.iptime.org:port번호 로 외부에서 접근이 가능함!
  
  2. tts_stt.py : 소스를 보면 os.environ['GOOGLE_APPLICATION_CREDENTIALS']='./STT_TTS/파일이름.json' 이라고 되어있는 부분이 있는데, STT_TTS 폴더 밑에 .json의 유저 인증 키 파일을 넣고
  gcp sdk 설치 후, 해당 사용자로 로그인해서 허용 설정해야함. 진수님이 잘 알거라고 믿음.. https://webnautes.tistory.com/1247 이곳이 상당히 자세하게 설명되어있으니 참고해도 좋음.
  
  3. postech/test.rar : 포스텍 서버에서 작동하는 소스코드를 통으로 압축한 파일. 포스텍 서버에 업로드 한 후 , 압축을 풀어 MaskTheFace/server.ipynb 파일이 서버 역할을 수행함. 하나하나 읽어보면 이해할 수 있으리라 믿음... 기본적인 각 코드들의 동작은 제목을 보고 유추할 수 있으나 flask stream.py 서버를 새로 여는 경우 cv2.CaptureVideo('주소')의 '주소'부분을 바꾸고 진행해야함! 현재 face embedding이라고 되어있는 부분의 두 블록은 arcface의 face feature extraction 성능이 안좋아보여서 주석쳐놓음. video = cv2.VideoCapture('http://posproject201013.iptime.org:8787/video_feed') 로 시작하는 블록의 if len(faces) != 0 내부의 긴 주석쳐놓은 부분이 사전에 face embedding을 뽑아놓고 현재 웹캠의 프레임에서 얼굴을 찾아 바운딩 박스만 crop 한 후, 114x114 사이즈로 resizing하고 feature extraction을 진행하여 cosine similiarity를 계산하여 argmax를 찾는 과정. known_faces_encoding은 files = glob.glob('../users/\*.jpg')에서 모든 .jpg 파일을 읽어오는데, 원하는 폴더로 경로를 변경하여 진행해야함  
  
  -- 런타임에 등장하는 no module 에러같은 것들은 pip install 로 대부분 해결할 수 있음. 
