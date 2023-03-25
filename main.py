from source.phonebook import PhoneBook

def main():
    ph_book = PhoneBook()
    ph_book.fill_from_csv("test.csv")
    ph_book.print_book()

if __name__=="__main__":
    main()