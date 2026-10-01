from flask import Flask,render_template,request,redirect,url_for


app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello i am Iram khan</h1>"

@app.route('/welcome')
def welcome():
    return "<h1>Welcome to flask</h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:a>')
def success(a):
    return "the person is pass and the score is" + str(a)

@app.route('/failed/<int:a>')
def failed(a):
    return "Adnan is failed and score is " + str(a)

@app.route('/calculate', methods=['POST','GET'])
def calculate():

    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        print(request.form)

        maths = float(request.form['ms'])
        science = float(request.form['science'])
        english = float(request.form['english'])

        avg = (maths + science + english) / 3

        result = ""

        if avg >= 80:
            result = "success"
        else:
            result = "failed"

        return redirect(url_for(result, a=int(avg)))

    
if __name__=='__main__':
    app.run(debug=True)