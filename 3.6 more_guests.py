guest_list = ["Excel", "Georgius", "Pier"]
print("I have found a bigger table, it's time to invite more 3 people.")
guest_list.insert(0, "Devin")
guest_list.insert(2, "Nicolas")
guest_list.append("Fariz")
print(guest_list)
print("Invitation ready!")
for i in range(6):
    print("{}, you are invited to the dinner!".format(guest_list[i]))
