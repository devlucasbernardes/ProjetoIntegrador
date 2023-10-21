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
        password="",
        database="db_pi2"
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

    try:
        # Conectar ao banco de dados
        conn = create_conn()

        # Criar um cursor
        cursor = conn.cursor()

        # Definir a consulta SQL para buscar todos os valores da tabela tb_package
        sql_query = "SELECT p.CD_ID AS PackageID, d.DC_COUNTRY AS DestinationCountry, d.DC_CITY AS DestinationCity, p.VL_VALUE AS PackageValue, p.DC_DESCRIPTION AS PackageDescription, p.DT_START_DATE AS StartDate, p.DT_END_DATE AS EndDate FROM tb_package AS p INNER JOIN tb_destiny AS d ON p.id_DESTINY = d.CD_ID;"

        # Executar a consulta
        cursor.execute(sql_query)

        # Recuperar todos os resultados
        resultados = cursor.fetchall()

        resultados_formatados = []


        # Função para formatar o valor como decimal
        def formatar_valor(valor):
            return '{:.2f}'.format(valor)  # Formata o valor com duas casas decimais

        # Função para formatar a data
        def formatar_data(data):
            # Formatar a data do formato "YYYY-MM-DD" para "DD/MM/YYYY"
            return data.strftime("%d/%m/%Y")

        # Iterar pelos resultados e imprimir
        for resultado in resultados:
            resultado_formatado = list(resultado)  # Converte a tupla para uma lista
            resultado_formatado[5] = formatar_data(resultado_formatado[5])
            resultado_formatado[6] = formatar_data(resultado_formatado[6])
            resultado_formatado[3] = formatar_valor(resultado_formatado[3])
            resultados_formatados.append(resultado_formatado)

        # Imprimir os resultados formatados
        #for resultado in resultados_formatados:
            #print(resultado)
        return resultados_formatados
    
    except mysql.connector.Error as err:
        print("Erro:", err)

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conn.close()