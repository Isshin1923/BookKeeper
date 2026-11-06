class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "У наявності" if self.is_available else "Видана"
        return f"'{self.title}' (Автор: {self.author}) — [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"✅ Книгу '{title}' успішно додано!")

    def search_books(self, query):
        query_lower = query.lower()
        results = [book for book in self.books if query_lower in book.title.lower() or query_lower in book.author.lower()]
        
        if results:
            print("\n🔍 Результати пошуку:")
            for book in results:
                print(f"  - {book}")
        else:
            print("\n❌ За вашим запитом нічого не знайдено.")

    def change_status(self, title, is_available):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.is_available = is_available
                status_str = "У наявності" if is_available else "Видана"
                print(f"🔄 Статус книги '{book.title}' змінено на '{status_str}'.")
                return
        print(f"❌ Книгу з назвою '{title}' не знайдено.")

    def show_all(self):
        if not self.books:
            print("\n📚 Бібліотека наразі порожня.")
        else:
            print("\n📚 Список усіх книг:")
            for book in self.books:
                print(f"  - {book}")

def main():
    library = Library()
    
    while True:
        print("\n" + "="*30)
        print("🏛️  МЕНЮ БІБЛІОТЕКИ")
        print("="*30)
        print("1. Додати нову книгу")
        print("2. Знайти книгу (за автором або назвою)")
        print("3. Змінити статус книги")
        print("4. Показати всі книги")
        print("0. Вийти з програми")
        print("="*30)

        choice = input("Оберіть дію (0-4): ").strip()

        if choice == '1':
            title = input("Введіть назву книги: ").strip()
            author = input("Введіть автора книги: ").strip()
            if title and author:
                library.add_book(title, author)
            else:
                print("Помилка: Назва та автор не можуть бути порожніми.")
                
        elif choice == '2':
            query = input("Введіть назву або автора для пошуку: ").strip()
            if query:
                library.search_books(query)
                
        elif choice == '3':
            title = input("Введіть точну назву книги: ").strip()
            status_input = input("Книга у наявності? (так/ні): ").strip().lower()
            if status_input in ['так', 'ні']:
                is_available = status_input == 'так'
                library.change_status(title, is_available)
            else:
                print("Помилка: Будь ласка, введіть 'так' або 'ні'.")
                
        elif choice == '4':
            library.show_all()
            
        elif choice == '0':
            print("👋 Роботу завершено. Гарного дня!")
            break
            
        else:
            print("⚠️ Невірний вибір. Будь ласка, введіть число від 0 до 4.")

if __name__ == "__main__":
    main()