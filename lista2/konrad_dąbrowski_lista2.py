import random
import sqlite3
import ssl
import pandas as pd
from sklearn.model_selection import LeaveOneOut
from sklearn.preprocessing import normalize
from sklearn.linear_model import LogisticRegression


ssl._create_default_https_context = ssl._create_unverified_context

# Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
# Użyj reszty wierszy jako nagłówków ramki danych.
# Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.

file = open("pliktextowy.txt", "r")
lines = file.read().splitlines()

url = lines[0]
columns = lines[1:]

df = pd.read_csv(url, names=columns)  # tutaj podmień df. Ma zawierać wczytane dane.

# Zadanie1 przypisz nazwy kolumn z df w jednej linii:   (2pkt)

wynik1 = ",".join(df.columns)
print(wynik1)

# Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii.  (2pkt)
wynik2 = f"Liczba wierszy: {df.shape[0]}, Liczba kolumn: {df.shape[1]}"
print(wynik2)


# Zadanie Utwórz klasę Wine na podstawie wczytanego zbioru:
# wszystkie zmienne objaśniające powinny być w liscie.
# Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
# listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
# nazwy mogą być dowolne.

# Klasa powinna umożliwiać stworzenie nowego obiektu na podstawie
# już istniejącego obiektu jak w pdf z lekcji lab6.
# podpowiedź: metoda magiczna __repr__
# Nie pisz metody __str__.

class Wine:
    def __init__(self, vals, type):
        self.vals = vals
        self.type = type

    def __repr__(self):
        return f'Wine([{", ".join(repr(value) for value in self.vals)}], {repr(self.type)})'


# Zadanie 3 Utwórz przykładowy obiekt:   (3pkt)
wynik3 = Wine([random.randint(1, 1000) for val in columns], random.randint(1, 3))  # do podmiany. Pamiętaj - ilość elementów, jak w zbiorze danych.
# Uwaga! Pamiętaj, która zmienna jest zmienną objaśnianą
print(wynik3)

# Zadanie 4.                             (3pkt)
# Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
# Nie podmieniaj listy, dodawaj elementy.
# Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniane i objąśniająca.
# Podpowiedź zobacz w pliktextowy.txt
wineList = []
for index, row in df.iterrows():
    vals = row.values[1:]
    type = row.values[0]
    wineList.append(Wine(vals, type))

wynik4 = len(wineList)
print(wynik4)

# Zadanie5 - Weź ostatni element z listy i na podstawie         (3pkt)
# wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
# do wyniku przypisz zmienną objaśnianą z tego obiektu:
wynik5 = eval(repr(wineList[-1])).type
print(wynik5)

# Zadanie 6:                                                          (3pkt)
# Zapisz ramkę danych  do bazy SQLite nazwa bazy(dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
# Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:

conn = sqlite3.connect('konraddabrowskis24415.db')

df.to_sql('wines', conn, if_exists='replace', index=False)
conn.close()

conn = sqlite3.connect('konraddabrowskis24415.db')
query = "SELECT * FROM wines WHERE TypeOf = 3"
only_type_3 = pd.read_sql_query(query, conn)
conn.close()

wynik6 = "W następnej linijce podmień na nowy  data frame z winami tylko klasy trzeciej:"
wynik6 =only_type_3  # tutaj do podmiany

print(wynik6.shape)

# Zadanie 7                                                          (1pkt)
# Utwórz model regresji Logistycznej z domyślnymi ustawieniami:

model = LogisticRegression()

wynik7 = model.__class__.__name__
print(wynik7)

# Zadanie 8:                                                        (3pkt)
# Dokonaj podziału ramki danych na dane objaśniające i  do klasyfikacji.
# Znormalizuj dane objaśniające za pomocą:
# preprocessing.normalize(X)
# Wytenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
#  Podaj średnią dokładność (accuracy)

y = df.iloc[:, 0]
X = df.iloc[:, 1:]

X_normalized = normalize(X)
model = LogisticRegression()

cv = LeaveOneOut()
accuracy_scores = []
for train_index, test_index in cv.split(X_normalized):
    X_train, X_test = X_normalized[train_index], X_normalized[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    accuracy_scores.append(accuracy)

average_accuracy = sum(accuracy_scores) / len(accuracy_scores)

wynik8 = average_accuracy
print(wynik8)