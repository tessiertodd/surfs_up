from flask import Flask
app = Flask(__name__)
@app.route('/')
def ski_comment():
    return 'Cannot wait to ski!!'