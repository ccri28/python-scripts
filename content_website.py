import urllib.request as urllib2

url = "http://www.cristianfaciano.it"

risposta_server = urllib2.urlopen(url)
dati_server = risposta_server.read()

print("##### INIZIO A SCANSIONARE IL SITO #####")
print(dati_server)

try:
    file_html = open("contenuto_sito.html","w")
    file_html.write(str(dati_server))
except Exception:
    print("Errore durante la scrittura del file")
else:
    file_html.close()

print("FINITO!")