# Examples

このディレクトリには、MOA プロジェクトの使用例を示すサンプルスクリプトが含まれています。

## 01_list_bedrock_models.py

このスクリプトは、AWS Bedrock で利用可能なファウンデーションモデルの一覧を取得して表示します。主な手順は以下の通りです。

1. Bedrock クライアントを作成
2. `list_foundation_models()` メソッドを使用してファウンデーションモデルの一覧を取得
3. 取得したファウンデーションモデルの一覧を表示

## 02_bedrock_text_generation.py

このスクリプトは、AWS Bedrock のモデルを使用してテキスト生成を行う方法を示しています。主な手順は以下の通りです。

1. Bedrock クライアントを初期化
2. 使用するモデル ID を指定
3. モデルに送信するメッセージを設定
4. `invoke_model()` メソッドを使用してモデルにリクエストを送信し、応答を取得
5. 取得した応答を表示

## 03_litellm_claude.py

このスクリプトは、LiteLLM を使用して Claude AI とチャットする方法を示しています。主な手順は以下の通りです。

1. LiteLLM の `completion` メソッドを使用
2. Claude-3-haiku-20240307 モデルを指定
3. ユーザーメッセージを送信し、応答を出力

## 04_aws_claude_chatbot.py

このスクリプトは、AWS Claude AI を使用したチャットボットの例を示しています。主な手順は以下の通りです。

1. `chat_with_aws_claude` 関数を定義し、Claude AI とのチャットを実装
2. anthropic.claude-3-haiku-20240307-v1:0 モデルを使用
3. ユーザーメッセージを送信し、応答を出力
4. LiteLLM のデバッグ情報を表示するオプションを追加

## 05_gemini_chat.py

このスクリプトは、Gemini API を使用したチャットの例を示しています。主な手順は以下の通りです。

1. LiteLLM の `completion` メソッドを使用
2. gemini/gemini-pro モデルを指定
3. ユーザーメッセージを送信し、応答を出力

これらのスクリプトを参考に、AWS Bedrock や他のサービスの機能を活用したアプリケーションを開発できます。各スクリプトには、使用例とステップバイステップの説明が含まれています。