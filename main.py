'''
QUESTO PROGRAMMA IMPLEMENTA IL FAMOSISSIMO GIOCO "CARTA, FORBICE, SASSO"

ATTENZIONE: Prima di far partire il programma assicurarsi di aver installato "emoji" per poter visualizzare le stesse.
Per installare basterà dare sul terminale il comando:
pip install emoji
e riavviare l'IDE

NON TI RESTA CHE COMINCIARE A GIOCARE!
'''

import random

scelte_possibili = ["carta", "forbice", "sasso"]
punteggio = [0, 0]
nome_giocatore = input("BENVENUTO GOCATORE!\nInserisci il tuo nome: ").upper()

while True:
    # stampa punteggio
    print("******************************************")
    print(f'********** {nome_giocatore} = {punteggio[0]}  |  PC = {punteggio[1]} **********')
    print("******************************************\n")
    scelta_utente = ""

    # scelta oggetto da parte dell'utente
    while scelta_utente not in scelte_possibili:
        scelta_utente = input("Scegli un oggetto (carta, forbice, sasso): ")
        if scelta_utente not in scelte_possibili:
            print("Oggetto non riconosciuto...RIPROVARE")

    # scelta oggetto da parte del pc
    scelta_pc = random.choice(scelte_possibili)
    print(f"\nTu hai scelto {scelta_utente}, il pc ha scelto {scelta_pc}.\n")

    # controllo chi vince confrontando i due oggetti scelti
    if scelta_utente == scelta_pc:
        print(f"Entrambi avete scelto {scelta_utente}. PAREGGIO! 👌")
    elif scelta_utente == "sasso":
        if scelta_pc == "forbice":
            print("Il sasso schiaccia la forbice! HAI VINTO! 😀")
            punteggio[0] += 1
        else:
            print("La carta copre il sasso! Hai perso ☹")
            punteggio[1] += 1
    elif scelta_utente == "carta":
        if scelta_pc == "sasso":
            print("La carta copre il sasso! HAI VINTO! 😀")
            punteggio[0] += 1
        else:
            print("La forbice taglia la carta! Hai perso ☹")
            punteggio[1] += 1
    elif scelta_utente == "forbice":
        if scelta_pc == "carta":
            print("La forbice taglia la carta! HAI VINTO! 😀")
            punteggio[0] += 1
        else:
            print("La roccia schiaccia la forbice...hai perso ☹")
            punteggio[1] += 1

    # controllo la volontà da parte dell'utente di continuare a giocare
    check = input("\nGIOCARE ANCORA? (s/n): ")
    while check.lower() != "s" and check.lower() != "n":
        check = input("INPUT NON VALIDO!\nGIOCARE ANCORA? (s/n): ")
    if check.lower() != "s":
        break

# fine del gioco: riepilogo punteggio ed esito finale
print(f'\nD\'ACCORDO {nome_giocatore} GRAZIE PER AVER GIOCATO\nIL PUNTEGGIO FINALE E\': {nome_giocatore} = {punteggio[0]}  |  PC = {punteggio[1]}')
if punteggio[0] > punteggio[1]:
    input("HAI VINTO! 😀\n\n...TORNA PRESTO 😉")
elif punteggio[0] < punteggio[1]:
    input("Hai perso! ☹\n\n...TORNA PRESTO 😉")
else:
    input("Hai pareggiato! \n\n...TORNA PRESTO 😉")
