# Utilizando o dicionário para substituir a matriz, sendo chave = caracter e valor = posição na matriz
polibio = {'A':'11','B':'12','C':'13','D':'14','E':'15','F':'16',
           'G':'21','H':'22','I':'23','J':'24','K':'25','L':'26',
           'M':'31','N':'32','O':'33','P':'34','Q':'35','R':'36',
           'S':'41','T':'42','U':'43','V':'44','W':'45','X':'46',
           'Y':'51','Z':'52','0':'53','1':'54','2':'55','3':'56',
           '4':'61','5':'62','6':'63','7':'64','8':'65','9':'66'}

#  RECEBE UMA FRASE DE ENTRADA E FAZ A ENCRIPTAÇÃO DA MESMA

# Criação de uma estrutura de repetição(FOR) para cada elemento da frase, contendo uma estrutura de comparação, onde a condição se aplica a frases com espaço

def encryption(frase):
    # Criação de uma variável do tipo string para o resultado final
    cripto = ""
    for letra in frase.upper():
        if letra == ' ':
            cripto += ' '
            continue
            #Letra por letra na frase
        cripto += polibio[letra] # Acesso ao dicionário, de acordo com a chave = letra, adicionando a string do valor da chave o resultando final(cripto)
        # Se i da frase for = 'A', ele pega o polibio cujo a chave é = 'A', sendo assim '11'
    return cripto

###   RECEBE UM CÓDIGO E DESENCRIPTA O MESMO

def decryption(descript):
    ## Criação de uma variável do tipo string para o resultado final
    uncripto = ""
    # Criação de uma estrutura de repetição(While) para comparar os valores das chaves dos dicionários com o código digitado
    while descript:
        # Estrutura de comparação para condição onde chave tenha espaço
        if descript[0] == ' ':
            # Adiciona espaço no resultado final
            uncripto += ' '
            # Cortando o index 0 que seria o espaço da string
            descript = descript[1:]
        # Acessando a chave com index
        for chave in polibio:
            # Comparação entre o dicionário na posição 'chave' que seja igual ao 2 números do código inserido
            if polibio[chave] == descript[:2]:
                # Adiciona a chave ao resultado final, logo em seguida corta os dois primeiros números do código inserido
                uncripto += chave
                descript = descript[2:]
                break
    return uncripto
