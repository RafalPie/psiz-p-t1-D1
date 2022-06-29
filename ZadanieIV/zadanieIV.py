import os

nazwa_pierwszego_pliku = input('prosze wpisac sciezke do pierwszego pliku: ')
nazwa_drugiego_pliku =  input('prosze wpisac sciezke do drugiego pliku: ')
rozmiar_pierwszego_pliku=os.path.getsize(nazwa_pierwszego_pliku)
rozmiar_drugiego_pliku=os.path.getsize(nazwa_drugiego_pliku)
