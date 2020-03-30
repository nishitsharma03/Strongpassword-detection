import re

check=False
def passcheck():
    passw = input('Enter Password')
    lencheck=re.compile(r'(\w{8,})')
    lowercheck=re.compile(r'([a-z]+)')
    uppercheck=re.compile(r'([A-Z]+)')
    numcheck=re.compile(r'([0-9]+)')
    specialcharcheck=re.compile(r'([_&*%$+-.,;^#@!~/\{}])')
    if(lencheck.findall(passw)==[]):
        print('Password Must contain atleast 8 characters')
    elif(lowercheck.findall(passw)==[]):
        print('Password must have atleast 1 lowercase character')
    elif(uppercheck.findall(passw)==[]):
        print('Password must have atleast 1 uppercase character')
    elif(numcheck.findall(passw)==[]):
        print('Password must contain atleast 1 digit')
    elif(specialcharcheck.findall(passw)==[]):
        print('Password must have atleast one special character')
    else:
        global check
        check=True
        print('You have a strong password')
        return
while not check:
    passcheck()
    
        
    

