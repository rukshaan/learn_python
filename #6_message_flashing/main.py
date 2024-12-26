from flask import Flask,render_template,redirect,url_for,request,session,flash
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
        flash("Login successful")
        return redirect(url_for("user",user=user))
    else :
        if "user" in session:
            flash("Already registered!!")
            return redirect(url_for("user",user=session["user"]))
        return  render_template('login.html')
    
@app.route("/logout")
def logout():
     if "user" in session:
        session_user=session["user"]
        flash("You have been log out . Try log in !!!","info")

        session.pop("user", None)  
        # flash("You have been Logged out!!","info")
        return redirect(url_for("login"))

@app.route("/user/<user>")
def user (user):
    if "user" in session:
        session_user=session["user"]
       
        # flash("You have been log out!!!","info")
        return render_template('user.html',user=user)
    else:
         flash("You are not logged in!!!")
    return redirect(url_for("login"))
if __name__ == '__main__':
    app.run(debug=True)