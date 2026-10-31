from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "StreamYard Guest Bot Ready - Link: https://streamyard.com/hjtifd896z"

@app.route('/join')
def join():
    return "Bot will join StreamYard link"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
