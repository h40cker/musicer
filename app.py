from flask import Flask, render_template, request, jsonify
from generate_music import generate_music_description

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_music', methods=['POST'])
def generate_music():
    user_prompt = request.form['prompt']
    music_description = generate_music_description(user_prompt)
    # 这里可以添加生成音频文件的逻辑，暂时返回文本描述
    return jsonify({"music_description": music_description})

if __name__ == "__main__":
    app.run(debug=True)
