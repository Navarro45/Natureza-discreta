set1 = {}
set2 = {}
resultado = {}
vetor1 = []
vetor2 = []

while True:
  vetor1.clear()
  vetor2.clear()
  print("=============")
  print("Selecione a sua operação:")
  print("Digite U para realizar a união dos conjuntos;")
  print("Digite I para realizar a intersecção;")
  print("Digite D para realizar a diferença;")
  print("Digite C para realizar o produto cartesiano;")
  print("Digite S para finalizar o programa;")
  operacao = input("Qual será a opção desejada:")

  print("=============")

  if operacao == 'S':
    break
  n = int(input("Digite a quantidade de números para o conjunto 1:"))
  n2 = int(input("Digite a quantidade de números para o conjunto 2:"))

  for i in range(n):
    vetor1 += [input("Digite os elementos do primeiro set: ")]

  for i in range(n2):
    vetor2 += [input("Digite os elementos do segundo set: ")]

  set1 = set(vetor1)
  set2 = set(vetor2)

  if operacao == 'U':
    resultado = set1.union(set2)
    print("União: conjunto 1 {}, conjunto 2 {},. Resultado: {}".format(
        set1, set2, resultado))

  elif operacao == 'I':
    resultado = (set1 & set2)
    print("Interseção: conjunto 1 {}, conjunto 2 {},. Resultado: {}".format(
        vetor1, vetor2, resultado))
  elif operacao == 'D':
    resultado = set1.difference(set2)
    print("Diferença: conjunto 1 {}, conjunto 2 {},. Resultado: {}".format(
        vetor1, vetor2, resultado))
  elif operacao == "C":
    resultado = {(x, y) for x in vetor1 for y in vetor2}
    print("Produto cartesiano: conjunto 1 {}, conjunto 2 {},. Resultado: {}".
          format(vetor1, vetor2, resultado))
  else:
    print("Digite uma operação válida")
