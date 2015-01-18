## Python Wrapper for FullContact API

* https://www.fullcontact.com/developer/docs/

```python
from fullcontact import FullContactApi

api = FullContactApi(apikey="my api key")

email = "foo@bar.com"
person = api.person(email=email)
guess  = api.guess_name(email=email)
```

