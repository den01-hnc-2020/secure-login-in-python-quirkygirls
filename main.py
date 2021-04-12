import users

def prompt_register():
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")

  users.add_user(username, password)

def prompt_login():
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")

  users.check_user(username, password)

def main():

  while True:
    choice = input("Welcome to my site. Please choose from the following options:\n\n[1] Register\n[2] Login\n\nEnter selection: ")

    if choice == "1":
      prompt_register()
      break
    elif choice == "2":
      prompt_login()
      break
    else:
      print("Sorry. I didn't quite catch that. Please enter [1] or [2].")
      
if __name__ == '__main__':
  main()
