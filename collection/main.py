import collect_image

# キーワードと保存先のディレクトリを指定
keywords = ['TakaichiSanae']  # 収集する画像のキーワード
num_images = 100  # 収集する画像の枚数

for keyword in keywords:
    save_dir = f'./collection/images/{keyword}'
    save_name = keyword  # 保存名をキーワードに設定
    # 画像のダウンロードと処理を実行
    collect_image.download_images(keyword, num_images, save_dir, save_name)