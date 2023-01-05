from be import app

@app.route("/e")
def home1():
    return "Hello, Flask!!!!!!"