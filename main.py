from flask import Flask, render_template, request, redirect, url_for, Response
from src.services import allservices
import validators

app = Flask(__name__)


@app.route("/", methods=["GET"])
def check_status():
    name = ""
    return render_template("index.html", name=name)


# @app.route("/int/<int:val>", methods=["GET"])
# def int_val(val):
#     return "{}".format(val)
#
#
# @app.route("/float/<float:val>", methods=["GET"])
# def float_val(val):
#     return "{}".format(val)

@app.route("/scrape", methods=["GET", "POST"])
def extract_keywords_from_website():
    url = None
    if request.method == "POST":
        url = request.form['url']
    else:
        url = request.args.get("url")
    if validators.url(url):
        keywords = allservices.extract_keywords_from_website(url)
        keywords = sorted(keywords, key=lambda l: l[0], reverse=True)[:40]
        return render_template("keywords_table.html", keywords=keywords, website=url)
    else:
        error = "Url({}) is not valid".format(url)
        return redirect(url_for("error_page", error=error))


@app.route("/error", methods=["GET", "POST"])
def error_page():
    error = request.args.get("error")
    return render_template("404.html", error=error)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8080)
    app.run(debug=True)
    # website = "https://saurabhy27.github.io"
    # print(extract_keywords_from_website(website))
