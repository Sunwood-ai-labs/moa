from litellm import completion

response = completion(
    # model="ollama/llm-jp-13b-v2", 
    model="bedrock/claude-3-haiku", 
    messages=[{ "content": "20語で答えてください。あなたは誰ですか？","role": "user"}], 
    # api_base="http://host.docker.internal:11434"
    # api_base="http://localhost:11434"
    api_base="http://localhost:4000"
)
print(response)
