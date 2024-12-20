from openai import OpenAI  # Biblioteka do komunikacji z modelem OpenAI

# Inicjalizacja klienta OpenAI z kluczem API
client = OpenAI(api_key="TWÓJ_KLUCZ_API")  # Wprowadź swój klucz API tutaj

# Ścieżka do pliku wejściowego
file_path = "files/tekst.txt"

# Odczytywanie zawartości pliku tekstowego
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()  # Wczytanie treści pliku do zmiennej

# Ścieżka do pliku wyjściowego
output_file_path = "files/artykul.html"

# Tworzenie pliku wyjściowego do zapisu HTML
with open(output_file_path, "w", encoding="utf-8") as output_file:
    # Wysyłanie zapytania do modelu OpenAI
    stream = client.chat.completions.create(
        model="gpt-4o-mini",  # Model, który ma przetwarzać zapytanie
        messages=[{
            "role": "user",  # Rola użytkownika w interakcji
            "content": (
                f"{file_content} \n"  # Dodanie treści z pliku
                "Przekształć tekst na kod HTML z odpowiednimi tagami. Wstaw miejsca na grafikę, używając tagu "
                "<img src='image-placeholder.jpg'> w sekcji alt wpisz dokładny prompt opisujący obrazek, "
                "który byłby w odpowiedniej formie aby później można było go użyć do wygenerowania grafiki w programie AI."
                "Do każdego obrazu dodaj podpis w tagu <figcaption>.Twoja odpowiedź powinna zawierać tylko treść między tagami "
                "<body> i </body>, gotową do zapisania w pliku .html. Nie używaj CSS ani tagów <body> i </body> w odpowiedzi."
            )
        }],
        stream=True,  # Włączenie strumieniowania odpowiedzi
    )

    # Iteracja po odpowiedzi modelu
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:  # Sprawdzenie, czy fragment odpowiedzi zawiera dane
            output_file.write(chunk.choices[0].delta.content)  # Zapis fragmentu do pliku

# Informacja o zakończeniu pracy programu
print(f"\nKod HTML został zapisany do pliku: {output_file_path}")
