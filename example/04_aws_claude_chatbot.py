import os
from litellm import completion
import litellm
from art import *
# LiteLLMのデバッグ情報を表示する
litellm.set_verbose = True

def chat_with_aws_claude(message, model):
    """
    Claude AIモデルとチャットを行う関数

    Args:
        message (str): ユーザーからのメッセージ
        model (str): 使用するモデルの名前 (デフォルト: anthropic.claude-3-haiku-20240307-v1:0)

    Returns:
        str: Claude AIモデルからの応答
    """
    response = completion(
        model=model,
        messages=[{"content": message, "role": "user"}]
    )
    return response

if __name__ == "__main__":
    """
    メインの実行関数
    """
    
    # スクリプト名を取得して出力
    script_name = os.path.basename(__file__)
    tprint(script_name)
    
    # モデルとメッセージの設定
    MODEL = "anthropic.claude-3-haiku-20240307-v1:0"
    DEFAULT_MESSAGE = "Hello, how are you?"
    
    user_message = DEFAULT_MESSAGE
    claude_response = chat_with_aws_claude(user_message, MODEL)
    print(claude_response)