
import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 10

password1 = "".join(random.choices(total,k=length))
password = "".join(random.sample(total,length))

print("Password = ",password1)
print("Password = ",password)

