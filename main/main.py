import cv2
import face_recognition

# 画像の読み込み
img = cv2.imread('./main/images/sample.jpg')

# 画像が読み込めているか確認
if img is None:
    print("Error: 'sample.jpg' not found.")
else:
    # 色空間をRGBに変換（OpenCVはBGR形式で画像を読み込むため）
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 顔の位置を検出
    face_locations = face_recognition.face_locations(img_rgb)

    # 顔の特徴を抽出
    face_encodings = face_recognition.face_encodings(img_rgb, face_locations)

    # 顔の検出結果を表示（BGR形式に戻す）
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

    # 画像を表示
    cv2.imshow('Detected Faces', img)

    # face_locations と face_encodings をターミナルに出力
    print("Face Locations:", face_locations)
    print("Face Encodings:", face_encodings)

    # ウィンドウを閉じるための処理
    cv2.waitKey(0)
    cv2.destroyAllWindows()
