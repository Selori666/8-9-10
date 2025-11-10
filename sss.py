from utilis import add_film, delete_film, find_film

# 8 апта: функциялар мен логика
def show_films(films):
    print("\nФильмдер тізімі:")
    for name, rating in films.items():
        print(f"{name}: {rating}")

def ask_repeat():  # Рекурсия мысалы
    again = input("Қайтадан таңдауды қалайсыз ба? (иә/жоқ): ").lower()
    if again == "иә":
        menu()
    elif again == "жоқ":
        print("Бағдарлама аяқталды.")
    else:
        print("Қате енгізу. Қайта енгізіңіз.")
        ask_repeat()

# Бастапқы деректер
films = {
    "Выживший": 7.8,
    "Остров проклятых": 8.6,
    "Поймай меня, если сможешь": 8.5
}

# 10 апта: файлға сақтау
def save_to_file(films, filename="data.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for name, rating in films.items():
            f.write(f"{name}:{rating}\n")
    print("Мәліметтер файлға сақталды!")

def load_from_file(filename="data.txt"):
    films = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:  # бос жол болса өткізіп кет
                    continue
                parts = line.split(":")
                if len(parts) == 2:
                    name, rating = parts
                    films[name] = float(rating)
                else:
                    print(f"⚠️ Қате форматтағы жол өткізіліп кетті: {line}")
    except FileNotFoundError:
        print("Файл табылмады, жаңа база жасалды.")
    return films


# 9 апта: try-except арқылы қателерді өңдеу
def menu():
    global films
    while True:
        print("\nМәзір:")
        print("1 - Фильмдер тізімі")
        print("2 - Фильм қосу")
        print("3 - Фильм жою")
        print("4 - Рейтинг көру")
        print("5 - Файлға сақтау")
        print("6 - Файлдан оқу")
        print("7 - Шығу")

        choice = input("Таңдауыңыз: ")

        try:
            if choice == "1":
                show_films(films)
            elif choice == "2":
                name = input("Фильм атауы: ")
                rating = float(input("Рейтингі: "))
                films = add_film(films, name, rating)
            elif choice == "3":
                name = input("Жою үшін фильм атауы: ")
                films = delete_film(films, name)
            elif choice == "4":
                name = input("Фильм атауы: ")
                find_film(films, name)
            elif choice == "5":
                save_to_file(films)
            elif choice == "6":
                films = load_from_file()
                print("Файлдан деректер оқылды!")
            elif choice == "7":
                print("Бағдарлама аяқталды.")
                break
            else:
                print("Қате таңдау!")
        except ValueError:
            print("Рейтинг санмен енгізілуі керек!")
        except Exception as e:
            print("Қате:", e)

    ask_repeat()


# Бағдарламаны іске қосу
if __name__ == "__main__":
    films = load_from_file()
    menu()