
![logo](https://itoishoukai.com/od_course/logo.png)

必要な手順のリストになります。  
詳細は動画を参照ください。

### 📋 Table of content
 1. [gitのインストール](#git)
 2. [コードのダウンロード](#code)
 3. [Pycharmの設定](#pycharm)
    1. [venv](#venv)
    2. [terminal](#terminal)
 4. [YOLOv5のダウンロード](#yolov5)
 5. [weightsを保存](#weghts)

### 1.gitのインストール <a name="git"></a>
YOLOv5を取得するためには、gitが必要です。  
gitはコードのバージョン管理をするもので、<a href="https://github.com/">github</a>というサービスには、様々なコードが公開されており、YOLOv5もそこからダウンロードします。  
下記からダウンロード、インストールをしましょう。

https://git-scm.com/downloads

### 2.OpenCVのインストール <a name="code"></a>
カメラの起動に必要なopencv-pythonのライブラリをインストールします。
```
git clone https://github.com/itoiyoshihiko/ObjectDetectionCourseLocal.git
```

### 3.Pycharmの設定 <a name="pycharm"></a>
Pycharmを使っていく上での設定です。
 - venv <a name="venv"></a>
 - terminal <a name="terminal"></a>

### 4.YOLOv5のダウンロード <a name="yolov5"></a>
gitがインストールできたら、YOLOv5をダウンロードします。
次のコードをTerminalで実行します。

```
git clone https://github.com/ultralytics/yolov5.git
pip install -r yolov5/requirements.txt
```



### 5.weightsを保存 <a name="weghts"></a>
GoogleDriveに保存されたweightsフォルダをダウンロードして、ObjectDetectionCourseLocalの中に保存しましょう。  
使うのは、best.ptになりますが、フォルダごとおいておきます。
