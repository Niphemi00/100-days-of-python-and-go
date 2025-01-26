from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')



@app.route('/create', methods=['POST', 'GET'])
def signup():
    return render_template('signup.html')



if __name__ == '__main__':
    app.run(debug=True)
python3 -m venv venv
