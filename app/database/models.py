import datetime
from mongoengine import Document, StringField, IntField, BooleanField, DateTimeField



class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    is_admin = BooleanField(default=False)
    is_active = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
