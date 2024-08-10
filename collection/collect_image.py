import os
import face_recognition
from icrawler.builtin import BingImageCrawler

def create_folder(folder_path):
    """フォルダが存在しない場合に作成します。"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def delete_non_single_person_images(folder_path):
    """1人以上の人物が検出された画像を削除します。"""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # 画像を読み込む
            image = face_recognition.load_image_file(file_path)
            # 顔を検出する
            face_locations = face_recognition.face_locations(image)
            # 顔が1人以上検出された場合は画像を削除
            if len(face_locations) != 1:
                os.remove(file_path)
                print(f"Deleted {filename} because it contains {len(face_locations)} faces.")
        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")

def rename_images(folder_path, prefix):
    """画像の名前を変更します。"""
    for i, filename in enumerate(os.listdir(folder_path), start=1):
        # 新しいファイル名を作成（ゼロパディング）
        new_name = f"{prefix}{str(i).zfill(3)}.jpg"
        # 古いファイルパスと新しいファイルパス
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        # ファイル名を変更
        os.rename(old_path, new_path)

def download_images(keyword, num_images, save_dir, save_name):
    create_folder(save_dir)

    # クローラーの設定
    crawler = BingImageCrawler(storage={'root_dir': save_dir})

    try:
        # 画像の検索とダウンロード
        crawler.crawl(keyword=keyword, max_num=num_images)
    except Exception as e:
        print(f"An error occurred: {e}")

    # 画像内の人物数をチェックして削除
    delete_non_single_person_images(save_dir)

    # ダウンロードが終了した後、画像のリネーム処理を実行
    rename_images(save_dir, prefix=f"{save_name}")
    print(f"Successfully renamed images for keyword: {keyword}")

if __name__ == "__main__":
    # キーワードと保存先のディレクトリを指定
    keywords = ['TakaichiSanae']  # 収集する画像のキーワード
    num_images = 100  # 収集する画像の枚数

    for keyword in keywords:
        save_dir = f'./collection/images/{keyword}'
        save_name = keyword  # 保存名をキーワードに設定
        # 画像のダウンロードと処理を実行
        download_images(keyword, num_images, save_dir, save_name)
