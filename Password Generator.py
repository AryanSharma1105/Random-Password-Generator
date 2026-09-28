      
#Import Random and String Module
import random
import string

#Decide Your Password's Characters and its length
characters = string.ascii_letters + string.digits + string.punctuation

length = 16

#Random Password with Unique Characters
password = "".join(random.sample(characters,length))

#Another Random Password with Repeating Characters
password1 = "".join(random.choices(characters,k = length))
	
print("Your Unique Password is:",password)
print("Your Password is:",password1)




