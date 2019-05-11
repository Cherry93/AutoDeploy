from main import app


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    d = dict()
    a = d.get("1")
    print a is None
    app.run(threaded=True)
