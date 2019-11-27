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
    phone = CharField()


db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

steven = Contact(name='Steven', birthday=date(1990, 1, 14), phone='555-555-5551')
steven.save()
roger = Contact(name='Roger', birthday=date(1994, 11, 18), phone='555-555-5552')
roger.save()
bola = Contact(name='Bola', birthday=date(1994, 2, 13), phone='555-555-5553')
bola.save()
ray = Contact(name='Ray', birthday=date(1992, 11, 14), phone='555-555-5554')
ray.save()

print(f"{steven.name} - {steven.birthday} - {steven.phone}")

steven.birthday = date(1993, 1, 14)
steven.phone = '555-555-5555'
steven.save()

print(f"{steven.name} - {steven.birthday} - {steven.phone}")