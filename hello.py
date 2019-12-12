from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    return 'hi'


@app.route('/hayoung')
def hayoung():
    return 'hayoung~'

@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요</h1>'

@app.route('/html_file')
def html_file():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug = True)