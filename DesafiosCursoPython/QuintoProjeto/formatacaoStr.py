nome = 'Gabriel'
inteiro=12
#variações de String

print(f'%s , %d , %x' % (nome, inteiro, inteiro)) 
print (f'{nome}')
print (f'{nome:0>10}')
print (f'{nome:0<10}')
print (f'{nome:^21}')
print (f'{100.4323435:-,.1f}')
print (f'{100.4323435:+,.1f}')
print (f'{100.4323435:0>-,.1f}')
print (f'1500 em hexa é {1500:08X}')

#Fatiamento de Strings

var='Ola Mundo'

print(var[4:7])

print (var[0:len(var):1])