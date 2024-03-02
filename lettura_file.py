import os

file_name = input("Inserire il percordo del file da leggere: ")

if os.path.exists(file_name):
    #with si occupa automaticamente della chiusura del file dopo che è stato letto il contenuto del file
    with open(file_name, 'r') as file:
        content = file.read()
        print('\n')
        print(content)
else:
    print('\n')
    print(f"Il file {file_name} non esiste.")