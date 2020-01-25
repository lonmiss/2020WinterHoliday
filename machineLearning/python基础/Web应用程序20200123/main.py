from flask import Flask

app=Flask(__name__)  #创建flask对象的app

@app.route("/")
@app.route("/hello")
def hello():
    return "hello world! 这是一个文本程序"

if __name__=="__main__":
    app.run()