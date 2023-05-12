import hashlib
from django.conf import settings

def hasher(
    raw_password: str,
    alg: str =settings.PASSWORD_HASH_ALG,
    salt: str =settings.PASSWORD_HASH_SALT,
    iteration: int =settings.HASH_ITERATION
):
    key = hashlib.pbkdf2_hmac(
        hash_name=alg,
        password=raw_password.encode("utf-8"),
        salt=bytes(salt, "utf8"),
        iterations=iteration
    )
    return str(key)