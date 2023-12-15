from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html')
  #return "Hello World!"

def main():
  app.run(debug=True)