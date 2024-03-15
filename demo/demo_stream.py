from adb_screencap_streaming import ADBScreenshot
import cv2

def main():
    adb_path = r"C:\Prj\platform-tools_r35.0.0-windows\platform-tools\adb.exe"  # ADBのパスを指定
    bilder = ADBScreenshot(
        adb_path,
        "192.168.0.147:5555",  # ADBデバイスのアドレス
        show_capture_keys="ctrl+alt+z",  # cv2.imshow() を有効/無効にするキー
        show_fps_keys="ctrl+alt+f",  # FPS表示を有効/無効にするキー
        kill_screencap_keys="ctrl+alt+x",  # キャプチャプロセスを終了するキー
    )

    for frame in bilder.get_adb_screenshots(
        sleeptime=None,
        resize_width=None,
        resize_height=None,
        resize_percent=None,
        interpolation=cv2.INTER_AREA,
    ):
        # ここでフレームに対する処理を行う
        cv2.imshow('ADB Screencap', frame)
        print('Do some stuff here', end='\r')

        # 'q'キーが押されたらループを抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    bilder.kill_screencap()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
