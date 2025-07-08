# База данных книг для проверки
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int) -> None:
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"


class Library:

    def __init__(self, books=None) -> None:
        """
        Не забудьте про 'Конструктор должен принимать необязательный аргумент со значением по умолчанию. Если пользователь
        его не передал, то библиотека инициализируется с пустым списком книг.'
        :param books:
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        """
        Необходимо узнать последнюю книгу в библиотеке, посмотреть атрибут 'id' этой книги и вернуть следующее
        значение после этого `id`
        :return:
        """
        if not self.books:
            return 1
        return self.books[-1].id_ + 1


    def get_index_by_book_id(self, id__: int) -> int:
        """
        Так как в библиотеке книги хранятся в списке, то данная функция возвращает индекс где книга с определенным
        `id` хранится в списке книг. Для примера. [Book(id=1, ...), Book(id=2, ...)] книга с id=2 хранится
        на индексе 1 списка книг
        :param id_: id книги
        :return: индекс, где лежит книга в списке книг
        """
        for index, book in enumerate(self.books):
            if book.id_ == id__:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
