from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/fruits/<id>')         
def fruits(id):
    print(id)
    print(request.args['actor']) # Query Parameter
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    