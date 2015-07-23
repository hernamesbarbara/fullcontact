## Python Wrapper for FullContact API

* https://www.fullcontact.com/developer/docs/

```python
from fullcontact import FullContactApi

api = FullContactApi(apikey="my api key")

email = "foo@bar.com"
person = api.person(email=email)
guess  = api.guess_name(email=email)
```

### Installation

```
cd ~/Desktop
git clone git@github.com:hernamesbarbara/fullcontact.git
cd fullcontact
pip install .
```

### Command Line

Configure FullContact on your machine by passing your username and apikey to the CLI one time. Save your username and apikey in a json file like this:

```
# ~/Desktop/full_contact.json
{"username": "foo@bar.com", "apikey": "my api key"}
```

Now run a query and pass in your api key json file. You'll only do this once.

```
fullcontact travis@fullcontact.com --secrets-file ~/Desktop/full_contact.json
```

Your credentials will be automatically saved to a dotfile in your home directory here:

```
~/.full_contact_secrets
```

You can delete the `--secrets-file` (`full_contact.json` if you followed the above exactly).

Now you can use `fullcontact` CLI without authentication.

```
fullcontact travis@fullcontact.com
```



