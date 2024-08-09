import face_recognition
import pickle
import cv2
import numpy as np

def load_model(model_file):
    """ モデルをロードする """
    with open(model_file, 'rb') as f:
        known_face_encodings, known_face_names = pickle.load(f)
    return known_face_encodings, known_face_names

def calculate_similarity(face_encoding1, face_encoding2):
    """ 顔の特徴量間の距離を計算し、パーセンテージの類似度を返す """
    distance = np.linalg.norm(face_encoding1 - face_encoding2)
    # 距離を逆にしてパーセンテージに変換
    similarity_percentage = max(0, 100 - distance * 100)  # 距離が小さいほど似ているとする
    return similarity_percentage

def recognize_face(image_path, model_file):
    """ 顔認識を行い、結果を画像に表示する """
    known_face_encodings, known_face_names = load_model(model_file)
    
    # 画像の読み込み
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 顔の位置を検出
    face_locations = face_recognition.face_locations(img_rgb)
    face_encodings = face_recognition.face_encodings(img_rgb, face_locations)
    
    # 画像の高さと幅を取得
    img_height, img_width, _ = img.shape
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # 顔の位置を枠で表示
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        
        # 顔認識
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        highest_similarity = 0
        
        if True in matches:
            for i, match in enumerate(matches):
                if match:
                    # 類似度を計算
                    similarity = calculate_similarity(face_encoding, known_face_encodings[i])
                    if similarity > highest_similarity:
                        highest_similarity = similarity
                        name = known_face_names[i]
        
        # 類似度を画像の下に表示
        similarity_label = f"Similarity: {highest_similarity:.2f}%"
        text_size, _ = cv2.getTextSize(similarity_label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        text_width, text_height = text_size
        
        # テキストが画像の下に収まるように位置を調整
        text_x = max(left, 0)
        text_y = min(img_height - 10, bottom + text_height + 10)  # 画像の下部に収める
        
        cv2.putText(img, similarity_label, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    
    # 画像を表示
    cv2.imshow('Image with Face Recognition', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_face('./main/test_images/sample.jpg', './main/model/politician_model.pkl')
