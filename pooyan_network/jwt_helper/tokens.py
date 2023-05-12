from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class MongoTokenMixin:
    @classmethod
    def for_user(cls, user):
        """
        Returns an authorization token for the given user that will be provided
        after authenticating the user's credentials.
        """
        user_id = getattr(user, "id")
        if not isinstance(user_id, int):
            user_id = str(user_id)

        token = cls()
        token["user_id"] = user_id
        token["username"] = user.username

        return token
    

class MongoAccessToken(MongoTokenMixin, AccessToken):...
    
    
class MongoRefreshToken(MongoTokenMixin, RefreshToken):
    access_token_class = MongoAccessToken