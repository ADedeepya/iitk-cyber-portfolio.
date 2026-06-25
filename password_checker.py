def passwordChecker(password):
    if len(password) < 5:
        return False
        
    caps = any(c.isupper() for c in password)
    nums = any(c.isdigit() for c in password)
    symb = any(c in '!@#$%^&' for c in password)
    
    if not caps:
        return False
    elif not nums:
        return False
    elif not symb:
        return False
    else:
        return True
