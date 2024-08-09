# ja_politician_judge

## 仮想環境
### 仮想環境に入る
```
source ENV/bin/activate
```

### 仮想環境を終了する
```
deactivate
```

## module
```
pip freeze > requirements.txt
```

## 実行
### モデルのトレーニング
```
python main/train_model.py
```

### 実行
```
python main/main.py
```

## 顔検出
### 顔検出(Face Detection)
顔検出とは、入力された画像または動画から人間の顔の有無や位置を検出する処理のことです。つまり、画像内に顔があるかどうか、そしてあった場合はその位置(座標)を特定することが目的です。
検出アルゴリズムは特徴量(エッジ、輝度勾配など)を用いて顔らしい部分を見つけ出します。代表的な従来手法であるHaar-likeは OpenCVでは組み込まれています。近年では深層学習を使った高精度な顔検出手法も多数提案されています。

### 顔認識(Face Recognition)
顔認識は検出された顔から、誰の顔なのかを同定する処理を指します。つまり、個人の識別が目的です。
顔認識では、まず顔検出によって顔の位置が特定され、次に検出された顔画像から特徴量が抽出されます。そして、事前に登録された既知の顔画像の特徴量とのマッチングを行うことで、個人を識別します。
特徴量の抽出には、主成分分析(PCA)や線形判別分析(LDA)などの手法が従来から利用されてきましたが、近年は深層学習による高次元特徴量がよく使われるようになりました(FaceNet、VGGFace2など)。
顔認識はセキュリティゲート、入退室管理システムなどでの本人確認に加え、デジタルアルバムの自動顔タグ付けなどの用途があります。

つまり、顔検出は「顔の有無と位置検出」、顔認識は「個人の同定」が主な目的です。顔認識を行うには、事前に顔検出が必要不可欠な処理となります。両者は密接に関係しながらも、別個の処理概念となります。​​​​​​​​​​​​​​​

#### OpenCV(Haar Cascade)
- Haar Cascade手法を用いた従来の手法に基づく顔検出器が使用可能
- 軽量なアルゴリズムのため、処理速度は比較的速い
- 精度は他の深層学習ベースの手法に比べると低め

#### OpenCV(Yu Net)
- 畳み込みニューラルネットワーク (CNN)をベースとした、軽量で高速な顔検出アルゴリズム
- 顔検出だけでなく、目、鼻、口などのランドマーク検出に対応
- リアルタイム性と高精度のバランスが優れている

#### OpenCV(Yu Net)
- 畳み込みニューラルネットワーク (CNN)をベースとした、軽量で高速な顔検出アルゴリズム
- 顔検出だけでなく、目、鼻、口などのランドマーク検出に対応
- リアルタイム性と高精度のバランスが優れている

#### MTCNN (Multi-task Cascaded Convolutional Networks)
- ディープラーニングベースの顔検出/ランドマーク検出アルゴリズム
- 3つのネットワークが直列につながったカスケード構造を採用
- 顔検出の精度が非常に高く、角度や照明の変化にも頑健
- フェイスランドマーク検出も高精度に行える
- ただし、ディープラーニングモデルなので処理速度は遅め
- GPU使用時の高速化が可能

#### face_recognition
- dlib の顔検出/顔認識エンジンを Pythonラッパーでパッケージ化
- 顔検出/エンコーディング/クラスタリングなどの機能を提供
- 顔認識の精度は非常に高い
- 検出モデルとして、”hog”と”cnn”の2つが使用可能。”cnn”はGPU/CUDAを使用することで高速化に対応。
- アップサンプリングに対応しており、精度向上が期待できる