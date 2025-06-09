from metaflow import FlowSpec, step
from openai import OpenAI
import ast

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

        
        self.student_dict = ast.literal_eval(self.summary)
        self.key=list(self.student_dict)
        #self.next(self.end)
        self.next(self.capitalize, foreach="key")

    @step
    def capitalize(self):
        """Capitalize the input name."""
        name = self.input or ""
        value = self.student_dict[name]
        print(name)
        self.person = name.capitalize()
        self.marks=value+10
        print(f'Turned "{name}" into "{self.person}" and "{self.marks}"')

        self.next(self.join)

    @step
    def join(self, inputs):
        """Join the results of the foreach."""
        ''' self.people = [i.person for i in inputs]'''
        self.results = {inp.person: inp.marks for inp in inputs}
        self.next(self.end)

    @step
    def end(self):
        print("LLM Output:", self.results)

if __name__ == '__main__':
    LLMFlow()