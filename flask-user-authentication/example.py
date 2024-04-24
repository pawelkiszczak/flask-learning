from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

# BCRPYT
bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bcrypt.generate_password_hash(password=password)
print(hashed_password)

check = bcrypt.check_password_hash(hashed_password, 'wrongpassword')
print(check)

check = bcrypt.check_password_hash(hashed_password, 'supersecretpassword')
print(check)

# WERKZEUG
hashed_pass = generate_password_hash('mypassword')
print(hashed_pass)

check = check_password_hash(hashed_pass, 'wrongpassword')
print(check)

check = check_password_hash(hashed_pass, 'mypassword')
print(check)