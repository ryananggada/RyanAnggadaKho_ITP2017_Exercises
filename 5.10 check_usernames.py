current_users = ["tynamo", "excel", "peter", "john", "penne"]
new_users = ["asdf", "ExCel", "anna", "azer", "joHn"]
for user in new_users:
    if user.lower() in current_users:
        print("{} is not available.".format(user))
    else:
        print("{} is available.".format(user))
