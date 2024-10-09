import openai # openai v1.0.0+
client = openai.OpenAI(api_key="sk-tdjdCTqaFOp4IuPMOPvDSg",base_url="http://localhost:4000") # set proxy to base_url
# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="bedrock/claude-3-haiku", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])

print(response)
