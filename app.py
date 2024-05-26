from flask import Flask,render_template,request,redirect
import check_password as ck

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/submit',methods=['POST'])
def submit():
    password = (request.form.get("password"))
    cnt = ck.main(password)
    if(cnt):
        res = f"{password} is found {cnt} times!! You should change it."
    else:
        res = f"{password} not found! You are good to go."
    return render_template("test.html", res=res)

if __name__ == "__main__":
    app.run()