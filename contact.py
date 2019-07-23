from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')

class Contact(Model):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    note = TextField()

    class Meta:
        database = db


    def full_name(self):
        return (f'{self.first_name.capitalize} {self.last_name.capitalize}')

db.connect()
db.create_tables([Contact])
