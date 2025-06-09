from metaflow import FlowSpec, step
from openai import OpenAI

client = OpenAI(api_key="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")



# Set your OpenAI key securely in environment or secrets manager
# openai.api_key = "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"

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