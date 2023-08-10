password = input("What's the password : ")
secret = "i see dead people"
while True:
    if password == secret:
        break
    password = input("What's the password : ")
print ("You've successfully left the loop.")