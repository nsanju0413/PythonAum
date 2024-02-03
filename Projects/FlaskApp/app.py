from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    if request.method == 'POST':
        user_name = request.form['user_name']
        return render_template('greet.html', user_name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
