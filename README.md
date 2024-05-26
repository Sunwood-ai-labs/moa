
<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/moa_icon.jpeg" width="100%">
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


以下は修正・添削後のREADME文書です。誤字の修正、言い回しの最適化、そして技術用語の統一を行いました。

---

## 🌟 はじめに

MOA (Magic of AWS) は、AWSの基盤技術を活用し、Dockerを通じて企業がクラウド環境でLLM（Large Language Models）を簡単に利用できるようにするプロジェクトです。AWS CLIがプリインストールされた独立した開発環境を提供することで、企業が高度なセキュリティとプライバシーを保ちつつ、AI技術を効果的に活用できるよう支援します。MOAを使用することで、ユーザーはローカルマシンの設定を変更せずに、セキュアな環境から直接AWSリソースを管理し、先進的なAI機能を実装できます。

主な特徴:
- AWS BedrockやAWS Cloud AIなどの最新AIサービスを手軽に試すことができます。
- LiteLLMプロジェクトを利用して、多様なLLMモデルを統一的なインターフェースで活用できます。
- Ollama WebUIを使い、独自のLLMモデルをチャットボットとして動作させることができます。

## 🚀 始め方

### 前提条件

始める前に、以下のものがマシンにインストールされていることを確認してください。

- Docker
- Docker Compose
- Visual Studio Code（オプションですが、より良い開発体験のために推奨します）

### インストール

1. リポジトリをクローンします。
```bash
git clone https://github.com/Sunwood-ai-labs/MOA.git
```

2. プロジェクトディレクトリに移動します。
```bash
cd MOA
```

3. プロジェクトルートに`.env`ファイルを作成し、AWSアクセスキーID、シークレットアクセスキー、その他の設定を追加します。
```plaintext
AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY
AWS_REGION_NAME=your-preferred-region
AWS_DEFAULT_REGION=your-preferred-region
AWS_DEFAULT_OUTPUT=json

# ANTHROPIC_API_KEY=sk-ant-XXXXX

OLLAMA_BASE_URL=http://ollama:11434
WEBUI_SECRET_KEY=sk-1234
LITELLM_PROXY_HOST=0.0.0.0
OPEN_WEBUI_PORT=8080
```

>[!IMPORTANT]
>`.env.example`ファイルに新しい環境変数 `OLLAMA_BASE_URL`, `WEBUI_SECRET_KEY`, `LITELLM_PROXY_HOST`, `OPEN_WEBUI_PORT` が追加されました。APIキーの設定も更新されています。
>
>機密性の高い AWS 認証情報を誤ってコミットしないように、必ず`.env`ファイルを`.gitignore`に追加してください。

### 使い方

#### ollama webui

1. Visual Studio Codeでプロジェクトを開きます。

2. VS Codeのターミナルを開き、以下のコマンドを実行してDockerコンテナをビルドし、起動します。
    ```bash
    # Ollama WebUI を追加で起動
    docker-compose -f docker-compose.ollama.yml up
    ```

- ollama: LLMモデルを提供するメインのサービス。GPU利用の設定も可能。
- open-webui: ollama WebUIを提供するサービス。デフォルトでポート8080をリッスン。
- litellm: 各種LLMモデルへのアクセスを提供するサービス。

#### ollama webui + langfuse の起動方法

1. 必要な環境変数を`.env`ファイルに設定します。`LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`が必要です。
   ```plaintext
   LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
   LANGFUSE_SECRET_KEY=your_langfuse_secret_key
   ```

2. 以下のコマンドを使用して、ollama webuiとlangfuseを含むすべての関連サービスを起動します。
   ```bash
   docker-compose -f docker-compose.ollama.yml -f langfuse/docker-compose.yml up
   ```

   このコマンドにより、ollamaとlangfuse関連のサービスが一緒に起動されます。`langfuse`は`http://localhost:3000`でアクセス可能です。

#### Dify の起動方法

1. Dify関連のサービスを起動するには、次のコマンドを実行します。
   ```bash
   docker-compose -f spellbook/dify/docker/docker-compose.yaml up
   ```

   このコマンドは、`spellbook`ディレクトリ内の`dify`サブディレクトリにあるDocker Compose設定ファイルを使用して、Difyサービスを起動します。

## 📚 サンプルスクリプト

AWS Bedrock や Claude AI、LiteLLM、Gemini APIなどの使用例を示すサンプルスクリプトが `example` ディレクトリに含まれています。詳細については、[example/README.md](example/README.md) を参照してください。 

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
├── docker-compose.ollama.yml # ollama と webui の Docker Compose 設定
├── example/              # サンプルスクリプトディレクトリ  
│   ├── 01_list_bedrock_models.py       # Bedrock モデルの一覧を取得するサンプル
│   ├── 02_bedrock_text_generation.py   # Bedrock を使用したテキスト生成のサンプル 
│   ├── 03_litellm_claude.py            # LiteLLM と Claude AI を使用したチャットのサンプル
│   ├── 04_aws_claude_chatbot.py        # AWS Claude AI を使用したチャットボットのサンプル
│   ├── 05_gemini_chat.py               # Gemini API を使用したチャットのサンプル
│   ├── 06_langfuse_openai_chat_completion.py # Langfuse と OpenAI API を使用したチャットのサンプル  
│   └── README.md         # サンプルスクリプトの説明
├── litellm/              # LiteLLM 設定ディレクトリ
│   └── config.yaml       # LiteLLM 設定ファイル  
├── requirements.txt      # 必要な Python パッケージのリスト
├── script/               # 便利なスクリプトファイル
│   └── activate-moa_dev.bat  # moa_dev 仮想環境をアクティベートするスクリプト
└── docs/                 # ドキュメントファイル
    ├── moa_icon.jpeg     # プロジェクトアイコン
    └── page_front.md     # フロントページのドキュメント
```

## 📝 更新情報

リリースノートについては、[GitHub リリース](https://github.com/Sunwood-ai-labs/MOA/releases)ページを参照してください。

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
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [AWS Claude AI](https://aws.amazon.com/chatbot/claude/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)  
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)  
- [LiteLLM](https://github.com/Lightning-AI/lit-llama)
- [Langfuse](https://github.com/Sunwood-ai-labs/langfuse)
- [OLLaMa WebUI](https://github.com/Sunwood-ai-labs/ollama-webui)
- [Gemini API](https://www.gemini.com/developers)
- [Anthropic API](https://www.anthropic.com/)

## 📧 お問い合わせ

ご質問、ご提案、フィードバックがある場合は、[support@sunwoodai.com](mailto:support@sunwoodai.com)までお気軽にお問い合わせください。  

MOA で AWS と AI の魔法を探検してみてください！✨
