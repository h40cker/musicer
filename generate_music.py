import openai

def generate_music_description(prompt: str) -> str:
    """
    使用OpenAI API生成音乐描述（可以是旋律、和弦进行等）
    :param prompt: 用户输入的提示，描述生成音乐的风格或者内容
    :return: AI生成的音乐描述
    """
    response = openai.Completion.create(
        engine="text-davinci-003",  # 选择合适的模型
        prompt=prompt,
        max_tokens=150,            # 可以调整生成的长度
        temperature=0.7,           # 控制生成的创意度
        n=1
    )
    music_description = response.choices[0].text.strip()
    return music_description
