from flask import Flask, render_template 
app = Flask(__name__) 

@app.route('/')
def index():
    return  render_template('index.html', num_rows=8, num_cols=8)

@app.route('/<int:x>')
def sized_checkboard(x):
     return render_template('index.html', num_rows=int(x), num_cols=int(x))

@app.route('/<int:x>/<int:y>')
def sized_checkboard_two_dimensions(x,y):
     return render_template('index.html', num_rows=int(x), num_cols=int(y))

@app.route('/<int:x>/<int:y>/<c1>/<c2>')
def sized_checkboard_two_dimensions_and_color(x, y, c1, c2):
     return render_template('index.html', num_rows=int(x), num_cols=int(y), color_one=c1, color_two=c2)

if __name__=="__main__":
      app.run(debug=True)