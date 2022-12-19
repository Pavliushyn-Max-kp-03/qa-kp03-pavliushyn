from flask import Flask

app = Flask(__name__)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World1'
    a = response.status_code
    print(a)


if __name__ == '__main__':
    app.run(debug=True)