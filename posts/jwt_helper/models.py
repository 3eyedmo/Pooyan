import mongoengine as me


class User(me.EmbeddedDocument):
    user_id=me.StringField()
    username=me.StringField()

    def is_authenticated(self):
        return True
