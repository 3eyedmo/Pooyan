def validate_passwords(pass1, pass2):
    if pass1 != pass2:
        return False, "passwords are not equal"
    if not 5 < len(pass2) < 25:
        return False, "passwords must have 6 to 25 chars"
    return True, "success"