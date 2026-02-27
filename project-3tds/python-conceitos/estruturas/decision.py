nome = 'Joao'
altura = 1.80
casado = True
idade = 18

if idade >=18:
    print(f'{nome} é maior de idade.')

elif idade >=60:
    print(f'{nome} é idoso.')   

if casado:
    print('{nome} é casado')
elif not casado:
    print(f'{nome} é infeliz')    

  idade1 = 19
  autorizacao = True
  
  if idade1>=18 or autorizacao:
    print("pode entrar")
    else:
        print(" nao pode entrar")
