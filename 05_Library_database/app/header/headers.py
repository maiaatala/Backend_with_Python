def theader(op):
    x = 30

    if op.lower() == "all":
        print("\t+{}+{}+{}+{}+".format("=" * x, "=" * x, "=" * x, "=" * x))
        print(
            "\t| {:^28} | {:^28} | {:^28} | {:^28} |".format(
                "Books", "Publisher", "Author", "Cathegory"
            )
        )
        print("\t+{}+{}+{}+{}+".format("=" * x, "=" * x, "=" * x, "=" * x))
        # print("\t+{}+{}+{}+{}+".format("-"*30, "-"*30, "-"*30, "-"*30))

    elif op.lower() == "author":
        print("\t+{}+".format("=" * x))
        print("\t| {:^28} |".format("Authors"))
        print("\t+{}+".format("=" * x))
        # print("+{}+".format("-"*30))

    elif op.lower() == "publisher":
        print("\t+{}+".format("=" * x))
        print("\t| {:^28} |".format("Publishers"))
        print("\t+{}+".format("=" * x))
        # print("+{}+".format("-"*30))

    elif op.lower() == "category":
        print("\t+{}+".format("=" * x))
        print("\t| {:^28} |".format("Categories"))
        print("\t+{}+".format("=" * x))
        # print("+{}+".format("-"*30))

    elif op.lower() == "book":
        print("\t+{}+{}+{}+{}+".format("=" * x, "=" * x, "=" * x, "=" * x))
        print(
            "\t| {:^28} | {:^28} | {:^28} | {:^28} |".format(
                "Book", "Publisher", "Author", "Cathegory"
            )
        )
        print("\t+{}+{}+{}+{}+".format("=" * x, "=" * x, "=" * x, "=" * x))
        # print("\t+{}+{}+{}+{}+".format("-"*30, "-"*30, "-"*30, "-"*30))
