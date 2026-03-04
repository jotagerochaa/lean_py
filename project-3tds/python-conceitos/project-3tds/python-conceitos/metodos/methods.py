"""
METODOS SAO BLOCOS DE CÓDIGOS QUE REALIZAM UMA TAREFA ESPECIFICA
E PODEM SER REUTILIZADOS EM DIFERENTES PARTES DO PROGRAMA.
ELES SAO DEFINIDOS USANDO "DEF" SEGUIDA PELO NOME DO METODO,
E ENTRE PARENTESES, OS PARAMETROS.
"""
def saudacao(nome):
    print(f'Ola,{nome}!')

saudacao('Joao')
saudacao('Lara')
saudacao('Jose')
saudacao('babu')
saudacao('calleri')

cadastros = [
{
"username": "joao123",
"password": "joaodogas123"},

{
    "username": "maria123",
    "password": "maria444"},

{
    "username": "pedro123",
    "password": "pedro321"}
]

def formatacao_username(username):
    return username.replace(" ", "").lower()

def cadastrar(username,password):
    valid_username = formatacao_username(username)
    print(valid_username)
    for cadastro in cadastros:
        if cadastro['username'] == username:
            return 'Usuario ja cadastrado'
    cadastros.append({
        "username": username,
        "password": password,
    })
    return 'Usuario cadastrado com sucesso'

print(cadastrar('Joao', 'catapimbas'))
print(cadastrar('Juca', 'bode'))
print(cadastrar('lucas', 'abacaxi'))