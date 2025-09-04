from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    
    return render_template("index.html")

@app.route('/saluda')
def saluda():
    return "<marquee><h1>Hola clase</h1></marquee"


if __name__ == '__main__':
    app.run(debug=True)
    