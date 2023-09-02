# Sistema Fox Travel

# ambiente virtual
 criar o ambiente na pasta raiz
    python -m venv venv
 ativar o ambiente virtual
    raiz/venv/Scripts/Activate.ps1
 Video de apoio:
 https://www.youtube.com/watch?v=m1TYpvIYm74


# atualizar ao salvar alterações
    no fim do arquivo raiz/main.py
        if __name__ == '__main__':
            app.run(debug=True)
    lembrar de alterar após o desenvolvimento

# bibliotecas
    Back end Flask
        pip install flask
    