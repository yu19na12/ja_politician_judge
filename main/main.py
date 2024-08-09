import cv2
import matplotlib.pyplot as plt
import os

print("Current working directory:", os.getcwd())

# jpeg 画像の読み込み
img = cv2.imread('./main/images/sample.jpg')

# 画像が読み込めているか確認
if img is None:
    print("Error: 'sample.jpg' not found.")
else:
    # グレースケール変換
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 画像の表示→ matplotlib では cv2.COLOR_BGR2RGB の設定が必要
    plt.imshow(img_gray, cmap='gray')
    plt.show()