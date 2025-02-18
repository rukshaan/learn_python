from flask import Flask,request,render_template

app=Flask(__name__,template_folder='templates')
@app.route('/')
def index():
    myList=[10,20,30,40,50]
    return render_template('index.html',myList=myList)
@app.route('/other')
def other():
    address="Mathagal"
    return render_template('other.html',address=address)


@app.template_filter('reverse_string')
def reverse_string(s):
    
    return s[::-1]
@app.template_filter('repeat')
def repeat(s,times=3):
    return s*times



@app.route('/hello',methods=['GET','POST','PUT'])
def hello():
    return "<h1>Hello World!!!</h1>"   
      



@app.route("/greet/<name>")
def greet(name):
    return f"<h1>Hello {name}!!!</h1>"

@app.route("/math/<int:num1>/<int:num2>")
def add(num1,num2):
    return f"{num1}+{num2} = {num1+num2}"


@app.route("/handle_url_params")
def handle_url_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting=request.args['greeting']
        name=request.args['name']
        return f"{greeting},{name}"
    return "Some parameters are missing!!!"

if __name__ =='__main__':
    app.run(debug=True)