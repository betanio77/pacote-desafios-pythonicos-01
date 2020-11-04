"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

def linear_merge(list1, list2):
    # +++ SUA SOLUÇÃO +++
    # print('Lista1: ' + str(list1))
    # print('Lista2: ' + str(list2))

    listmerge = []
    idxmerge = 0
    idx1 = 0
    idx2 = 0
    hasitem1 = True
    hasitem2 = True

    while len(listmerge) < (len(list1) + len(list2)):
        # print('idx1: ' + str(idx1) + '  //  idx2: ' + str(idx2))
        if hasitem1 and hasitem2:
            if list1[idx1] < list2[idx2]:
                listmerge.append(list1[idx1])
                if idx1 < len(list1)-1:
                    idx1 += 1
                else:
                    hasitem1 = False
            else:
                listmerge.append(list2[idx2])
                if idx2 < len(list2)-1:
                    idx2 += 1
                else:
                    hasitem2 = False
        elif hasitem1:
            listmerge.append(list1[idx1])
            if idx1 < len(list1) - 1:
                idx1 += 1
            else:
                hasitem1 = False
        elif hasitem2:
            listmerge.append(list2[idx2])
            if idx2 < len(list2) - 1:
                idx2 += 1
            else:
                hasitem2 = False

        # print('listmerge: ' + str(listmerge))
        idxmerge += 1

    return listmerge


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
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
