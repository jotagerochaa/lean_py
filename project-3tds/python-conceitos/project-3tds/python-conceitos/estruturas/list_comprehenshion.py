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
ids = [user["id"] for user in users]
ids_nao_ativos = [user["id"] for user in users if not user["active"]]
ids_ativos = [user["id"] for user in users if user ["active"]]
print(nomes)
print('todos os ids: ',ids)
print('todos os ids ativos: ',ids_ativos)
print('todos os ids inativos: ',ids_nao_ativos)


prices = [100.0, 250.0, 80.0, 150.0]
discounted =  [price * 0.9 for price in prices]
desconto_10 = [price * 0.10 for price in prices]
desconto_20 = [price * 0.20 for price in prices]
desconto_30 = [price * 0.30 for price in prices]
desconto_40 = [price * 0.40 for price in prices]
desconto_50 = [price * 0.50 for price in prices]

print(desconto_10)
print(desconto_20)
print(desconto_30)
print(desconto_40)
print(desconto_50)

raw_emails = [      
    "J O A   O@e ma il.c om"
    " P e DR o@ em ail.C oM"
]

striped_emails = [email.strip() for email in raw_emails]
print(f'emails sem espaços:{striped_emails}\n')

lower_emails = [email.lower() for email in raw_emails]
print(f'emails em letra minuscula: {lower_emails}\n')

emails =[email.strip() .lower() for email in raw_emails]
print(f' emails limpos: {emails}\n\n\n')

emails_limpos = [email.lower().replace(" ", "") for email in emails]
print(emails_limpos)

# list comprehenshion é uma forma concisa
# de criar listas a partir de iteráveis
# aplicando uma expressão a cada item e
# opcionalmente filtrando os itens com umq
# condição. A sintxe basica é:
# nova_lista - [ expressao for item in interavel if condição]