# cadastro-clientes #
Para começar, você pode usar o framework Flask para criar seu aplicativo web. Ele é fácil de usar e possui uma documentação clara. Para instalar o Flask, você precisará de Python 3.7 ou superior. 
`python.exe -m pip install --upgrade pip`

# Quickstart
1. Crie um ambiente virtual para isolar as dependências do projeto: `python -m venv venv`
2. Ative o ambiente virtual: `venv\Scripts\activate.bat`
3. Instale o Flask: `pip install flask`
4. Crie um arquivo app.py na raiz do seu projeto e cole o seguinte código:
```py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)
```
5. Salve o arquivo e execute o aplicativo: `python app.py`
6. Abra o seu navegador e visite http://localhost:5000. Você deve ver uma mensagem "Hello, world!" na página.