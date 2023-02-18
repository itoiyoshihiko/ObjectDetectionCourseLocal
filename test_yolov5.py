"""
3-2-5.自分で学習したモデルを使ってみる
と同じようなコードをLocal環境で動かします。
"""
import torch

if __name__ == '__main__':
    weights_dir = "weights/best.pt"
    model = torch.hub.load('yolov5', 'custom', path=weights_dir, source='local')

    # 動かすだけなので、yolov5においてある画像を利用します
    image_url = 'https://github.com/ultralytics/yolov5/raw/master/data/images/bus.jpg'

    # 推論の実行
    model.conf = 0.6  # confidence threshold (0-1)
    results = model(image_url)

    # 結果の表示
    results.print()