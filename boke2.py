#coding=utf-8
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    return 'user_agent is %s' % user_agent



if __name__ == '__main__':
    app.run()