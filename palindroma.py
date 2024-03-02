def palindroma():
    stringa = input('Inserisci una stringa: ')
    #ricavo la lunghezza della stringa inserita 
    lungezza = len(stringa)
    #ricavo l'ultimo indice della stringa 
    indice = lungezza - 1
    nuova_stringa = ''
    while indice >= 0:
        nuova_stringa += stringa[indice]
        indice -= 1
    if nuova_stringa == stringa:
        print("La parola inserita è palindroma")
    else:
        print("La parola inserita non è palindroma")

palindroma()
