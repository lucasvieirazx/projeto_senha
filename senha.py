import random

senha = ''
caracteres = 'abcdefghij1234567890'
for digito in range(8):
    aleatorio = random.choice(caracteres)
    senha += aleatorio

print('-' * 15)
print(senha)
print('-' * 15)