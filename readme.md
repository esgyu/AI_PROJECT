포스코 청년 AI 빅데이터 아카데미 11기 최강 2조 마지막 AI 프로젝트

1. 소스설명
  1. stream.py : flask서버를 8787포트로 열어줌. 명령어 프롬프트에서 ipconfig 하면 자기 아이피 (192.168.0.x) 로 된 주소 볼 수 있음
  다른 컴퓨터에서 사용하고 싶으면 우리 공유기 게이트웨이 주소(192.168.0.1)로 로그인 후 고급설정 -> NAT/라우터 관리 -> 포트포워드 수정 메뉴에서 아이피주소 및 포트번호 설정(겹치면 안됨)
  stream.py의 app.run의 port부분을 설정한 포트번호로 수정하게 되면 stream.py 실행 시 http://posproject201013.iptime.org:port번호로 외부에서 접근이 가능함!
  
  2. tts_stt.py : 소스를 보면 os.environ['GOOGLE_APPLICATION_CREDENTIALS']='./STT_TTS/파일이름.json' 이라고 되어있는 부분이 있는데, STT_TTS 폴더 밑에 .json의 유저 인증 키 파일을 넣고
  gcp sdk 설치 후, 해당 사용자로 로그인해서 허용 설정해야함. 진수님이 잘 알거라고 믿음..
  
  3. postech/test.rar : 포스텍 서버에서 작동하는 소스코드를 통으로 압축한 파일. 포스텍 서버에 업로드 한 후 , 압축을 풀어 MaskTheFace/server.ipynb 파일이 서버 역할을 수행함.
  하나하나 읽어보면 이해할 수 있으리라 믿음...
