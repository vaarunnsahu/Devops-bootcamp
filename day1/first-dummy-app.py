from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_docker():
    return '<h1> This is Varun Sahu</h1><br><p>https://www.linkedin.com/in/vaarunsahu/, follow for more content around Devops.</p> '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')