from fastapi import FastAPI, WebSocket
import subprocess
import asyncio
from PIL import Image
import io

app = FastAPI()

async def capture_and_send_screenshot(websocket: WebSocket, path: str = None):
    """ADBコマンドまたは指定されたパスからスクリーンショットを取得し、JPEGとしてWebSocketを通じて送信する"""
    if path:
        # 指定されたパスから画像を読み込む
        with open(path, "rb") as image_file:
            result = image_file.read()
    else:
        # ADBを使用してスクリーンショットを取得
        result = subprocess.check_output(['adb', 'exec-out', 'screencap', '-p'])
    
    image = Image.open(io.BytesIO(result))
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    with io.BytesIO() as output:
        image.save(output, format="JPEG")
        jpeg_data = output.getvalue()
        await websocket.send_bytes(jpeg_data)

@app.websocket("/stream")
async def stream_screen(websocket: WebSocket):
    """Androidデバイスのスクリーンショットをリアルタイムでストリーミングするエンドポイント"""
    await websocket.accept()
    while True:
        await capture_and_send_screenshot(websocket)
        await asyncio.sleep(0.1)

@app.websocket("/demo")
async def stream_demo_image(websocket: WebSocket):
    """デモ画像をリアルタイムでストリーミングするエンドポイント"""
    await websocket.accept()
    while True:
        await capture_and_send_screenshot(websocket, "demo/demo.jpg")
        await asyncio.sleep(0.1)
