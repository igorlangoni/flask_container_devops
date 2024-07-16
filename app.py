from flask import Flask

app = Flask(__name__)

@app.route('/sebastien')
def lotr():
    return "<p>You SHALL not pass!</p>"

@app.route('/george')
def jerry_maguire():
    return "<p>Show me the money!</p>"

@app.route('/igor')
def godfather():
    return '<p>Look at what they did to my boy...</p>'

