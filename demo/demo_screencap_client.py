import asyncio
import websockets
import io
from PIL import Image


async def receive_and_save_image():
    uri = "ws://localhost:8000/stream"  # WebSocket接続のURI
    async with websockets.connect(uri) as websocket:
        # サーバーからのバイナリデータ（JPEG画像）を受信
        data = await websocket.recv()

        # 受信したデータをファイルに保存
        with open("received_image.jpg", "wb") as image_file:
            image_file.write(data)
            print("画像を受信し、保存しました。")

# イベントループを実行して、画像受信関数を呼び出す
asyncio.run(receive_and_save_image())