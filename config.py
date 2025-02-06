import openai
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 从环境变量中获取 OpenAI API 密钥
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 配置 OpenAI API 密钥
openai.api_key = OPENAI_API_KEY
