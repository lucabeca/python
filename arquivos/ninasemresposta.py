def orientadora(alunas):
    '''imagine que você é orientadora do if e quer saber quantas garotas têm o mesmo nome
    que o seu.
    retorne para o programa quantas garotas têm o mesmo nome que o seu.'''


def limpador_bucal(palavroes):
    '''o programa dá uma lista dizendo se as palavras são ou não palavrões. separe-as em duas listas, de palavrões e não palavrões.
    se a quantidade de não_palavrões for maior que a quantidade de palavrões, o limpador_bucal não deve entrar em ação.
    retorne True or False.
    ps: o programa te fornece valores booleanos na lista (true or false), então você já sabe se a palavra é ou não um palavrão.'''


def contador_de_a(frase):
    '''retorne quantos caracteres A tem em alguns frases carinhosas, que são:
    - eu amo a marina cada dia mais;
    - a marina é a minha maior inspiração diária;
    - a marina é o meu motivo de sorriso diário. Minha vida não seria a mesma sem ela!
    ps: eu te amo'''


def espirros_gastadores(quantidade_que_espirrei):
    '''pra cada espirro que você dá, você deve guardar no seu cofrinho o número do espirro +
    o número do seu espirro * 50% do número do espirro anterior.
    exemplo: no seu quinto espirro, você vai colocar no seu cofrinho R$5 + 5 * (0,5 * (5 - 1))
    retorne quanto você economizou no final de um dia'''

def gerente(vendas):
    '''Você deve retornar para o programa os meses que tiveram vendas abaixo
    da média anual, no formato jan, fev, mar...
    Além disso, retorne quantos meses ficaram abaixo da média.
    quantia_abaixos, [lista_de_abaixos]
    ps: os valores estão em ordem certa (mês 1, depois 2, depois 3...)'''


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Errou :(')
    else:
        prefixo = '\033[32m%s' % ('Acertou :) parabéns lindona')
        acertos += 1
    print('%s | esperado: %s \tobtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print('\n')
    print('Contagem de Marinas')
    test(orientadora(['marina', 'geovana', 'andrielli', 'roberta', 'josevalda']), 1)
    test(orientadora(['mariana', 'endrovana', 'andrielli', 'roberta', 'josevalda']), 0)
    test(orientadora(['marina', 'marina', 'andrielli', 'marina', 'josevalda']), 3)
    test(orientadora(['marina', 'geovana', 'andrielli', 'roberta', 'josevalda', 'marina', 'allana']), 2)

    print('\n')
    print('Limpador bucal')
    test(limpador_bucal([True, True, False, True, True, False, True, False]), True)
    test(limpador_bucal([False, False, False, True, True, False, True, False]), False)
    test(limpador_bucal([True, True, False, True, True, True, True, False]), True)
    test(limpador_bucal([False, False, False, True, True, False, True, False]), False)

    print('\n')
    print('Espirros gastadores')
    test(espirros_gastadores(19), 1330)
    test(espirros_gastadores(2), 4)
    test(espirros_gastadores(6), 56)
    test(espirros_gastadores(9), 165)
    test(espirros_gastadores(26), 3276)
    test(espirros_gastadores(1), 1)


    print('\n')
    print('Contador de A em frases românticas')
    test(contador_de_a('eu amo a marina cada dia mais'), 8)
    test(contador_de_a('a marina é a minha maior inspiração diária'), 10)
    test(contador_de_a('a marina é o meu motivo de sorriso diário. Minha vida não seria a mesma sem ela!'), 11)


    print('\n')
    print('Vendas abaixo da média anual')
    test(gerente([1000, 1110, 1500, 1640, 1720, 1920, 750, 240, 672, 912, 812, 902]), (7, ['jan', 'jul', 'ago', 'set', 'out', 'nov', 'dez']))
    test(gerente([1098, 1000, 1500, 1220, 1000, 2650, 820, 963, 1022, 675, 850, 914]), (9, ['jan', 'fev', 'mai', 'jul', 'ago', 'set', 'out', 'nov', 'dez']))


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (
        total, acertos, total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Muito bom gatinha, como você aprendeu python agora podemos nos beijar")