from flask import Flask, render_template, Response, redirect
import cv2
import time

video = cv2.VideoCapture(0)
app = Flask(__name__)

def gen():
    """Video streaming generator function."""
    while True:
        ret, frame = video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)

        # print("after get_frame")
        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        else:
            print("frame is none")
        time.sleep(0.2)


#   http://posproject201013.iptime.org:8787/video_feed

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8787, debug=True, threaded=True)


