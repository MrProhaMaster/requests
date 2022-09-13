import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
for i in contacts_list:
    print(i)
    
class PhoneBook:
  def __init__(self, lastname, firstname, surname=None, organization=None, position=None, phone=None, email=None):
      self.lastname = lastname
      self.firstname = firstname
      self.surname = surname
      self.organization = organization
      self.position = position
      self.phone = phone
      self.email = email

  def __str__(self):
    return f"{self.lastname} {self.firstname} {self.surname}: {self.organization}, {self.position}, {self.phone}, {self.email}"

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)