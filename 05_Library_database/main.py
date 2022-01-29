from app import crud as c
from os import system, path


def main_menu():
    print(
        "\t+--------+--------+\n"
        "\t| option |  Menu  |\n"
        "\t+--------+--------+\n"
        "\t| c      | Create |\n"
        "\t| r      | Read   |\n"
        "\t| u      | Update |\n"
        "\t| d      | Delete |\n"
        "\t| e      |  exit  |\n"
        "\t+--------+--------+\n"
    )


def create_menu():
    print(
        "\t+-----------+--------------------------+\n"
        "\t|  option   |       Create Menu        |\n"
        "\t+-----------+--------------------------+\n"
        "\t| book      | Register a new Book      |\n"
        "\t| author    | Register a new Author    |\n"
        "\t| publisher | Register a new Publisher |\n"
        "\t| category  | Register a new Category  |\n"
        "\t+-----------+--------------------------+\n"
    )


def read_menu():
    print(
        "\t+------------+-------------------------+\n"
        "\t|   option   |        Read Menu        |\n"
        "\t+------------+-------------------------+\n"
        "\t| consult    | Search an specific name |\n"
        "\t| book       | Show all books          |\n"
        "\t| author     | Show all authors        |\n"
        "\t| publisher  | Show all publishers     |\n"
        "\t| category   | Show all categories     |\n"
        "\t+------------+-------------------------+\n"
    )


def update_menu():
    print(
        "\t+-----------+--------------------+\n"
        "\t|  option   |    Update Menu     |\n"
        "\t+-----------+--------------------+\n"
        "\t| book      | Update a Book      |\n"
        "\t| author    | Update an Author   |\n"
        "\t| publisher | Update a Publisher |\n"
        "\t| category  | Update a Category  |\n"
        "\t+-----------+--------------------+\n"
    )


def delete_menu():
    print(
        "\t+-----------+--------------------+\n"
        "\t|  option   |    Delete Menu     |\n"
        "\t+-----------+--------------------+\n"
        "\t| book      | Delete a Book      |\n"
        "\t| author    | Delete an Author   |\n"
        "\t| publisher | Delete a Publisher |\n"
        "\t| category  | Delete a Category  |\n"
        "\t+-----------+--------------------+\n"
    )


def consult_menu():
    print(
        "\t+-----------+-------------------------------------+\n"
        "\t|  option   |            Consult Menu             |\n"
        "\t+-----------+-------------------------------------+\n"
        "\t| Book      | Consult if a Book is in the db      |\n"
        "\t| author    | Consult if an Author is in the db   |\n"
        "\t| publisher | Consult if a Publisher is in the db |\n"
        "\t| Category  | Consult if a Category is in the db  |\n"
        "\t+-----------+-------------------------------------+\n"
    )
    pass


menuing = "c r u d e".split()
options = "book author publisher category".split()
loop = True
db_path = "db/lib.db"
if not path.exists(db_path):
    c.init_db()

while loop:
    system("clear")
    main_menu()
    if (urs_menu := input(">> escolha: ").lower()) in menuing:
        if urs_menu == "c":
            create_menu()
            if (urs_menu := input(">> escolha: ").lower()) in options:
                if urs_menu == "book":
                    c.create_book()
                elif urs_menu == "author":
                    c.create_author()
                elif urs_menu == "publisher":
                    c.create_publisher()
                elif urs_menu == "category":
                    c.create_category()
            else:
                print("\t<< not a valid menu option! try again...")

        elif urs_menu == "r":
            read_menu()
            if (
                urs_menu := input(">> escolha: ").lower()
            ) in options or urs_menu == "consult":
                if urs_menu == "book":
                    c.show_all_books()
                elif urs_menu == "author":
                    c.show_all_authors()
                elif urs_menu == "publisher":
                    c.show_all_publishers()
                elif urs_menu == "category":
                    c.show_all_categories()
                elif urs_menu == "consult":
                    consult_menu()
                    if (urs_menu := input(">> escolha: ").lower()) in options:
                        if urs_menu == "book":
                            print(
                                "\t<< Search book by 'title', 'author', 'publisher' or 'category'?"
                            )
                            urs_input = input(">> ").lower()
                            if urs_input == "title":
                                print("\t<< Write the title: ")
                                urs_input = input(">> ").lower()
                                c.search_books(urs_input)
                            elif urs_input == "author":
                                print("\t<< Write the Author's name: ")
                                urs_input = input(">> ").lower()
                                c.books_by(urs_input, "author")
                            elif urs_input == "publisher":
                                print("\t<< Write the Publisher's name: ")
                                urs_input = input(">> ").lower()
                                c.books_by(urs_input, "publisher")
                            elif urs_input == "category":
                                print("\t<< Write the Category's name: ")
                                urs_input = input(">> ").lower()
                                c.books_by(urs_input, "genre")
                        elif urs_menu == "author":
                            print("\t<< Write the Author's name: ")
                            urs_input = input(">> ").lower()
                            c.search_author(urs_input)
                        elif urs_menu == "publisher":
                            print("\t<< Write the Publisher's name: ")
                            urs_input = input(">> ").lower()
                            c.search_publisher(urs_input)
                        elif urs_menu == "category":
                            print("\t<< Write the Category's name: ")
                            urs_input = input(">> ").lower()
                            c.search_category(urs_input)
            else:
                print("\t<< not a valid menu option! try again...")

        elif urs_menu == "u":
            update_menu()
            if (urs_menu := input(">> escolha: ").lower()) in options:
                if urs_menu == "book":
                    c.update_book()
                elif urs_menu == "author":
                    c.update_author()
                elif urs_menu == "publisher":
                    c.update_publisher()
                elif urs_menu == "category":
                    c.update_category()

            else:
                print("\t<< not a valid menu option! try again...")

        elif urs_menu == "d":
            delete_menu()
            if (urs_menu := input(">> escolha: ").lower()) in options:
                if urs_menu == "book":
                    c.delete_book()
                elif urs_menu == "author":
                    c.delete_author()
                elif urs_menu == "publisher":
                    c.delete_publisher()
                elif urs_menu == "category":
                    c.delete_genre()
            else:
                print("\t<< not a valid menu option! try again...")

        elif urs_menu == "e":
            print("\t<< Byeee...")
            loop = False
            break
    else:
        print("\t<< not a valid menu option! try again...")
    input("\n...Press enter do continue...")


# Postgrees
# estudar API - microservico - jeito de comunicacao utilizado (json)
# estudar fast API
