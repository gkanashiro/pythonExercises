
nome=input('Digite seu nome:')
idade=input('Digite sua idade')
q=len(nome)
if nome and idade:
 print(f'seu nome é {nome}')
 print(f'sua idade é {idade}')
 print(f'seu invertido é {nome[::-1]}')
 if " " in nome:
  print(f'seu nome tem espaços')
 else:
  print('seu nome não tem espaços') 
 print(f'sua primeira letra é {nome[0:1:1]}')
 print(f'a última letra do seu nome é {nome[len(nome)-1:len(nome):1]}')
else:    
 print('valor inválido')
