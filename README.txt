Narzędzie do generowania sekcji body HTML za pomocą OpenAI.

Program jest narzędziem do generowania stron internetowych na podstawie tekstu wejściowego. Wykorzystuje model OpenAI do konwersji tekstu na kod HTML. Główne funkcje programu obejmują:
1.	Odczyt pliku wejściowego: Program odczytuje treść pliku tekstowego, który zawiera surową treść do przekształcenia w stronę HTML.
2.	Komunikacja z OpenAI:
	•Program wysyła treść pliku wraz z wytycznymi do modelu gpt-4o-mini.
	•Wytyczne definiują, jak należy strukturyzować treść w HTML, w tym miejsca na grafiki z odpowiednimi atrybutami alt.
3.	Generacja HTML:
	•Model zwraca strumieniowo wygenerowany kod HTML, który jest zapisywany w pliku wyjściowym o nazwie artykul.html.
4.	Zapis danych do pliku:
	•Kod HTML jest zapisany w pliku wyjściowym, gotowym do wklejenia w sekcji body kodu HTML.


Wymagania:
1.	Python w wersji 3.8 lub wyższej.
2.	Biblioteka openai (można zainstalować poleceniem: pip install openai)
3.	Pliki wejściowe:
	Katalog "files" z plikiem "tekst.txt",który służy do formatowania 
	przez AI na kod gotowy do wklejenia do sekcji body
4.	Klucz API OpenAI, który powinien zostać wklejony w miejscu:
	client = OpenAI(api_key="TWÓJ_KLUCZ_API")

Uruchomienie programu:
1.	python main.py

Struktura projektu:

├── main.py              # Główny plik programu
├── files/               # Katalog z plikami wejściowymi i wyjściowymi
│   ├── tekst.txt        # Plik wejściowy z treścią do przetworzenia
│   ├── artykul.html     # Wygenerowany plik HTML

