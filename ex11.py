import random
mix = []

def word(f):
    file = open(f, 'r')
    words = file.read()
    global aleatory
    aleatory = random.choice(words.lower().split())
    return aleatory

def guess():

    for x in aleatory:
        mix.append(x)
        random.shuffle(mix)
    w = ''.join(mix)
    print(f'A palavra que você deve adivinhar é --->> {w}')
    print('Boa sorte você tem 6 tentativas')

def attempt():
    i = 7
    while not i == 0:
        play = input('Digite a palavra: ')

        if play == aleatory:
            print('Meus parabéns, você adivinhou a palavra !!!')

        elif i == 1:
            print('Você perdeu todas suas chances')
            break

        else:
            i-=1
            print(f'Ops não é essa a palavra , você possui {i} chances')
    print(f'A palavra era {aleatory}')

if __name__ == '__main__':

    word('aleatory_words')
    guess()
    attempt()



