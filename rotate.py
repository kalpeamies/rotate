# -*- coding: utf-8 -*-

# Rotaatiosalakirjoituksen salaaja/purkaja
# Pauli Kaikkonen 2016

# Rotaatiosalakirjoituksessa jokainen kirjain korvataan aakkosissa määrätyn monen askeleen päässä olevalla kirjaimella.
# Salausavaimena toimii numero, joka määrää askeleiden määrän.
# Esimerkki: Jos alkuperäinen viesti on "moi" ja salausavain on numero 3, on salattu viesti "prl" (m -> p; o -> r; i -> l)
# Salausavain voi olla myös negatiivinen luku, jolloin askeleet otetaan toiseen suuntaan.


import sys

pienet = "abcdefghijklmnopqrstuvwxyz"
isot = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def korvaa(rotaatio, lause):
    korvattu = ""
    # Tähän merkkijonoon tulee salattu/purettu viesti
    for i in lause:
        if i in isot:
            korvattu += isot[(isot.index(i) + rotaatio) % len(isot)]
            # Korvataan isot kirjaimet
        elif i in pienet:
            korvattu += pienet[(pienet.index(i) + rotaatio) % len(pienet)]
            # Korvataan pienet kirjaimet
        else:
            korvattu += i
            # Numerot ja erikoismerkit lisätään viestiin muuttamattomina
    return korvattu

# Ohjelman syöte on muotoa "rotate.py avain viesti", Esimerkiksi "rotate.py 3 moi"
# Linux-käyttäjien kannattaa tehdä ohjelmalle bash-alias, jotta se toimii missä tahansa hakemistossa

if __name__ == "__main__":
    try:
        print korvaa(int(sys.argv[1]), sys.argv[2])
        # Argumentti 1 on avain (int), argumentti 2 on viesti (string) (ja argumentti 0 on tietysti ohjelman nimi)
    except IndexError:
        print "Invalid command"
        # Liian vähän argumentteja
    except ValueError:
        if sys.argv[1] == "all":
        # "all" syötettynä avaimen paikalle tulostaa kaikki mahdolliset rotaatiot (25 kpl)
            for n in range(1, 26):
                print "rot" + str(n) + ": " + korvaa(n, sys.argv[2])
        else:
            print "Invalid rotation parameter"
