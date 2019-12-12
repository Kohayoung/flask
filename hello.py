from flask import Flask, escape, request, render_template
import random
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

@app.route('/lunch')
def lunch():
    
    #lunch = ['20층','김밥','자장면','부대찌개','돈까스']
    #lunch_image = ['http://cfile216.uf.daum.net/image/99B8464E5B3DAF2219F22E'
    #            ,'http://recipe1.ezmember.co.kr/cache/recipe/2016/11/28/6bc7f3c7a3fdf517e6943dd14a9b3df01.jpg'
    #            ,'https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F236F694453AA52A70D'
    #            ,'http://foodyap.co.kr/shopimages/goldplate1/049001000008.jpg?1561711447'
    #            ,'https://imagescdn.gettyimagesbank.com/500/201811/a11240496.jpg']
    #index = random.randrange(0,len(lunch))
    #return render_template('lunch.html', food= lunch[index], food_image = lunch_image[index])

    menus = {
        "20층":"http://cfile216.uf.daum.net/image/99B8464E5B3DAF2219F22E"
        ,"김밥":"http://recipe1.ezmember.co.kr/cache/recipe/2016/11/28/6bc7f3c7a3fdf517e6943dd14a9b3df01.jpg"
        ,"자장면":"https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F236F694453AA52A70D"
        ,"부대찌개":"http://foodyap.co.kr/shopimages/goldplate1/049001000008.jpg?1561711447"
        ,"돈까스":"https://imagescdn.gettyimagesbank.com/500/201811/a11240496.jpg"
        }

    menu_list = list(menus.keys())
    pick = random.choice(menu_list)
    img =menus[pick]
    print(menu_list)

    return render_template('lunch.html', food=pick, food_image=img)

@app.route('/movies')
def movies():
    movies = ['겨울왕국2', '굿라이어', '주만지']
    return render_template('movies.html', movies = movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong', methods=['GET','POST'])
def pong():
    #print(request.form.get('keyword'))
    keyword =request.form.get('keyword') #post방식 [ping.html - <form action="/pong" method="post">]
    #keyword =request.args.get('keyword') #get방식  [ping.html - <form action="/pong" method="ㅎㅈㅅ">]
    return render_template('pong.html',keyword=keyword)

@app.route('/naver', methods=['GET','POST'])
def naver():
   
    #keyword =request.form.get('keyword') #post방식 [ping.html - <form action="/pong" method="post">]
   
    return render_template('naver.html',keyword=keyword)

@app.route('/google')
def google():
   
    return render_template('google.html',keyword=keyword)

if __name__ =='__main__':
    app.run(debug = True)