"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys


def mimic_dict(filename):
  """Retorna o dicionario imitador mapeando cada palavra para a lista de
  palavras subsequentes."""
    # +++ SUA SOLUÇÃO +++

  words = []
  idxpass = 0
  word_before = ''
  dictLetters = {}

  with open(filename, "r") as file:
    # one_line = file.readline()
    # all_lines = file.readlines()
    for line in file:
      for word in line.split():
        wordlow = word.lower()
        words.append(wordlow)
        if len(words) == 1:
          dictLetters[''] = [wordlow]
          #print('First word: //' + str(dictLetters.get('')) + '//')
          word_before = wordlow
        else:
          if wordlow != word_before and word_before not in dictLetters:
            dictLetters[word_before] = [wordlow]
            #print('#' + str(idxpass) + ' WORD: //' + word_before + ' //  NEXT_TO: ' + str(dictLetters.get(word_before)) + ' //')
            word_before = wordlow
          elif wordlow != word_before:
            dictLetters[word_before].append(wordlow)
            #print('#' + str(idxpass) + ' WORD: //' + word_before + ' //  NEXT_TO: ' + str(dictLetters.get(word_before)) + ' //')
            word_before = wordlow
          else:
            # print('#' + str(idxpass) + ' IGNORING WORD: //' + wordlow + ' //')
            pass

        idxpass += 1

  if word_before not in dictLetters:
    dictLetters[word_before] = ['']
  else:
    dictLetters[word_before].append('')

  print('First word: // \'\' // NEXT_TO: ' + str(dictLetters.get('')) + '//')
  print('Last word: //' + word_before + ' // NEXT_TO: ' + str(dictLetters.get(word_before)) + '//')
  print(str(dictLetters))

  return dictLetters


def print_mimic(mimic_dict, word):
  """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    # +++ SUA SOLUÇÃO +++

  print(word)
  for i in range(200):
    next_word = random.choice(mimic_dict[word])
    word = next_word
    print(str(word), end=' ')

  print('')
  return


# Chama mimic_dict() e print_mimic()
def main():
  if len(sys.argv) != 2:
    print('Utilização: ./14_mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
