from rest_framework_simplejwt.tokens import RefreshToken

class MongoRefreshToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        """
        Returns an authorization token for the given user that will be provided
        after authenticating the user's credentials.
        """
        user_id = user.id
        token = cls()
        token['user_id'] = str(user_id)
        return token
