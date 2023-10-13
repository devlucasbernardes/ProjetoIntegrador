from flask import Flask, render_template, request, jsonify
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
            info_pacote = ["País", "Cidade", "Descrição da viagem", "Data incio", "Data fim", "1000"]
            #O usuário será redirecionado ao catalogo se tentar acessar essa pagina sem ser direcionado pelo catalogo
            return render_template('efetiva_compra.html',info_pacote=info_pacote)
        if request.method == 'POST':
            # Obter a hora atual no servidor
            import datetime
            hora_recebimento = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            nome = request.form['nome']
            valor = request.form['valor_oculto']
            # Faça o que quiser com o nome e a hora de recebimento
            print("Nome recebido:", nome)
            print("Hora de recebimento:", hora_recebimento)
            # Retorne uma resposta ou redirecione o usuário
            return f"Nome recebido: {nome}, Valor: {valor}, Hora de recebimento: {hora_recebimento}"

@app.route('/cambio')
def taxas_de_cambio():

    #data = convert_cambio('USD','BRL', 1)
    data = cambio_hoje('BRL', 'USD')
    # Verifique se a solicitação foi bem-sucedida
    if data.status_code == 200:
        result = data.text
        return result
    else:
        return jsonify({'error': 'Falha na solicitação'}), data.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5000)