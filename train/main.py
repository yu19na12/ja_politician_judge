import os
import shutil
import collect_images
import train_model

def clear_folder(folder_path):
    """ 指定したフォルダの中身を空にする """
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        print(f"Cleared contents of {folder_path}")
    else:
        print(f"Folder {folder_path} does not exist.")

if __name__ == "__main__":
    # フォルダのパスを指定
    src_folder = './collection/images/'
    dest_folder = './train/train_images/'

    # dest_folder の中身を空にする
    clear_folder(dest_folder)
    
    # collect_images.py を実行して画像をコピーする
    print("Starting image collection...")
    src_folder = './collection/images/'
    dest_folder = './train/train_images/'
    collect_images.copy_images(src_folder, dest_folder)
    
    # train_model.py を実行してモデルをトレーニングする
    print("Starting model training...")
    train_model.train_model_from_folder('./train/train_images', './train/model/politician_model.pkl')
    
    print("Image collection and model training completed.")
