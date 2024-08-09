import face_recognition
import pickle

def load_model(model_file):
    """ モデルをロードする """
    with open(model_file, 'rb') as f:
        known_face_encodings, known_face_names = pickle.load(f)
    return known_face_encodings, known_face_names

def recognize_face(image_path, model_file):
    """ 顔認識を行う """
    known_face_encodings, known_face_names = load_model(model_file)
    img = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        print(f"Face recognized as: {name}")

if __name__ == "__main__":
    recognize_face('./main/test_images/sample.jpg', './main/model/politician_model.pkl')
