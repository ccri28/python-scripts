prezzo = input('Inserire prezzo: ')
sconto = input('Inserire sconto: ')
#faccio il casting in float delle due variabili
prezzo = float(prezzo)
sconto = float(sconto)
scala = prezzo * sconto / 100
prezzo_scontato = prezzo - scala
#arrotonda il numero a due decimali
prezzo_scontato = round(prezzo_scontato,2)
print(f"Il prezzo scontato è: {prezzo_scontato}")
