![GaifaaYeepun](https://user-images.githubusercontent.com/42882840/80269234-b4ad1c80-86e8-11ea-8a02-567b854170d5.png)
====

## Overview
Djangoによる、日本語、タイ語、英語の単語、例文翻訳サイトプロジェクトです。
(タイ人、日本人向け)

## Requirement
### 運用サーバ

* Webサーバ(Windows Server+IISなど)(本番環境用)
* Python(3.6.7推奨)
* Git

### クライアント

* PC / スマートフォンなど


## Install
- 本番環境用 (**To Be Determined**)
- [開発環境用](./docs/ja/install/develop.md)


## How to use
メインページの単語・例文検索画面から、調べたい単語(または例文)を入力して検索する。
また、知りたい単語(または例文)がシステムに登録されていない場合は、リクエスト画面からシステム管理者に通知を送ることが出来る。

各画面の詳細は、以下を参照。
- [単語・例文検索画面](./docs/ja/howtouse_search.md)
- [リクエスト画面](./docs/ja/howtouse_request.md)
- Demo

<img src ="https://user-images.githubusercontent.com/42882840/80270542-f5f6f980-86f3-11ea-9383-059f04cd9fec.gif" alt="demo" width="400">


## Maintenance
- [単語・例文追加、変更](./docs/ja/maintenance_reqrecieved.md)
- [単語・例文リクエスト受領時の対応](./docs/ja/maintenance_dataedit.md)


## Structure
- [Database](./docs/ja/database.md)
