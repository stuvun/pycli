from peewee import *
from datetime import date
import tkinter as tk
from tkinter import *

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

run = "Y"
while run == "Y":
    # Prints all the available options for navigating contacts
    selection = input("Please enter an option (enter '?' to see list of options): ").lower()
    while selection != "?" and selection != "a" and selection != "s" and selection != "v":
        selection = input("There are no options that match your selection.\nPlease enter a valid option (enter '?' to see list of options): ").lower()
    if selection == "?":
        print("- 'a' to add a new contact\n- 'e' to edit a contact\n- 's' to search for a contact by their name\n- 'v' to view all saved contacts")
    # Creates a new contact (name, birthdate(year, month, day), email)
    if selection == "a":
        new_key = input("Please enter a new contact name: ")
        new_name = str(new_key).capitalize()
        new_year = int(input("Please enter the birth year: "))
        new_month = int(input("Please enter the birth month (number): "))
        new_day = int(input("Please enter the birth day: "))
        new_email = input("Please enter the email (example@gmail.com): ")
        new_key = Contact(name=new_name, birthday=date(new_year, new_month, new_day), email=new_email)
        new_key.save()
        print(f"\nSuccessfully added '{new_key.name} - {new_key.birthday} - {new_key.email}' to your contacts list.")
    # Searches for the list id of the entered name and prints the details of that id's row
    if selection == "s":
        name_search = str(input("Please enter the name of the contact you are looking for: ")).capitalize()
        query = Contact.select().dicts()
        search_id = Contact.get(Contact.name == name_search).id - 1
        print(query[search_id])
    # Prints the full list of saved contacts
    if selection == "v":
        query = Contact.select().dicts()
        for i in query:
            print(i)
    run = input("Would you like to do something else? (Y/N): ").capitalize()
    while run != "Y" and run != "N":
        run = input("Please enter 'Y' or 'N': ").capitalize()