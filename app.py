from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/catalogo', methods=['GET', 'POST'])
def catalogo():
    if request.method == 'GET':
        list_catalogo = get_catalogo()
        return render_template('catalogo.html', list_catalogo=list_catalogo)
    if request.method == 'POST':
        #pegar o id do catalogo e passar como parametro para função valida_idcatalogo(id)
        id = 999
        if valida_idcatalogo(id):
            return render_template('efetiva_compra.html')
        else:
            return "Id invalido"

@app.route('/efetiva_compra', methods=['GET', 'POST'])
def efetiva_compra():
        if request.method == 'GET':
            #O usuário será redirecionado ao catalogo se tentar acessar essa pagina sem ser direcionado pelo catalogo
            return render_template('catalogo.html')
        if request.method == 'POST':
            return "Compra efetivada com sucesso!"
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)