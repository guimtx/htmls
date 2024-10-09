import random
aleatorio= random.randint(1,100)
i=10
soma=0
print('o numero secreto esta entre 1 e 100')
while(i>0):
    soma+=1
    palpite=int(input('digite o palpite numero '))
    if(palpite<aleatorio):
        print('o numero que voce digitou é menor que o numero secreto')
    elif(palpite>aleatorio):
        print('o numero que voce digitou é maior que o numero secreto')
    elif(palpite==aleatorio):
        break
    i-=1
    print('restam ',i,' tentativas')
if(palpite==aleatorio):
    print('parabens voce acertou em ',soma, 'tentativas')

else:
    print('é você não acertou seu burro mongoloide otario nojento')

