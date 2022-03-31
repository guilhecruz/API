from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine
import pandas as pd


# Base de dados
engine = create_engine('mysql+pymysql://root:@localhost:3306/followup_bs')
connection = engine.connect()
app = FastAPI()


# Raiz


@app.get('/')
def root():
    return {"Olá,": "mundo"}

# Modelo


@app.get('/email')
def users():
    query = f'SELECT * FROM tb_usuarios'
    #result = conn.execute(query).first()
    df = pd.read_sql(query, connection)
    return df


class Usuario(BaseModel):
    email: str
    senha: str




# Get All


@app.get('/usuarios')
def get_usuarios():
    return base_de_dados

# Get ID


@app.get('/usuarios/{id_usuario}')
def get_usuario_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario

    return{"Status": 404, "Mesagem": "Usuário não encontrado"}


def cadastro(usuario: Usuario):
    try:
        engine.execute(
            f"insert into login values(null, '{usuario.email}','{usuario.senha}');")
        return "Cadastro realizado com sucesso"
    except:
        return "Email não pode ser utilizado"

# Insere Usuario


@app.post('/cadastro')
def insere_usuario(usuario: Usuario):
    try:
        engine.execute(
            f"insert into login values(null, '{usuario.email}','{usuario.senha}');")
        return "Cadastro realizado com sucesso"
    except:
        return "Email não pode ser utilizado"


@app.delete('/delete')
def deleta_usuario(usuario: Usuario):
    base_de_dados.pop(usuario)
    return usuario
