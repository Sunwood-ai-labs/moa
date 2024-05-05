
<p align="center">
<img src="docs/moa_icon.jpeg" width="100%">
<br>
<h1 align="center">MOA</h1>
<h2 align="center">
  ～ Magic of AWS ～

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/MakiAi/MOA)
[![MOA - Sunwood-ai-labs](https://img.shields.io/static/v1?label=MOA&message=Sunwood-ai-labs&color=blue&logo=github)](https://github.com/MOA/Sunwood-ai-labs "Go to GitHub repo")
[![stars - Sunwood-ai-labs](https://img.shields.io/github/stars/MOA/Sunwood-ai-labs?style=social)](https://github.com/MOA/Sunwood-ai-labs)
[![forks - Sunwood-ai-labs](https://img.shields.io/github/forks/MOA/Sunwood-ai-labs?style=social)](https://github.com/MOA/Sunwood-ai-labs)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/MOA)](https://github.com/Sunwood-ai-labs/MOA)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/MOA)](https://github.com/Sunwood-ai-labs/MOA)
[![GitHub Release](https://img.shields.io/github/v/release/Sunwood-ai-labs/MOA?sort=date&color=red)](https://github.com/Sunwood-ai-labs/MOA)
[![GitHub Tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/MOA?color=orange)](https://github.com/Sunwood-ai-labs/MOA)

  <br>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリは[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage)を活用しており、リリースノートやREADME、コミットメッセージの9割は[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage) ＋ [claude.ai](https://claude.ai/)で生成しています。

## 🌟 はじめに

MOA (Magic of AWS) は、初心者でも Docker を使って AWS CLI v2 を簡単に使えるようにすることを目的としたプロジェクトです。Docker を利用することで、AWS CLI がプリインストールされた独立した環境を作成でき、ローカルマシンの設定を変更する必要がなくなります。

## 🚀 始め方

### 前提条件

始める前に、以下のものがマシンにインストールされていることを確認してください。

- Docker
- Docker Compose
- Visual Studio Code (オプションですが、より良い開発体験のために推奨されます)

### インストール

1. リポジトリをクローンします。

```bash
git clone https://github.com/Sunwood-ai-labs/MOA.git
```

2. プロジェクトディレクトリに移動します。

```bash
cd MOA
```

3. プロジェクトルートに `.env` ファイルを作成し、AWS アクセスキー ID とシークレットアクセスキーを追加します。

```plaintext
AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY
```

> ⚠️ **重要**: 機密性の高い AWS 認証情報を誤ってコミットしないように、必ず `.env` ファイルを `.gitignore` に追加してください。

### 使い方

1. Visual Studio Code でプロジェクトを開きます。

2. VS Code でターミナルを開き、以下のコマンドを実行して Docker コンテナをビルドして起動します。

```bash
docker-compose up
```

3. コンテナが起動したら、次のコマンドを実行してコンテナ内で Bash シェルを開きます。

```bash
docker-compose run exec app /bin/bash
```

4. コンテナ内で、AWS CLI コマンドを使用できるようになりました。例えば、S3 バケットを作成してファイルをアップロードしてみましょう。

```bash
# S3 バケットを作成
[root@xxxxxxxxxxxx:/workdir]# aws s3 mb s3://test-20210711
make_bucket: test-20210711

# S3 バケットを一覧表示
[root@xxxxxxxxxxxx:/workdir]# aws s3 ls
2021-07-11 09:46:05 test-20210711

# S3 バケットにファイルをアップロード
[root@xxxxxxxxxxxx:/workdir]# aws s3 cp .env_sample s3://test-20210711/
upload: ./.env_sample to s3://test-20210711/.env_sample
```

おめでとうございます！Docker コンテナ内で AWS CLI v2 を設定して使用することに成功しました。

## 🛠️ プロジェクト構造

プロジェクトの構造は次のようになっています。

```plaintext
.
├── .env                  # 環境変数ファイル (リポジトリには含まれていません)
├── .env.example          # 環境変数ファイルの例
├── .gitattributes        # Git 属性の設定
├── .github/              # GitHub 固有のファイルと設定
│   └── workflows/        # GitHub Actions ワークフロー
├── Dockerfile            # AWS CLI コンテナをビルドするための Dockerfile
├── README.md             # プロジェクトのドキュメント
├── app.py                # メインアプリケーションファイル
├── docker-compose.yml    # Docker Compose 設定
└── docs/                 # ドキュメントファイル
    ├── moa_icon.jpeg     # プロジェクトアイコン
    └── page_front.md     # フロントページのドキュメント
```

## 📝 更新情報

更新情報とリリースノートについては、[GitHub リリース](https://github.com/Sunwood-ai-labs/MOA/releases)ページを参照してください。

## 🤝 コントリビューション

コントリビューションを歓迎します！プロジェクトに貢献したい場合は、以下の手順に従ってください。

1. リポジトリをフォークします。
2. 新しい機能やバグ修正用のブランチを作成します。
3. 変更を加え、わかりやすいコミットメッセージでコミットします。
4. フォークしたリポジトリに変更をプッシュします。
5. メインリポジトリにプルリクエストを送信します。

## 📄 ライセンス

このプロジェクトは[MIT ライセンス](LICENSE)の下でライセンスされています。

## 🙏 謝辞

MOA の開発に影響を与え、貢献してくれた以下のプロジェクトとリソースに感謝の意を表します。

- [AWS CLI](https://aws.amazon.com/cli/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

## 📧 お問い合わせ

ご質問、ご提案、フィードバックがある場合は、[support@sunwoodai.com](mailto:support@sunwoodai.com)までお気軽にお問い合わせください。

MOA で AWS の魔法を探検してみてください！✨