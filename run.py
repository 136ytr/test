from flask import Flask,render_template
app = Flask(__name__)

'''
@app.route('/')
def index():
    return 'Hello World!!'


@app.route('/')
def ran():
    return render_template("ran.html")
'''

@app.route('/')
def pdf():
    return render_template("pdf.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
