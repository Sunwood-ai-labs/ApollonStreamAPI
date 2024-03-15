import subprocess
from PIL import Image
import io
import time

def save_screenshot(filename):
    start_time = time.time()

    # スクリーンショットの取得
    start_screencap_time = time.time()
    result = subprocess.check_output(['adb', 'exec-out', 'screencap', '-p'])
    end_screencap_time = time.time()
    screencap_time = end_screencap_time - start_screencap_time

    # 画像データの変換
    start_conversion_time = time.time()
    image = Image.open(io.BytesIO(result))
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    end_conversion_time = time.time()
    conversion_time = end_conversion_time - start_conversion_time

    # 画像の保存
    start_save_time = time.time()
    image.save(filename, "JPEG")
    end_save_time = time.time()
    save_time = end_save_time - start_save_time

    end_time = time.time()
    total_time = end_time - start_time

    print(f"スクリーンショット取得時間: {screencap_time:.3f}秒")
    print(f"画像データ変換時間: {conversion_time:.3f}秒")
    print(f"画像保存時間: {save_time:.3f}秒")
    print(f"全体の処理時間: {total_time:.3f}秒")

save_screenshot("screenshot.jpg")
