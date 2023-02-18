import cv2

# このpyファイルを直接実行する場合のみ動かすという条件
# pyファイルはほかから読み込んで使うときもありますが、その時は実行されない
if __name__ == '__main__':
    # 接続されているカメラを取得
    # 複数接続されている場合には、かっこの中の数値を変更します。
    # cv2.VideoCapture(カメラのID)
    capture = cv2.VideoCapture(0)

    # 「q」が押されるまで繰り返し
    while (True):
        # カメラから画像取得
        # ret: 取得成功したかどうか
        # frame: numpyのndarrayで画像
        ret, frame = capture.read()
        # 取得に成功した場合、表示する
        if ret:
            # 画像表示
            cv2.imshow('camera', frame)
            # キー操作を確認
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # 終了処理
    capture.release()
    cv2.destroyAllWindows()

