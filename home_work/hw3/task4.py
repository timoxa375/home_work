mess = input("Please, enter your message:")
list(mess)
if "Mr./Mrs." in mess:
    print("Gender is male")
elif "Miss/Ms." in mess:
    print("Gender is female")
else:
    print("No gender!")