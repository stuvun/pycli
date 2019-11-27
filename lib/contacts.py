from peewee import *
from datetime import date

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    name = CharField()
    birthday = DateField()
    email = CharField()

db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

steven = Contact(name='Steven', birthday=date(1990, 1, 14), email='example2@gmail.com')
steven.save()
roger = Contact(name='Roger', birthday=date(1994, 11, 18), email='example3@gmail.com')
roger.save()
bola = Contact(name='Bola', birthday=date(1994, 2, 13), email='example4@gmail.com')
bola.save()
ray = Contact(name='Ray', birthday=date(1992, 11, 14), email='example5@gmail.com')
ray.save()

new_key = input('Please enter a new contact name: ')
new_name = str(new_key).capitalize()

new_year = int(input('Please enter the birth year: '))
new_month = int(input('Please enter the birth month (number): '))
new_day = int(input('Please enter the birth day: '))

new_email = input('Please enter the email (example1@gmail.com): ')

new_key = Contact(name=new_name, birthday=date(new_year, new_month, new_day), email=new_email)
new_key.save()

print(f"{new_key.name} - {new_key.birthday} - {new_key.email}")