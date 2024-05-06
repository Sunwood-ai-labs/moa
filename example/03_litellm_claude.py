import os
from litellm import completion
from art import *

# スクリプト名を取得して出力
script_name = os.path.basename(__file__)
tprint(script_name)

messages = [{"role": "user", "content": "Hey! how's it going?"}]
response = completion(model="claude-3-haiku-20240307", messages=messages)
print(response)