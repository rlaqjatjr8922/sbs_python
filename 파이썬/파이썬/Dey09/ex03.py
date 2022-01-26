from os import name
import secure as q
from secure import *

name = '김범석'
no = '080731-1234567'
phone = "010-4859-8922"

print( secure_name(name))
print( secure_on(no))
print( secure_phone(phone))