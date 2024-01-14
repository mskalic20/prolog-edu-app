# prolog-edu-app
Repozitorij za projekt iz kolegija UUI, prolog aplikacija

---------------------------------------------------------------------------------

UPUTE ZA POKRETANJE
u terminalu se sa naredbom cd postaviti na pravilnu lokaciju

u mome slucaju to je bilo
cd prolog_edu

a puna putanja je bila C:\Users\Marko\Desktop\PrologEduApp\prolog_edu>

Nakon toga pokrećete server sa naredbom "python EdukacijaApp.py"

Nakon što ste pokrenuli Flask server
U web pregledniku otvorite http://127.0.0.1:5000/

---------------------------------------------------------------------------------

Nalazite se na početnoj stranici
S lijeve strane je sidebar
Trenutno postoje tri destinacije gdje možete ići
- Lekcije
- Kvizovi
- Projekti i Primjeri koda

U planu je bilo da na stranici Lekcije budu postavljeni materijali za učenje prologa, ali trenutno je prazna

Slično i sa stranicom Kvizovi, na njoj je zamišljeno da se mogu rješavati kvizovi, ali trenutno nema dodanih kvizova

Ono što nas najviše zanima je stranica Projekti i Primjeri koda

Na toj stranici se na vrhu nalazi forma u kojoj možete unositi i testirati vlastiti prolog kod

Ispod forme je linije preko koje se pokreću pravila

Pored linije je gumb "Provjeri rješenje"

Klikom na gumb ispisuje se na ekran rješenje upita ili odgovarajuća poruka o grešci

Također postoji gumb "Analiza programa"

Klikom na njega aplikacija pokušava povezati odgovarajući kod u formi sa opisom i ključnim rječima nekog zadatka, te ako zna o čemu se radi javlja na ekranu što misli da se u kodu traži

Na kraju na dnu stranice imamo kratke opise zadataka.
