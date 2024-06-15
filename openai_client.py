import openai
from openai import AzureOpenAI
from config import Config
import prompt
# from utils.helpers import load_json_config

class OpenAIClient:
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=Config.openai_api_base,
            api_key=Config.openai_api_key,
            api_version=Config.openai_api_version
        )

    def generate_completion(self, prompt):
        """Returns the generated text answer from ChatGPT OpenAI API."""
        completion = self.client.chat.completions.create(
            model=Config.openai_deployment_name,
            temperature=0.7,
            max_tokens=497,
            messages=[
            # {"role": "system", "content": "You are a helpful assistant. Summarize the following text in 60 words or less."},
            {"role": "user", "content": prompt}
            ]
        )
        generated_text = completion.choices[0].message.content.strip()
        return generated_text
    
    def generate_prompt(self, text, criteria):
        custom_prompt = prompt.prompt[criteria]
        return custom_prompt + text