# 1. Ask what the user would like to do
# 2. Inform user to enter "?" to see list of options
#     i.   "a" for adding a new contact
#     ii.  "e" for editing a contact
#     iii. "d" for deleting a contact
#     iv.  "v" to look for a contact by their first name
#     v.   "l" to view all contacts

from peewee import *
from datetime import date

db = PostgresqlDatabase("contacts", user="postgres", password="",
                        host="localhost", port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    name = CharField()
    birthday = DateField()
    email = CharField()

db.connect()

selection = input("Please select an option (enter '?' to see list of options): ")
if selection == "?":
    print("- 'a' to add a new contact\n- 'e' to edit a contact\n- 'v' to look for a contact by their name\n- 'l' to view all saved contacts")
# Creates a new contact (name, birthdate(year, month, day), email)
if selection == "a":
    new_key = input("Please enter a new contact name: ")
    new_name = str(new_key).capitalize()
    new_year = int(input("Please enter the birth year: "))
    new_month = int(input("Please enter the birth month (number): "))
    new_day = int(input("Please enter the birth day: "))
    new_email = input("Please enter the email (example1@gmail.com): ")
    new_key = Contact(name=new_name, birthday=date(new_year, new_month, new_day), email=new_email)
    new_key.save()
    print(f"\nSuccessfully added '{new_key.name} - {new_key.birthday} - {new_key.email}' to your contacts list.")
if selection == "v":
    name_search = str(input("Please enter the name of the contact you are looking for: ")).capitalize()
    query = Contact.select()
    search_id = Contact.get(Contact.name == name_search).id - 1
    print(query[search_id].name)