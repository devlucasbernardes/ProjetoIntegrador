from flask import Flask, render_template, request, jsonify, redirect
from functions import *
from datetime import datetime


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

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        fullname = request.form['DC_FULLNAME']
        birthdate = request.form['DT_BIRTHDATE']
        birthdate = datetime.strptime(birthdate, "%d/%m/%Y").strftime("%Y-%m-%d")
        document = request.form['DC_DOCUMENT']
        email = request.form['DC_MAIL']
        phone = request.form['DC_PHONE']
        
        conn = create_conn()
        cursor = conn.cursor()
        
        try:
            sql_query = "INSERT INTO TB_CLIENTS (DC_FULLNAME, DT_BIRTHDATE, DC_DOCUMENT, DC_MAIL, DC_PHONE) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_query, (fullname, birthdate, document, email, phone))
            conn.commit()
            msg = "Usuário cadastrado com sucesso!"
        except IntegrityError as err:
            if 'DC_DOCUMENT' in str(err):
                msg = "CPF já cadastrado."
            elif 'DC_MAIL' in str(err):
                msg = "E-mail já cadastrado."
            else:
                msg = "Erro ao cadastrar usuário."
        except mysql.connector.Error as err:
            print("Erro ao inserir usuário:", err)
            msg = "Erro ao cadastrar usuário."
            raise
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('cadastro', msg=msg))
    
    else:
        msg = request.args.get('msg')
        return render_template('cadastro.html', msg=msg)     

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
    
@app.route('/conversor')
def conversor():
        return render_template('conversor_de_moedas.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)