f = open("input.txt", "r")
emails = f.read()

emails = emails.split(";")

for email in emails:
    print (email)