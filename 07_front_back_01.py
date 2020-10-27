"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

def even(a):
    if len(a) % 2 == 0:
        return True
    else:
        return False


def frentestr(a):
    idmeio = int(len(a)/2)
    if even(a):
        return idmeio, a[:idmeio]
    else:
        return idmeio+1, a[:idmeio+1]


def front_back(a, b):
    # +++ SUA SOLUÇÃO +++

    id_a_tras, a_frente = frentestr(a)
    id_b_tras, b_frente = frentestr(b)

    # print('ID Tras A: >>>  ' + str(id_a_tras) + ' ' + a_frente)
    # print('ID Tras B: >>>  ' + str(id_b_tras) + ' ' + b_frente)

    return ''.join((a_frente, b_frente, a[id_a_tras:], b[id_b_tras:]))


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
