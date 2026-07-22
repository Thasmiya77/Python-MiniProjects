import random
import string
password_len=12
password_values=string.ascii_letters+string.digits+string.punctuation
password="".join([random.choice(password_values) for i in range(password_len)])
print(" your password is:",password)