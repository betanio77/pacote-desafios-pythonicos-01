"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""

def not_bad(s):
    # +++ SUA SOLUÇÃO +++

    id_not = 0
    id_bad = 0
    i = 0
    before_not = ''
    after_bad = ''
    list_str = s.split()

    for str in list_str:
        if str == 'not' and id_not == 0:
            id_not = i
        elif str == 'bad' and id_bad == 0:
            id_bad = i
        elif id_not == 0:
            before_not += str + ' '
        elif id_bad != 0:
            after_bad += str

        i += 1;

    if id_bad > id_not:
        return ''.join((before_not, 'good'))
    else:
        return s



# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
