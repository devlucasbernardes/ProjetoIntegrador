from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem-vindo à agência de viagens!'

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)