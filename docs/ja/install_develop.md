# 開発環境インストール
## 1. 必須ソフトウェアのインストール
以下をインストール(詳細は省略)
* Python
    * 推奨バージョン3.6.7
    * 仮想環境を作成することを推奨
    * 以降、実行ファイルにパスが通っているもの(pythonコマンドで実行可能)とする
* Git

## 2. プロジェクトファイルのClone

このgithubプロジェクトをcloneする。
```
git clone https://github.com/jocv-thai/pleethai.git
````

## 3. 依存パッケージのインストール

プロジェクトが使用するPython依存パッケージをインストール。
```
cd pleethai
pip install -r requirements.txt
````

## 4. DBの構築
````
python manage.py migrate
````

## 5. 管理ユーザの作成
````
python manage.py createsuperuser
````
* 表示されるメッセージに従ってユーザ名、パスワードなどを入力する。

## 6. システム起動
````
python manage.py runserver
````
* ブラウザで`http://127.0.0.1:8000/`にアクセスすることで、画面表示できる。


## 7. DBデータの登録
[単語・例文追加、変更](./maintenance_dataedit.md)の手順に従い、データを登録する。

* 登録する各データの詳細は、[Database](./database.md)を参照
* [動作確認用サンプルデータ](https://drive.google.com/open?id=1AuRX2f7LATfLzXgWiI3-wmAbNUo3tt8o)

