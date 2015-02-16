spam = 42

def eggs():
    spam = 99 # Spam is local
    print('In eggs():', spam)

def ham():
    print('In ham():', spam) # Spam is global

def bacon():
    global spam # spam is global
    print('In bacon():', spam)
    spam = 0 

def crash():
    print(spam) # spam is local
    spam = 0

print(spam)
eggs()
print(spam)
ham()
print(spam)
bacon()
print(spam)
crash()
