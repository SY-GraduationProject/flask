from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from darkflow.net.build import TFNet
import cv2

#Flask 인스턴스 생성
app = Flask(__name__)
api = Api(app)

## 웹 카메라
def capture(camid = 0):
    cam = cv2.VideoCapture(camid, cv2.CAP_DSHOW)
    if cam.isOpened() == False:
        print('cant open the cam (%d)' %camid)
        return None

    ret, frame = cam.read()
    if frame is None:
        print('frame is not exist')
        return None

    cv2.imwrite('../data/testset/demo.jpeg', frame, params=[cv2.IMWRITE_PNG_COMPRESSION, 0])
    cam.release()

## 이미지 detection
class detection(Resource):
    def get(self):
        capture()

        options = {"model": "./cfg/my-tiny-yolo.cfg", "load": -1, "threshold": 0.3}

        tfnet = TFNet(options)

        imgcv = cv2.imread("../data/testset/demo.jpeg")
        result = tfnet.return_predict(imgcv)

        # label만 따로 파싱
        l = []
        for i in result:
            q = i['label']
            l.append(q)

        print(result)

        return jsonify(l)

## URL Router에 맵핑
api.add_resource(detection, '/detection')


#서버 실행
if __name__ == '__main__':
    app.run(
        host="210.117.181.74",
        port=5000,
        debug=True)
