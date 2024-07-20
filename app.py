from flask import Flask, render_template, request, jsonify, session
from anthropic import AnthropicVertex
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 为session设置一个密钥

PROJECT_ID = os.getenv('PROJECT_ID')
LOCATION = os.getenv('LOCATION')

client = AnthropicVertex(region=LOCATION, project_id=PROJECT_ID)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # 从session中获取对话历史，如果没有则初始化
    conversation = session.get('conversation', [])
    
    # 添加用户消息到对话历史
    conversation.append({"role": "user", "content": user_message})
    
    try:
        response = client.messages.create(
            max_tokens=2000000,  # 增加 token 数量
            messages=conversation,
            model="claude-3-5-sonnet@20240620",
        )
        
        # 提取文本内容
        response_text = response.content[0].text if response.content else "No response"
        
        # 添加助手回复到对话历史
        conversation.append({"role": "assistant", "content": response_text})
        
        # 更新session中的对话历史
        session['conversation'] = conversation
        
        return jsonify({'response': response_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/new_chat', methods=['POST'])
def new_chat():
    # 清除session中的对话历史
    session.pop('conversation', None)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=14514)
