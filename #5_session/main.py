from flask import Flask,render_template,redirect,url_for,request,session
from datetime import timedelta

app = Flask(__name__)
app.secret_key="rukshan"
app.permanent_session_lifetime=timedelta(days=2)
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/test")
def test():
    return render_template('new.html')

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method =='POST':
        user=request.form["nm"]
        session.permanent=True
        session["user"]=user
        return redirect(url_for("user",user=user))
    else :
        return  render_template('login.html')
    
@app.route("/logout")
def logout():
    session.pop("user", None)  
    return redirect(url_for("login"))

@app.route("/user/<user>")
def user (user):
    if "user" in session:
        session_user=session["user"]
        return render_template('user.html',user=user)
    else:
        return redirect(url_for("login"))
if __name__ == '__main__':
    app.run(debug=True)