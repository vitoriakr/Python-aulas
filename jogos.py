import random

def escolher_palavra():
    palavras = ['python','desenvolvimento','jogo','programacao','algoritimo']
    return random.choice(palavras).upper()

def jogo_forca():
    palavra = escolher_palavra()
    letras_adivinhacao = []
    tentativas = 6
    
    print( 'Seja bem-vindo ao jogo da forca ')
    print('_ '*len(palavra))
    
    while tentativas>0:
        tentativa =input('Tente uma letra: ').upper()
              
        if tentativa in letras_adivinhacao:
            print('Você já tentou essa letra. Tente novente.')
            continue
        
        letras_adivinhacao.append(tentativa)
        
        if tentativa in palavra:
            print(' A letra está na palavra.')
        
        else :
            tentativas -= 1 
        print('Errado! Você tem () tentativas restantes. '.format(tentativas))
        
        palavra_oculta=" ".join( letra if letra in letras_adivinhacao else "_" for letra in palavra )
        print(" ".join(palavra_oculta))
    
        if "_" not in palavra_oculta:
            print("Parábens! você acertou a palavra.")
            break 
    
    if tentativas == 0 :
        print('Você perdeu! Apalvra era ()'.format(palavra))
    
jogo_forca()
    