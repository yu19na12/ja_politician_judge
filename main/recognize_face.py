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
    similarity_percentage = max(0, 100 - distance * 100)
    return similarity_percentage

def recognize_face(image_path, model_file):
    """ 顔認識を行い、結果を画像に表示する """
    known_face_encodings, known_face_names = load_model(model_file)
    
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    face_locations = face_recognition.face_locations(img_rgb)
    face_encodings = face_recognition.face_encodings(img_rgb, face_locations)
    
    img_height, img_width, _ = img.shape
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

        highest_similarity = 0
        best_match_name = "Unknown"
        
        for known_face_encoding, name in zip(known_face_encodings, known_face_names):
            similarity = calculate_similarity(face_encoding, known_face_encoding)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match_name = name

        if highest_similarity >= 50:
            label = f"{best_match_name} ({highest_similarity:.2f}%)"
        else:
            label = "No match found"

        text_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        text_width, text_height = text_size
        text_x = max(left, 0)
        text_y = min(img_height - 10, bottom + text_height + 10)
        
        cv2.putText(img, label, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    
    cv2.imshow('Image with Face Recognition', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_face('./main/test_images/sample.jpeg', './main/model/politician_model.pkl')
