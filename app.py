from flask import Flask, render_template, request
import marks as m

app = Flask(__name__)

@app.route("/")
def welcome_page():
    return render_template("file1.html")

@app.route("/file2", methods=['POST'])
def second_page():
    html_data = request.form["enter_value"]
    marks_pred = m.marks_prediction(html_data)
    mk = marks_pred
    return render_template("file2.html", html_data=mk)
# request form from id in html file

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)