from requ import Sheety

user_post = Sheety()
print(
  "Welcome to the Flight Club!\nWe find the best flight deals and email you.")
first = input("What is your first name?\n").title()
last = input("What is your last name?\n").title()
email = input("What is your email?\n").lower()
again = input("Type your email again?\n")
if email == again:
  print("You are in the club!")
  user_post.post_users(first=first, last=last, email=email)
else:
  print("Email doesn't match!")
