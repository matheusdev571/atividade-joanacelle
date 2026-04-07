#11 Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par
negativo”; Caso contrário → “Ímpar”
a= int(input("digite um numero: "))
if ( a % 2 ==0 ):
  if (a > 0 ):
  print("par positivo")
else:
  print("par negativo")
else:
  print("impar")
