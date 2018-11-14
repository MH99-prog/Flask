from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<action>')
def index(action):
    args={}
    args['param'] = 'Noman'
    args['action'] = action
    return render_template('user.html' , args = args)


if __name__ == '__main__':
    app.run(debug=True ,port = '7080')

