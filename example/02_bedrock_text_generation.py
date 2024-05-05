import boto3
import json

# Bedrockクライアントを初期化する関数
def initialize_bedrock_client(region="us-west-2"):
    """
    指定されたリージョンでBedrockクライアントを初期化します。
    指定可能なリージョンはバージニア北部（us-east-1）またはオレゴン（us-west-2）です。
    デフォルトリージョンで良い場合はリージョン指定省略可能です。
    """
    return boto3.client('bedrock-runtime', region_name=region)

# Bedrockモデルにリクエストを送信する関数
def send_request_to_bedrock(client, model_id, message, max_tokens=1000):
    """
    指定されたBedrockモデルにリクエストを送信し、応答を返します。
    """
    body = json.dumps(
        {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ]
        }
    )
    accept = 'application/json'
    content_type = 'application/json'
    response = client.invoke_model(body=body, modelId=model_id, accept=accept, contentType=content_type)
    response_body = json.loads(response.get('body').read())
    return response_body["content"][0]["text"]

# メインの処理
def main():
    # Bedrockクライアントを初期化
    bedrock_client = initialize_bedrock_client()
    
    # 使用するモデルIDを指定
    model_id = 'anthropic.claude-3-haiku-20240307-v1:0'
    
    # モデルに送信するメッセージ
    message = "味噌汁の作り方を説明してください"
    
    # Bedrockモデルにリクエストを送信し、応答を取得
    answer = send_request_to_bedrock(bedrock_client, model_id, message)
    
    # 応答を表示
    print(answer)

if __name__ == "__main__":
    main()