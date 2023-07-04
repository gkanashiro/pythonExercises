primeiroValor=input('Digite um valor: ')
segundoValor=input('Digite um  segundo valor: ')
if (primeiroValor.isdecimal()) and (segundoValor.isdecimal()):
 pv=int(primeiroValor)
 sv=int(segundoValor)
else:
 print('primeiro valor ou segundo valor inválido')
 quit()
if (int(primeiroValor)>int(segundoValor)): 
        print(f'O  primeiro valor {primeiroValor} é maior que o segundo valor {segundoValor}')

elif (int(primeiroValor)<int(segundoValor)): 
        print(f'O  primeiro valor {primeiroValor} é menor que o segundo valor {segundoValor}')

elif (int(primeiroValor)==int(segundoValor)): 
        print('O  primeiro valor {} é igual que o segundo valor {}'.format(primeiroValor,segundoValor))
 
 
