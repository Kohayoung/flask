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

@app.route('/variable')
def variable():
    name = "고하영이"
    return render_template('variable.html', html_name = name)

@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name = def_name)

@app.route('/cube/<int:num>/')
def calculate(num):
    def_num = num
    #def_cal_num = num*num*num
    def_cal_num = num**3
    return render_template('calculate.html', html_num = def_num, html_cal_num = def_cal_num)


if __name__ =='__main__':
    app.run(debug = True)