from flask import Flask, render_template

# flask 클래스를 인스턴스화한다
app = Flask(__name__)

# url과 실행할 함수를 매핑
@app.route('/', endpoint = 'endpoint-name')
def index():
    return 'Hello, Flaskbook! nice to meet ya'
# 엔드포인트를 지정하지 않으면 함수명이 엔드포인트
#@app.get('/hello') = @app.route('/hello', methods=['GET'])

# rule에 변수 지정
@app.route('/hello/<name>', # 컨버터 <name : string>
methods = ['GET', 'POST'],
endpoint = 'hello-endpoint')
def hello(name):
    return ('hello {}!'.format(name))

# show_name 엔드포인트 작성
@app.route('/name/<name>')
def show_name(name):
    # 변수를 템플릿 엔진에 건넨다
    return render_template('index.html', name=name)