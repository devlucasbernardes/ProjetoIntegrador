from mysql.connector.errors import IntegrityError
import mysql.connector
import requests

from decimal import Decimal


def get_weather_forecast(city, country, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

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


# def create_conn():
#     conn = mysql.connector.connect(
#         host="db-infra-pi.database.windows.net",
#         user="admin_pi",
#         password="K!uuxhfh5EJzR7V",
#         database="projetoPI"
#     )
#     return conn
def create_conn():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="db_projetopi"
    )
    return conn
def efetiva_compra():
    return "Ok"

def valida_idcatalogo(id):
    try:
        # Conectar ao banco de dados
        conn = create_conn()

        # Criar um cursor
        cursor = conn.cursor()

        # Consulta SQL para verificar a existência do ID na tabela tb_package
        sql_query = "SELECT CD_ID FROM TB_PACKAGE WHERE CD_ID = %s"
        cursor.execute(sql_query, (id,))

        # Verificar se o ID existe
        resultado = cursor.fetchone()

        if resultado:
            return True  # O ID existe na tabela
        else:
            return False  # O ID não existe na tabela

    except mysql.connector.Error as err:
        print("Erro:", err)
        return False

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conn.close()

def get_catalogo():
    conn = None
    cursor = None
    try:
        conn = create_conn()
        cursor = conn.cursor()
        sql_query = """SELECT p.CD_ID AS PackageID, d.DC_COUNTRY AS DestinationCountry, d.DC_CITY AS DestinationCity,
                       p.VL_VALUE AS PackageValue, p.DC_DESCRIPTION AS PackageDescription, p.DT_START_DATE AS StartDate, 
                       p.DT_END_DATE AS EndDate FROM TB_PACKAGE AS p INNER JOIN TB_DESTINY AS d ON p.id_DESTINY = d.CD_ID;"""
        cursor.execute(sql_query)
        resultados = cursor.fetchall()
        print("Resultados obtidos:", resultados)  # Debug: Verifique os resultados obtidos
        return resultados

        resultados_formatados = []
        for resultado in resultados:
            resultado_formatado = list(resultado)
            resultado_formatado[5] = resultado_formatado[5].strftime("%d/%m/%Y")
            resultado_formatado[6] = resultado_formatado[6].strftime("%d/%m/%Y")
            resultado_formatado[3] = '{:.2f}'.format(resultado_formatado[3])
            resultados_formatados.append(resultado_formatado)

        return resultados_formatados

    except mysql.connector.Error as err:
        print("Erro ao acessar o banco de dados:", err)
        return []

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def format_decimal(value):
    # Formata o valor decimal com duas casas decimais
    return f'{value:.2f}'

def format_date(date):
    # Formata a data no formato "YYYY-MM-DD"
    return date.strftime('%d/%m/%y')

def get_package_and_destination_by_id(package_id):
    try:
        # Conectar ao banco de dados
        conn = create_conn()

        # Criar um cursor
        cursor = conn.cursor(dictionary=True)

        # Consulta SQL para recuperar informações do pacote e destino com base no ID do pacote
        query = """
        SELECT d.DC_COUNTRY AS Country, d.DC_CITY AS DestinationCity, 
               p.DC_DESCRIPTION AS DESCRIPTION, p.DT_START_DATE AS START_DATE, 
               p.DT_END_DATE AS END_DATE, p.VL_VALUE AS VALUE, p.CD_ID AS PackageID
        FROM tb_package AS p
        INNER JOIN tb_destiny AS d ON p.id_DESTINY = d.CD_ID
        WHERE p.CD_ID = %s
        """

        # Executar a consulta com o ID do pacote fornecido
        cursor.execute(query, (package_id,))

        # Obter o resultado da consulta
        result = cursor.fetchone()

        # Verificar se a consulta retornou resultados
        if result:
            # Formatar os valores e datas
            result["VALUE"] = format_decimal(Decimal(result["VALUE"]))
            result["START_DATE"] = format_date(result["START_DATE"])
            result["END_DATE"] = format_date(result["END_DATE"])
            
            # Criar uma lista com os resultados formatados
            formatted_result = [result["Country"], result["DestinationCity"], 
                                result["DESCRIPTION"], result["START_DATE"], 
                                result["END_DATE"], result["VALUE"], result["PackageID"]]
            
            return formatted_result
        else:
            return ["Pacote não encontrado."]

    except mysql.connector.Error as error:
        print("Erro ao conectar ao banco de dados:", error)
        return [None]

    finally:
        # Fechar o cursor e a conexão
        if cursor:
            cursor.close()
        if conn:
            conn.close()

