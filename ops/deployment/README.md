# INFRA

1. Atualize o Sistema:
Primeiro, atualize os pacotes do sistema:

```bash
sudo apt update && sudo apt upgrade -y
```
2. Instale o Git:
```bash
sudo apt install git -y
```
3. Clone o Repositório:
```bash
sudo mkdir /var/www
cd /var/www/
sudo git clone https://github.com/devlucasbernardes/ProjetoIntegrador
sudo mv ProjetoIntegrador/ html
```
4. Instale Python e Pip:

```bash
sudo apt install python3 python3-pip -y
```

5. Instale as Dependências do Projeto:
```
cd /var/www/html/
//sudo pip3 install -r requirements.txt
```
6. Configurar o Flask para Execução Externa:
Certifique-se de que o app é executado com host='0.0.0.0' para torná-lo acessível externamente. Seu código deve se parecer com:


``` python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
7. Execute a Aplicação:

``` bash
python3 nome_do_seu_script.py
```
8. Configurar Firewall:

Se você tiver um firewall ativo, pode ser necessário abrir a porta 5000:
No meu caso, tive abrir a porta no azure.

``` bash
sudo ufw allow 5000
```


sudo apt-get install screen
screen -S sess_1
source venv/bin/activate
sudo python3 app.py


# Desconecte-se da sessão screen:
```powershell
# Desconecte-se da sessão screen:
# Pressione Ctrl + A e depois Ctrl + D. 
# Isso irá desconectá-lo da sessão screen, 
# mas manterá sua aplicação Flask em execução.
```
 