#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""example.py
"""
from fullcontact import FullContactApi

api = FullContactApi(apikey="my api key")

email = "foo@bar.com"
person = api.person(email=email)
guess  = api.guess_name(email=email)
