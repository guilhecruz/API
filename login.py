from sqlalchemy import create_engine
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

engine = create_engine('mysql+pymysql://root:@localhost:3306/crud')
app = FastAPI()

class Usuario(BaseModel):
    email: str
    senha: str


@app.post('/cadastro')
def cadastro(usuario:Usuario):
    engine.execute(f"insert into login values(null, '{usuario.email}', '{usuario.senha}');")
    

@app.post('/login')
def logar(usuario:Usuario):
    dados = engine.execute(f"SELECT * FROM login WHERE username = '{usuario.email}' and password = '{usuario.senha}';")
    for dado in dados:
        if(dado.username == usuario.email and dado.password == usuario.senha):
            #print(dado.username)
            return "Logado"
    else:
        return "Email  ou Senha Incorretos"

@app.get('/usuarios/{username}')
def get_usuario(username:str):
    #dados = engine.execute(f"SELECT username FROM login WHERE username = '{username}'")
    #return dados.first()[0]
    #fatchall
    dados = engine.execute(f"SELECT username FROM login WHERE username = '{username}'").fetchone()
    return dados['username']

@app.get('/users')
def get_users():
    #dados = engine.execute(f"SELECT username FROM login WHERE username = '{username}'")
    #return dados.first()[0]
    #fatchall
    lista = []
    dados = engine.execute(f"SELECT * FROM login")
    for row in dados:
        lista.append(row['username'])
    return lista

@app.get('/users2')
def get_users2():
    query = 'SELECT * FROM login'
    df = pd.read_sql(query, con = engine)
    print(df.iloc[0,1])
    return "sucesso"

        






'''
@app.delete('/{id}')
def deleta_usuario(:str):
    for usuario in dados:
        if(usuario.id == id):
            dados.remove(usuario)
            yield "Usuario deletado"
            yield dados
        else:
            return "Usuario não encontrado"
'''
'''
banco_de_dados = [
    Usuario(id=1, email="blueshift@blueshift.com.br", senha="blue123"),
    Usuario(id=2, email="teste@teste.com.br", senha="teste123")
]

@app.post('/')
def raiz(teste:Usuario):
    return teste.email, teste.senha
'''