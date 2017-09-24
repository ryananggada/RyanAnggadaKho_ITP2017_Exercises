username = ["tynamo", "admin", "pewdiepie", "eric", "penne"]
for user in username:
    if "admin" in user:
        print("Hello {}, would you like to see a status report?".format(user))
    else:
        print("Hello {}, welcome back.".format(user))
