#18
a= int(input("digite um numero: "))
if (a == 0):
  print("neutro")
elif (a % 2 == 0 ):
  if (a > 0):
    print("par positivo")
  else:
    print("par negativo")
else:
 if ( a > 0):
   print ("impar positivo")
 else:
   print ("impar negativo")