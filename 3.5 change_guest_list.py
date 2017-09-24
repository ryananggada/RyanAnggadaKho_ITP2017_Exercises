guest_list = ["Excel", "Georgius", "Diwa"]
print("Diwa can't make it to the dinner, I'm gonna replace him with Pier.")
guest_list.remove("Diwa")
guest_list.append("Pier")
print(guest_list)


print("This is the new invitation down here.")
for i in range(3):
    print("{}, you are invited to the dinner!".format(guest_list[i]))
