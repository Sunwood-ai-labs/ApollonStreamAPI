
<h1>
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/Manim-Examples-Docker/main/docs/Animatos.png" height=300px align="right"/>
ApollonStreamAPI
</h1>

ApolloStreamは、Androidデバイスのスクリーンショットをリアルタイムでストリーミングするためのツールです。FastAPIを使用してWebSocketサーバーを構築し、ADBコマンドを使用してスクリーンショットを取得します。

## 機能

- Androidデバイスのスクリーンショットをリアルタイムでストリーミング
- 取得したスクリーンショットをJPEG形式で保存
- デモ画像のストリーミングにも対応

## 使用方法

### サーバー側

1. FastAPIとUvicornをインストールします。

```bash
pip install fastapi uvicorn
```

2. `api/screencap_server.py`を実行してサーバーを起動します。

```bash
uvicorn api.screencap_server:app --host 0.0.0.0 --port 8000
```

### クライアント側

1. `demo/demo_screencap_client.py`を実行してクライアントを起動します。

```bash
python demo/demo_screencap_client.py
```

2. クライアントは、サーバーからストリーミングされたスクリーンショットを受信し、`received_image.jpg`として保存します。

## 疎通確認

スタンドアロンでのスクリーンショット取得と保存の処理時間を確認するには、`demo/demo_screenshot_standalone.py`を実行します。

```bash
python demo/demo_screenshot_standalone.py
```

このスクリプトは、ADBコマンドを使用してスクリーンショットを取得し、画像データの変換と保存を行います。処理時間が出力されます。

## ADBコマンドのヘルプ

ADBの`screencap`コマンドのヘルプは以下の通りです。

```bash
(ApolloStream) C:\Prj\_ApolloStream\demo>adb shell screencap -h    
usage: screencap [-hp] [-d display-id] [FILENAME]
   -h: this message
   -p: save the file as a png.
   -d: specify the physical display ID to capture (default: 0)
       see "dumpsys SurfaceFlinger --display-id" for valid display IDs.
If FILENAME ends with .png it will be saved as a png.
If FILENAME is not given, the results will be printed to stdout.
```

## 注意事項

- ApolloStreamを使用するには、AndroidデバイスとADBの設定が正しく行われている必要があります。
- サーバーとクライアントは同じネットワーク上で実行してください。
- デモ画像のストリーミングには、`demo/demo.jpg`が必要です。
