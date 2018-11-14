from flask import Flask, render_template
app = Flask(__name__)
@app.route('/pakistan')
def Pakistan():
    return render_template('html_index.html ')


@app.route('/india')
def India():
    return render_template('html_index2.html')





if __name__ == '__main__':
    app.run(debug=True)