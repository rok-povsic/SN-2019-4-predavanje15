from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def prva_stran():
    return render_template("prva-stran.html")


@app.route("/smreka")
def smreka():
    html = ""
    for i in range(20):
        html = html + "&nbsp;" * (20 - int(i/1.5)) + "*" * (i + 1) + "<br>\n"
    return html


@app.route("/o-meni")
def o_meni():
    return render_template("o-meni.html")


if __name__ == '__main__':
    app.run()
