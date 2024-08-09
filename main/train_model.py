import face_recognition
import pickle
import os

def train_model_from_folder(folder_path, model_file):
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue  # 画像ファイルでない場合はスキップ
        
        img = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(img)
        
        for face_encoding in face_encodings:
            known_face_encodings.append(face_encoding)
            known_face_names.append(os.path.splitext(filename)[0])  # ファイル名を名前として使用

    with open(model_file, 'wb') as f:
        pickle.dump((known_face_encodings, known_face_names), f)
    
    print("Model trained and saved to", model_file)

# 使用例
train_model_from_folder('./main/train_images', './main/model/politician_model.pkl')
