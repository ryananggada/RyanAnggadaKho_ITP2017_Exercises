guest_list = ["Devin", "Excel", "Nicolas", "Georgius", "Pier", "Fariz"]
print("Oh no! The large table is missing, I only have 2 spaces left.")
while len(guest_list) > 2:
    drop_guest = guest_list.pop()
    print("I'm sorry {}, I cannot invite you to the dinner.".format(drop_guest))
print(guest_list)
for i in range(2):
    print("{}, you are still invited to my party.".format(guest_list[i]))

print("")
del guest_list[1]
del guest_list[0]
print(guest_list)
print("All done!")
