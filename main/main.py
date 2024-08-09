import cv2

def main():
    # 画像の読み込み
    img = cv2.imread('./main/test_images/sample.jpg')

    # 画像が読み込めているか確認
    if img is None:
        print("Error: 'test_images/sample.jpg' not found.")
        return

    # 顔の検出結果を表示（BGR形式に戻す）
    cv2.imshow('Image', img)

    # 画像を表示
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
