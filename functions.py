from mysql.connector.errors import IntegrityError
import mysql.connector
import random
import requests


def cambio_hoje(moeda, base):
    # Defina os cabeçalhos personalizados
    headers = {
        'apikey': 'AAk1TgCXVEbtBP65GvJz1SOoQJNtoA9R'
    }
    # URL da API de conversão de moeda (exchangerate-api.com)
    url = f'https://api.apilayer.com/exchangerates_data/latest?symbols={moeda}&base={base}'
    # Faça a solicitação HTTP com os cabeçalhos personalizados
    response = requests.get(url, headers=headers)
    return response

def convert_cambio(de, para, qtd):
    # Defina os cabeçalhos personalizados
    headers = {
        'apikey': 'AAk1TgCXVEbtBP65GvJz1SOoQJNtoA9R'
    }
    # URL da API de conversão de moeda (exchangerate-api.com)
    url = f'https://api.apilayer.com/exchangerates_data/convert?to={para}&from={de}&amount={qtd}'
    # Faça a solicitação HTTP com os cabeçalhos personalizados
    response = requests.get(url, headers=headers)
    return response

def create_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1?2A6k6=",
        database="db_pi"
    )
    return conn

def efetiva_compra():
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
        except IntegrityError as err:
                print("Erro:", err)
        except mysql.connector.Error as err:
            print("Erro:", err)
        finally:
            cursor.close()
            conn.close()

def valida_idcatalogo(id):
     #return bool
     #validade se o id passado como parametro for verdadeiro
    print(id)
    return random.choice([True, False])

def get_catalogo():
     #list_catalogo = [[id_pacote, cidade, pais, valor, descrição, data_ini, data_fim]]
     list_catalogo = [[1, "São Paulo", "Brasil", 300.00, "Descrição aqui", "05/09/2023", "07/09/2023"],[2, "Paris", "França", 7000.00, "Descrição aqui", "05/09/2023", "25/09/2023"],[3, "Madrid", "Espanha", 5500.00, "Descrição aqui", "12/09/2023", "27/09/2023"]]
     return list_catalogo