pessoas = [
{
    "nome":"Muriel";
    "idade:" 30
 }

{
    "nome": "Maria";
    "idade": 25
    }

{
    "nome": "Pedro";
    "idade:" 39
    }

]
nomes = [] 
nomes.append(pessoas[0]["nome"])
nomes.append(pessoas[1]["nome"]) 
nomes.append(pessoas[2]["nome"]) 


for pessoa in pessoas
nome.append(pessoa["nome"])
idades.append(pessoas["idade"])
print(f'{nomes}, ["idades"])

nomes = [pessoa["nome"] for pessoa in pessoas]
idades = [pessoa["idade"] for pessoa in pessoas]
print(nomes)
print(idades)