email = input("Enter the email: ")
userID = email[0:email.index("@")]
user_Domain = email[email.index("@")+1:]
var = (f"The username is {userID} and domain name is {user_Domain}")
print(var)

# email = input("Enter Your Email: ").strip()
# username = email[:email.index("@")]
# domain_name = email[email.index("@")+1:]
# format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
# print(format_)