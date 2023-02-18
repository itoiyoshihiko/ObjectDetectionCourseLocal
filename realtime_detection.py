"""
launch_web_camera.pyとtest_yolov5.pyを組み合わせることで、
リアルタイムに検知できるシステムができます。

"""
import glob
import os

import torch
import cv2

def detect_img(model, image):
    # 推論の実行
    model.conf = 0.6  # confidence threshold (0-1)
    results = model(image)

    # 結果を返す
    return results

if __name__ == '__main__':
    weights_dir = "weights/best.pt"
    model = torch.hub.load('yolov5', 'custom', path=weights_dir, source='local')

    capture = cv2.VideoCapture(0)

    while (True):
        ret, frame = capture.read()
        if ret:

            # 位置検出
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = detect_img(model, frame)
            # 結果保存
            results.save(save_dir="result")
            # 結果読み込み
            img = cv2.cvtColor(cv2.imread("result/image0.jpg"), cv2.COLOR_BGR2RGB)
            os.remove("result/image0.jpg")
            # 結果表示
            results.print()
            cv2.imshow('camera', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    capture.release()
    cv2.destroyAllWindows()