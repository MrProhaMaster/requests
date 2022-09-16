import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

class PhoneBook:
  def __init__(self, lastname, firstname, surname='', organization='', position='', phone='', email=''):
      self.lastname = lastname
      self.firstname = firstname
      self.surname = surname
      self.organization = organization
      self.position = position
      self.phone = phone
      self.email = email

  def __str__(self):
    return f"{self.lastname} {self.firstname} {self.surname},{self.organization},{self.position},{self.phone},{self.email}"

for person in contacts_list:
    if ' ' in person[0]:
        a = contacts_list[contacts_list.index(person)][0].split(' ')
        for i in a:
            person[a.index(i)] = i
    if ' ' in person[1]:
        a = contacts_list[contacts_list.index(person)][1].split(' ')
        for i in a:
            person[a.index(i)+1] = i
pattern = r"^(\+7|8)?\s*\(*(\d{1,3})\)*\s*\-*(\d{1,3})\s*\-*(\d{1,2})\s*\-*(\d{1,2})\s*\(*доб.\s*(\d*)\)*"
for person in contacts_list[1:]:
    if person in contacts_list:
        contacts_list[contacts_list.index(person)][5] = re.sub(pattern, r"+7(\2)\3-\4-\5 доб.\6", person[5])
        for check in contacts_list[1:]:
            if person[0]+person[1] == check[0]+check[1] and contacts_list.index(person) < contacts_list.index(check):
                for i in person:
                    if i == '':
                        if check[person.index(i)] == '':
                            contacts_list[contacts_list.index(person)][person.index(i)] = ' '
                        else:
                            contacts_list[contacts_list.index(person)][person.index(i)] = contacts_list[contacts_list.index(check)][person.index(i)]
                contacts_list.pop(contacts_list.index(check))
for person in contacts_list[1:]:
    for i in person:
        if i == ' ':
            contacts_list[contacts_list.index(person)][person.index(i)] = ''

# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)