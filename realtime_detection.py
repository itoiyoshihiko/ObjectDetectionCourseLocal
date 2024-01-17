"""
launch_web_camera.pyとtest_yolov5.pyを組み合わせることで、
リアルタイムに検知できるシステムができます。

"""
import glob
import shutil

import torch
import cv2

# メールの送信
from mail import send_mail

def detect_img(model, image):
    # 推論の実行
    model.conf = 0.6  # confidence threshold (0-1)
    results = model(image)

    # 結果を返す
    return results

def add_result(image, results, x, y):
    # 結果から検出された物体の名前を取得する
    results_name = [row["name"] for ind, row in results.pandas().xyxy[0].iterrows()]
    # リストにある重複をカウントする
    results_count = {i: results_name.count(i) for i in results_name}
    str = ""
    offset = 0
    for key in results_count.keys():
        str = f"{key}:{results_count[key]}"
        # 文字を追加する
        image = cv2.putText(image, str, (x, y+offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        offset+=30
    return image

if __name__ == '__main__':
    # weights_dir = "weights/best.pt"
    # model = torch.hub.load('yolov5', 'custom', path=weights_dir, source='local')
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

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
            shutil.rmtree("result")
            # 文字の追加
            img = add_result(img, results, 10, 30)
            # 結果表示
            results.print()
            cv2.imshow('camera', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # 異常時のメール処理 参考：検出結果０件の場合
            if len(results.pandas().xyxy[0]) == 0:
                send_mail(
                    send_message="物体検出で閾値を下回りました",
                    to_email="", # 送信先メールアドレス
                    from_email="", # 送信元メールアドレス
                    account="", # メールのアカウント　メールアドレスと同じ場合が多い
                    password="", # メールのパスワード
                    smtp_server="", # メールサーバー
                    smtp_port=465 # メールサーバーのポート番号
                )
                # 一度メールを送信したら、カメラを止める
                break

    capture.release()
    cv2.destroyAllWindows()