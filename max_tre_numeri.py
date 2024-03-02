def max_tre_numeri():
    a = input("Inserire il primo numero: ")
    b = input("Inserire il secondo numero: ")
    c = input("Inserire il terzo numero: ")
    #converto i numeri da stringhe in float
    a = float(a)
    b = float(b)
    c = float(c)
    max = 0
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c 
    print("Il numero maggiore è: " + str(max))

max_tre_numeri()