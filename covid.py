age = input("Are you a cigarette addict older than 75 years old? Yes or No :").lower()
chronic = input("Do you have a severe chronic disease? Yes or No :").lower()
imnune = input("Is your immune system too weak? Yes or No :").lower()
risk = age == "yes" or chronic == "yes" or imnune == "yes"
if risk == True:
    print("You are in riskly group")
else:
    print("You are not in riskly group")
