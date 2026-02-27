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
    {"id": 3, "nome": "Odete", "active": True},
    {"id": 4, "nome": "Doris", "active": True},
    {"id": 5, "nome": "Gabriela", "active": False},
    {"id": 6, "nome": "Laion", "active": True},
    {"id": 7, "nome": "Marcelo", "active": True},
    {"id": 8, "nome": "Marlene", "active": False},
    {"id": 9, "nome": "Astride", "active": False},
    {"id": 10, "nome": "Marguit", "active": False},
    {"id": 11, "nome": "Elisângela", "active": True},
    {"id": 12, "nome": "Vera", "active": True},
    {"id": 13, "nome": "Ana Beatriz", "active": False},
    {"id": 14, "nome": "Adriane", "active": False},
    {"id": 15, "nome": "Fernanda", "active": False}
] 
active_users = [user for user in users if user["active"]]
inactive_users = [user for user in users if not user["inactive"]]
print(f'Usuários ativos: \n{active_users}\n')
print(f'Usuários inativos: \n{inactive_users}\n')

nomes = [user["name"] for user in users]
print(nomes)