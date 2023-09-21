def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."
    for char in string:
        if char not in valid:
            return True
            break
    return False

def is_valid(email):
    valid = True
    if email.count("@") != 1:
        return False
    if email.count(".") != 1:
        return False
    if ".com" not in email:
        return False
    if "@" in email:
        parts = email.split("@")
        prefix = parts[0]
        domain = parts[1]
    else:
        return False
    if has_invalid_characters(prefix) == True:
        return False
    if has_invalid_characters(domain) == True:
        return False
    dom_parts = domain.split(".")
    domain_name = dom_parts[0]
    extension = dom_parts[1]
    if email.count("@") != 1:
        return False
    elif email.count(".") != 1:
        return False
    elif len(prefix) == 0:
        return False
    elif len(domain_name) == 0:
        return False
    elif len(extension) == 0:
        return False
    return valid