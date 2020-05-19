from werkzeug.security import generate_password_hash, check_password_hash
import json

def hash_create(string):
    return generate_password_hash(string)
    
def hash_verify(encrypt, string):
    return check_password_hash(encrypt, string)

def time_serial(datetime):
    print(datetime)
    return json.dumps(datetime)