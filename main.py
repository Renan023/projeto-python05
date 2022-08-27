import datetime, time

at = (datetime.date.today(), datetime.datetime.today().year)
print(at[0])
print('='*50)
print('='*20,'Cadastro','='*20)
time.sleep(0.5)
n = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
id = at[1]- nasc
print(f'{n} sua idade {id} anos em {at[1]}')
s = input('Sexo [M/F] ').strip().upper()[0]
while s not in 'MmFf':
    print('Digite novamente....')
    time.sleep(0.5)
    s = input('Sexo [M/F] ').strip().upper()[0]
    print('Podemos prosseguir com o cadastro ')
pas = input('Digite a frase chave para gerar sua senha ')
s =''
for l in  pas:
    if l in 'Aa': s= s +'1'
    elif l in 'Bb':s= s +'!'
    elif l in 'Cc':s= s +'2'
    elif l in 'Dd':s= s +'@'
    elif l in 'Ee':s= s +'3'
    elif l in 'Ff':s= s +'5'
    elif l in 'Gg':s= s +'6'
    elif l in 'Hh':s= s +'R'
    elif l in 'Ii':s= s +'$'
    elif l in 'Jj':s= s +'4'
    elif l in 'Kk':s= s +'¬'
    elif l in 'Ll':s= s +'7'
    elif l in 'Mm':s= s +'W'
    elif l in 'Nn':s= s +'9'
    elif l in 'Oo':s= s +'Q'
    elif l in 'Pp':s= s +'&'
    elif l in 'Qq':s= s+ 'T'
    elif l in 'Rr':s= s+ '_'
    elif l in 'Ss':s= s+ '='
    elif l in 'Tt':s= s + '|'
    elif l in 'Uu':s= s +'I'
    elif l in 'Vv':s= s+'R'
    elif l in 'Ww':s= s+ '~'
    elif l in 'Xx':s= s+'I'
    elif l in 'Yy':s= s+'S'
    elif l in 'Zz':s= s+'A'
print(f'Sua senha gerada é {s}')
print('Digite novamente sua senha ')
time.sleep(0.5)
c = input('Digite a senha ')
if c!= s:
    print('Acesso negado')
    while c != s:
        print('Digite novamente sua senha ')
        c = input('Digite a senha ')
print(f'{n} poderá realizar seu pedido ')

