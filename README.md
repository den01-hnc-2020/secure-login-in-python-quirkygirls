# Secure Login in Python

## Step 1 - Running the script

- To run this script, click the 'Work in Repl.it' button above to open the Repl.it IDE. _**Note**: Make sure you sign into Repl first, as there can sometimes be bugs if you access it the other way around._

- Once you are in the Repl.it IDE, press 'Run' at the top of the screen to run the program. 
 
In its current state, this program takes allows a user to 'register' using a username and password, then stores those credentials in a database. **No attempt** is made to obscure or hide the login details, and as such the code is completely insecure.

## Step 2 - Improving security (I)

The first step in securing our login procedure is to hide the password from view when we type it in. There are a few ways of doing this, the most common of which on command-line applications is to obscure it completely, so it looks like you're not even typing. This is the standard practice on the Linux terminal and it's what we're going to implement below. You will only be making changes to `main.py` in this section and we will be using the `getpass` Python library. You can read more about `getpass` [here](https://docs.python.org/3/library/getpass.html).

- Open `main.py` and insert the line `from getpass import getpass` at the top of the file.

- Replace the lines where the password is obtained with the correct syntax for `getpass`.

## Step 3 - Improving security (II)

The next step in securing our login procedure is to hide the password details when stored in the server. Passwords should _**never**_ be stored in plaintext and any attempt to do so is likely to end in disaster. Any unauthorised access to your server would mean that user passwords would be exposed! We can circumvent this via a process known as _hashing_ and _salting_. You can read more about this process [here](https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/).

This process is highly mathematical and can get quite confusing, but luckily Python has a few functions that will be able to help us out. The main library we will be using is `hashlib` ([see more](https://docs.python.org/3/library/hashlib.html)) and we will also make use of the `os` library, allowing us to access system prompts and the `binascii` library, allowing us to convert between binary and ascii. You can read more about that library [here](https://docs.python.org/3/library/binascii.html).

- Open `users.py` and insert the line `import hashlib, os, binascii` at the top of the file.

- Create a function called `hash_password()` and call it inside the `add_user()` function, replacing the line `db[username] = password`.

- Populate your new `hash_password()` function with the following:

```
salt = hashlib.sha256(os.urandom(32)).hexdigest().encode('ascii')
key = binascii.hexlify(hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000))

return (salt + key).decode('ascii')
```

- Fix the `check_user()` function so that it uses the new `salt` and `key` compbinations to check the inputted password. You may find [this example](https://gist.github.com/aharshbe/1ace2086b7ebe4e99a29d02e7fe83b74) helpful.

- Check your final code works by registering a user and attempting to login. 

## Step 4 - Over to you

Please feel free to continue to edit the code and improve its usability and security. 

There are plenty of additional things you could try to implement, including wrapping the script in a Flask server, checking for multiple login attempts and a facility to reset a password. What else can you make this code do?

## Contact

Any questions or issues can be raised via the [Github issues](https://github.com/den01-hnc-2020/python-login/issues) pages.

## License 

Copyright Scott Morgan (2021). Released under the [MIT License](https://opensource.org/licenses/MIT).
