# -*- encoding:utf-8 -/-
from flask import Flask, request
import flask

app=Flask(__name__)  #创建flask对象的app

@app.route("/",methods=['GET'])

def hello():
    n1=int(request.form["n1"])
    n2=int(request.form["n2"])
    n3=n1+n2
    return """
        <!Doctype html>
        <html>
            <body>
                <h2>输入两个数求和</h2>
                <from method="post" action="/add">
                    <table>
                        <p>使用表单计算两个数的和</p>
                        <tr><td>被加数</td><td><input type="text" name="n1" /></td></tr>
                        <tr><td>加数</td><td><input type="text" name="n2" /></td></tr>
                        <tr><td>和</td><td><input type="text" name="n3" value='''+str(n1)+'''/></td></tr>
                    </table> 
                    <button name="sum" type="submit" value="sum">求和</button>
                </from>
            </body>    
        </html>
    """
if __name__=="__main__":
    app.run()