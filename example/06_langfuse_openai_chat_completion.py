import os
from art import tprint
from dotenv import load_dotenv
from langfuse.openai import auth_check, openai

def load_env_vars():
    load_dotenv()
    # Uncomment and set the following environment variables if needed
    # os.environ["LANGFUSE_PUBLIC_KEY"] = ""
    # os.environ["LANGFUSE_SECRET_KEY"] = ""
    # os.environ["OPENAI_API_KEY"] = ""
    # os.environ["LANGFUSE_HOST"] = "http://localhost:3000"

def print_script_name():
    script_name = os.path.basename(__file__)
    tprint(script_name)

def create_completion():
    completion = openai.chat.completions.create(
        name="test-chat",
        # model="gpt-4o",
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a very accurate calculator. You output only the result of the calculation."},
            {"role": "user", "content": "1 + 1 = "}],
        temperature=0,
        metadata={"someMetadataKey": "someValue"},
    )
    return completion

def main():
    load_env_vars()
    print_script_name()
    auth_check()
    completion = create_completion()
    print(completion)

if __name__ == "__main__":
    main()