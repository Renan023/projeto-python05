import time

def leiachar(char):
    while True:
        try:
            char = input(char)
        except (KeyboardInterrupt):
            print('\n\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return char

def principal(msg):
    print('='*50)
    print(msg.center(50))
    print('='*50)
    time.sleep(0.5)

def sexo():
    s = input('Sexo [M/F] ').strip().upper()[0]
    while s not in 'MmFf':
        print('Digite novamente....')
        time.sleep(0.5)
        s = input('Sexo [M/F] ').strip().upper()[0]