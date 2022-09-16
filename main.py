import datetime, character, numero, password

at = (datetime.date.today(), datetime.datetime.today().year)

print(at[0])
character.principal('Cadastro')
n = character.leiachar('Nome: ')
nasc = numero.leiaint('Ano de nascimento: ')
id = at[1]- nasc
print(f'{n} sua idade {id} anos em {at[1]}')
character.sexo()
print('Podemos prosseguir com o cadastro ')
password.password()
print(f'{n} poderá realizar seu pedido ')

