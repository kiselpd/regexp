import re
import csv
from pprint import pprint


class PhoneBook:
  
    def __init__(self):
        self.__book = {}


    def __read_csv(self, file_csv_name: str):
        with open(file=file_csv_name, mode='r') as file_csv:
            return list(csv.DictReader(file_csv))
    

    def __bring_to_format(self, phone: dict) -> dict:
        format_dict = {}

        full_name = phone["lastname"] + " " + phone["firstname"] + " " + phone["surname"]
        name_patter = re.compile(r"(\w*)\s+(\w*)\s+(\w*)")

        lastname = name_patter.sub(r"\1", full_name)
        
        format_dict["firstname"] = name_patter.sub(r"\2", full_name)
        format_dict["surname"] = name_patter.sub(r"\3", full_name)

        format_dict["organization"] = phone["organization"]
        format_dict["position"] = phone["position"]
        format_dict["email"] = phone["email"]

        phone_patter = re.compile(r"(\+7|7|8)?\D?\(?(\d{3})\)?\D?(\d{3})\D?(\d{2})\D?(\d{2})(\s*)\(?(доб\.)?\s*(\d*)\)?")
        format_dict["phone"] = phone_patter.sub(r"+7(\2)\3-\4-\5\6\7\8", phone["phone"])
        
        return {lastname : format_dict}
    

    def __add_new_phone(self, phone_dict: dict):
        key_lastname = list(phone_dict.keys())[0]

        if key_lastname not in self.__book:
            self.__book.update(phone_dict)
        else:
            for key in self.__book[key_lastname]:
                if self.__book[key_lastname][key] == '':
                    self.__book[key_lastname][key] = phone_dict[key_lastname][key]

    
    def fill_from_csv(self, file_csv_name: str):
        list_phone = self.__read_csv(file_csv_name)

        for item in list_phone:
            format_phone_dict = self.__bring_to_format(item)
            self.__add_new_phone(format_phone_dict)


    def print_book(self):
        pprint(self.__book, width=100, sort_dicts=False)