import itertools as it
import time as t
import os
import string as s
import random as r
clear = lambda : os.system("cls")
clear()
def prolomeni(mod, GUI, slovo):
    words = [""]
    word = ""
    hesel = 0
    clear(
    nalezeno = False
    znaky = s.ascii_lowercase + s.ascii_uppercase + s.digits
    if slovo == True:
        words = []
        while True:
            print("Zmáčkni Enter pro ukončení výběru slov.")
            word = input("Zadej jaký slovo víš, že bude na začátku: ")
            clear()
            if word == "" or word == " ":
                break
            words.append(word)
    if mod == False:
        znaky = input("Napiš z jakých znaků mám vybírat: ")
        clear()
    for w in words:
        hesel += len(znaky)**(len(password)-len(w))
    c = 1
    print("Možných hesel: " + str(hesel))
    pokr = input("Přejete si pokračovat? (a = ano, n = ne): ")
    clear()
    if pokr == "a":
        start = t.time()
        cont = True
        for w in words:
            if cont == False:
                break
            comb = list(it.product(znaky, repeat=len(password)-len(w)))
            for item in comb:
                item = w + "".join(item)
                if GUI == True:
                    print("Zkouším " + str(c)+ ". z " + str(hesel) + " hesel.")
                    c += 1
                    print(item)
                    clear()
                if item == password:
                    nalezeno = True
                    cont = False
                    break
        if nalezeno == True:
            print("Heslo nalezeno!")
            print("Heslo: " + item)
        else:
            print("Heslo nenalezeno.")
        print("Strávený čas: " + str(round((t.time()-start), 1)) + " sekund")
        print("")
        pokr = input("Přeješ si spustit program znovu? (a = ano, n = ne): ")
        clear()
        if pokr == "a":
            main1()
        else:
            input("Zmáčkni libovolnou klávesu pro ukončení.")
            clear()
    else:
        input("Zmáčkni libovolnou klávesu pro ukončení.")
        clear()
def main1():
    print("------------------------------")
    print("-----PASSWORD CRACKER 7.0-----")
    print("---------by DampAdam----------")
    print("------------------------------")
    print("")
    print("=====================================================")
    print("Changelog:")
    print("")
    print("2.0:")
    print("- Přidána menu grafika")
    print("- Přidány 2 další možnosti, bez GUI a s GUI")
    print("")
    print("3.0:")
    print("- Přidány 2 další možnosti, se slovem, který víš a bez")
    print("- Optimalizace")
    print("")
    print("4.0:")
    print("- Přidána funkce vygenerování hesla")
    print("")
    print("5.0 (Největší update):")
    print("- Ultra mega velká optimalizace a zrychlení až o 4000%!")
    print("- Přidáno po špatným napsání zopakování")
    print("- Přidána funkce spustit program znovu po ukončení")
    print("")
    print("5.1:")
    print("- Přidán Changelog")
    print("")
    print("6.0:")
    print("- Vylepšení funkce Slovo na začátku (můžete přidat více slov)")
    print("")
    print("7.0")
    print("- Přidaná funkce Slovo na začátku u generování random hesla")
    print("========================================================")
    print("")
    global password
    global delka
    def main():
        mode = input("Jaký mód si přeješ (vse = vsechny písmena a čísla budou použity, nevse = zadáš písmena/čísla ty): ")
        clear()
        if mode == "vse":
            mode = input("Chceš to s GUI? (a = ano, n = ne): ")
            clear()
            if mode == "a":
                mode = input("Víš, jaký slovo bude na začátku hesla? (a = ano, n = ne): ")
                if mode == "a":
                    prolomeni(True, True, True)
                elif mode == "n":
                    prolomeni(True, True, False)
                else:
                    print("Někde nastala chyba!")
                    main()
            elif mode == "n":
                mode = input("Víš, jaký slovo bude na začátku hesla? (a = ano, n = ne): ")
                if mode == "a":
                    prolomeni(True, False, True)
                elif mode == "n":
                    prolomeni(True, False, False)
                else:
                    print("Někde nastala chyba!")
                    main()
            else:
                print("Někde nastala chyba!")
                main()
        elif mode == "nevse":
            mode = input("Chceš to s GUI? (a = ano, n = ne): ")
            clear()
            if mode == "a":
                mode = input("Víš, jaký slovo bude na začátku hesla? (a = ano, n = ne): ")
                if mode == "a":
                    prolomeni(False, True, True)
                elif mode == "n":
                    prolomeni(False, True, False)
                else:
                    print("Někde nastala chyba!")
                    main()
            elif mode == "n":
                mode = input("Víš, jaký slovo bude na začátku hesla? (a = ano, n = ne): ")
                if mode == "a":
                    prolomeni(False, False, True)
                elif mode == "n":
                    prolomeni(False, False, False)
                else:
                    print("Někde nastala chyba!")
                    main()
            else:
                print("Někde nastala chyba!")
                main()
        else:
            print("Někde nastala chyba!")
            main()
    def heslo(znaky, slovo):
        global password
        wordt = []
        w = ""
        symboly = s.ascii_letters + s.digits
        if znaky == True:
            symboly = input("Napiš z jakých znaků si mám vybírat: ")
            clear()
        if slovo == True:
            w = input("Napiš slovo, který má být na začátku hesla: ")
            clear()
        for m in range(delka-len(w)):
            pis = r.choice(symboly)
            wordt.append(pis)
        password = w + "".join(wordt)
        main()
    znaky = s.ascii_uppercase + s.ascii_lowercase + s.digits
    wordt = []
    mode = input("Přeješ jsi, aby za tebe program vygeneroval random heslo? (a = ano, n = ne): ")
    clear()
    if mode == "a":
        delka = input("Napiš kolik znaků má mít vygenerovaný heslo: ")
        clear()
        try:
            delka = int(delka)
        except:
            print("Musíš napsat celé číslo!")
            main1()
        else:
            mode = input("Chceš zadat písmena/čísla, který tam budou? (a = ano, n = ne): ")
            clear()
            if mode == "a":
                mode = input("Chceš zadat slovo, který má být na začátku hesla? (a = ano, n = ne): ")
                clear()
                if mode == "a":
                    heslo(True, True)
                elif mode == "n":
                    heslo(True, False)
                else:
                    print("Někde nastala chyba!")
                    main1()
            elif mode == "n":
                mode = input("Chceš zadat slovo, který má být na začátku hesla? (a = ano, n = ne): ")
                clear()
                if mode == "a":
                    heslo(False, True)
                elif mode == "n":
                    heslo(False, False)
                else:
                    print("Někde nastala chyba!")
                    main1()
            else:
                print("Někde nastala chyba!")
                main1()
    elif mode == "n":
        password = input("Napiš heslo: ")
        clear()
        main()
    else:
        print("Někde nastala chyba!")
        main1()
main1()