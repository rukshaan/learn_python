from flask import Flask,request

app=Flask(__name__)
@app.route('/')
def index():
    return "<h1>Hello World</h1>"

# @app.route('/hello')
# def hello():
#     name="Rukshan"
#     return f"<h1>Hello {name}!!!</h1>"
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