import os
import shutil

def copy_images(src_folder, dest_folder):
    """ コピー元フォルダからコピー先フォルダに画像をコピーする """
    # コピー先フォルダが存在しない場合は作成
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # コピー元フォルダを再帰的に探索
    for root, _, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_folder, file)
                shutil.copy(src_file, dest_file)
                print(f"Copied {src_file} to {dest_file}")

