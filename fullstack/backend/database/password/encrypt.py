import bcrypt
def encrypt(password:str):
    password_bytes = password.encode("utf-8")
    salt = b"$2b$12$abcdefghijklmnopqrstuu"
    hashed = bcrypt.hashpw(password_bytes,salt)
    return hashed.decode()
