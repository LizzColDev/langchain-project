from fastapi import FastAPI
from langchain.llms import LlamaCpp, OpenAI
import config

api = config.OPEN_API_KEY

app = FastAPI()
print(api)
llm_openai = OpenAI(model_name = "text-davinci-003", openai_api_key=api)

answer_openai = llm_openai("Hi, How are you?")

print(answer_openai)
@app.get("/")
def read_root():
    return {"message": "Hello, World"}
