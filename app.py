from flask import Flask, render_template, request, redirect, url_for
from functions import *
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/catalogo', methods=['GET'])
def catalogo():
    if request.method == 'GET':
        list_catalogo = [[1,'Brasil', 'Rio de Janeiro', 500.00, 'Pacote de férias para praia', '2023-11-01', '2023-11-15'],#
                        [2,'Estados Unidos', 'Nova Iorque', 800.00, 'Pacote de aventura nas montanhas', '2023-10-20','2023-10-30'],#
                        [3,'França', 'Paris', 350.00, 'Pacote cultural na cidade', '2023-12-05','2023-12-20'],#
                        [4,'Reino Unido', 'Londres', 700.00, 'Pacote de esportes aquáticos', '2023-11-15','2023-11-30'],
                        [5,'Italia','Roma', 900.00, 'Pacote de lua de mel', '2023-10-25','2023-11-05'],
                        [6,'Espanha', 'Madrid', 600.00, 'Pacote de relaxamento na floresta', '2023-11-10','2023-11-28'],
                        [7,'Australia', 'Sydney', 450.00, 'Pacote gastronômico na cidade', '2023-12-15','2023-12-30'],
                        [8,'Alemanha', 'Berlim', 550.00, 'Pacote de ecoturismo', '2023-10-15', '2023-10-25'],
                        [9,'Canada', 'Toronto', 750.00, 'Pacote de esqui nas montanhas', '2023-12-01','2023-12-15'],
                        [10,'Japão', 'Tóquio', 400.00, 'Pacote de turismo histórico', '2023-11-05', '2023-11-20']]
                       
                        #ID, PAIS, CIDADE, PREÇO POR CABEÇA, DESCRIÇÃO BREVE, IDA E VOLTA
        return render_template('catalogo.html', list_catalogo=list_catalogo)

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
            id = request.args.get('id')
            if valida_idcatalogo(id):
                info_pacote = get_package_and_destination_by_id(id)
                print(info_pacote)
                if info_pacote:
                    return render_template('efetiva_compra.html', info_pacote=info_pacote)
                else:
                    return "Erro"
            else:
                return "Erro"
                
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
  
@app.route('/conversor')
def conversor():
        return render_template('conversor_de_moedas.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)