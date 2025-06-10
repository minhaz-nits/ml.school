from metaflow import FlowSpec, step
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Set your OpenAI key securely in environment or secrets manager


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class LLMFlow(FlowSpec):

    @step
    def start(self):
        self.prompt = "give me a python dictionary with random student names and scores. Donot give me a code . I just want the dictionary nothing else"
        self.next(self.query_llm)

    @step
    def query_llm(self):
        response = client.chat.completions.create(
        model="gpt-4",
        messages=[
        {"role": "user", "content": self.prompt}
        ]
        )

        print(response.choices[0].message.content)
        self.summary = response.choices[0].message.content
        self.next(self.end)

    @step
    def end(self):
        print("LLM Output:", self.summary)

if __name__ == '__main__':
    LLMFlow()