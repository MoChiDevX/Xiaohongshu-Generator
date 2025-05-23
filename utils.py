from prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from xiaohongshu_model import Xiaohongshu
# import os

def generate_xiaohongshu(theme,openai_api_key,base_url = "https://api.openai.com/v1"):
    prompt = ChatPromptTemplate.from_messages([
        ('system', system_template_text),
        ('user', user_template_text)
    ])

    model = ChatOpenAI(model = 'gpt-3.5-turbo', api_key = openai_api_key, base_url = base_url)
    output_parser = PydanticOutputParser(pydantic_object = Xiaohongshu)

    chain = prompt | model | output_parser
    result = chain.invoke({
        'parser_instructions':output_parser.get_format_instructions(),
        'theme':theme
    })
    return result

# print(generate_xiaohongshu('ai绘画',os.getenv('OPEN_API_KEY')))