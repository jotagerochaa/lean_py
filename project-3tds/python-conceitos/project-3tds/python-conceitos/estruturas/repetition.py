""""
pessoas = [
    {
        "nome":"Joao",
        "idade": 30
    }, #pessoa0
    {
        "nome":"Maria",
        "idade": 25
    }, #pessoa1
    {
        "nome":"Pedro",
        "idade": 20
    } #pessoa2
]

nomes = [] 
idades = []
for pessoa in pessoas:
    nomes.append(pessoa["nome"]) #nova lista de nomes
    idades.append(pessoa["idade"]) #nova lista de idades
print(f'{nomes}, {idades}')

nomes = [pessoa["nome"] for pessoa in pessoas] #quero o nome de cada pessoa em pessoas
idades = [pessoa["idade"] for pessoa in pessoas] #quero a idad de cada pessoa em pessoas 
print(nomes)
print(idades)


users = [
    {"id": 1, "name": "João", "active": True},
    {"id": 2, "name": "leandro", "active": False},
    {"id": 3, "name": "Odete", "active": True},
    {"id": 4, "name": "Doris", "active": True},
    {"id": 5, "name": "Gabriela", "active": False},
    {"id": 6, "name": "Laion", "active": True},
    {"id": 7, "name": "Marcelo", "active": True},
    {"id": 8, "name": "Marlene", "active": False},
    {"id": 9, "name": "Astride", "active": False},
    {"id": 10, "name": "Marguit", "active": False},
    {"id": 11, "name": "Elisângela", "active": True},
    {"id": 12, "name": "Vera", "active": True},
    {"id": 13, "name": "Ana Beatriz", "active": False},
    {"id": 14, "name": "Adriane", "active": False},
    {"id": 15, "name": "Fernanda", "active": False}
] 
active_users = [user for user in users if user["active"]]
inactive_users = [user for user in users if not user["active"]]
print(f'Usuários ativos: \n{active_users}\n')
print(f'Usuários inativos: \n{inactive_users}\n')

nomes = [user["name"] for user in users]
#   capture o nome do usuario para cada usuario em users
#for user in users:
print(nomes)
"""
"""
for i in range(5):
    if i % 2 == 0:
     print(f'Iteração{i} é par')
else:
    print(f'Iteração{i} é impar')

for i in range(1, 6):
  print(f'Iteração {i}')
    
for i in range(0,10,2):
     print(f'Iteração {i}')
     """
     
usuarios = [
{
"username": "joao123",
"password": "joaodogas123"},

{
    "username": "maria123",
    "password": "maria444"},

{
    "username": "pedro123",
    "password": "pedro321"},
]   

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
def login(username, password):
    for usuario in usuarios
    if usuario ["username"] == username and usuario ["password"] == password:
        return "Login bem-sucedido"
        return "Login falhou"
    
print(login("joao123", "joaodoga123"))

