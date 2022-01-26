'''
    개인정보마스킹
    마스킹 :김*석,김**,080731 - **********
'''

def secure_name(name):
    return name[0] + '**'

def secure_on(no):
    return no[0:8] + '******'

def secure_phone(phone):
    return phone[0] + '****'
