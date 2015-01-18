#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""fullcontactapi.py
read the FullContact API docs here:
    • http://www.fullcontact.com/developer/docs/
"""
import json
import requests

class ValidationError(Exception):
    def __init__(self, message, errors):
        Exception.__init__(self, message)
        self.errors = errors

class AuthenticationError(Exception):
    def __init__(self, message, errors):
        Exception.__init__(self, message)
        self.errors = errors

class FullContactApi(object):
    BASE_URI = "https://api.fullcontact.com/{version}/{endpoint}.json"
    ENDPOINTS = ["person", "name/deducer"]
    VERSIONS = ["v2"]

    def __init__(self, username=None, apikey=None):
        super(FullContactApi, self).__init__()
        self.authenticate(username, apikey)
        self.last_url = None
        self.last_status_code = None
        self.last_headers = None
        self.last_response = None

    def __str__(self):
        return "FullContactApi(username, apikey)"

    def __repr__(self):
        return self.__str__()

    def authenticate(self, username=None, apikey=None):
        self._username = username
        self._apikey   = apikey

    def _uri_for(self, entity_type, version="v2"):
        if version and version in self.VERSIONS:
            if entity_type and entity_type in self.ENDPOINTS:
                return self.BASE_URI.format(version=version, endpoint=entity_type)
            else:
                msg = "Unknown or invalid resource: {}".format(entity_type)
                raise ValidationError(message=msg, errors={"endpoint": entity_type})
        else:
            print 'got here'
            msg = "Unknown or invalid version: {}".format(version)
            raise ValidationError(message=msg, errors={"version": version})

    def _call_get(self, url, query={}):
        self.last_url = url
        try:
            r = requests.get(url, params=query)
            self.last_headers = r.headers
            self.last_status_code = r.status_code
            self.last_url = r.url
            self.last_response = r
            return r.json()
        except Exception, err:
            msg = "Something went wrong\n\nCALLING:\n\t'{}'\nPARAMS:\n\t`{}`"
            msg = msg.format(url, query) + "\n" + err
            print >> sys.stderr, msg
            return {}

    def _authenticate_query(self, query):
        if self._apikey is None:
            msg ="Invalid or missing API key!"
            raise AuthenticationError(message=msg, errors={})
        query.update({"apiKey": self._apikey})
        return query

    def get(self, entity_type, query={}):
        url = self._uri_for(entity_type)
        query = self._authenticate_query(query)
        return self._call_get(url, query)

    def person(self, email):
        """lookup a person record using a known email address
        args:
            email: a known email
        """
        query = {"email": email}
        return self.get("person", query)

    def guess_name(self, email=None, username=None, casing="titlecase"):
        """deduce first and last name using a known email addr.
        Uses FullContact's Name Deducer API. Takes a username or email address provided 
        as a string and attempts to deduce a structured name. It also returns a 
        likelihood based on US population data. This method is ideal for business 
        email addresses due to the use of standard convention in corporate email
        address formats.
        """
        query = {}
        if email:
            query["email"] = email
            if username:
                msg = "Choose email or username but not both...\n using email...{}"
                print >> sys.stdout, msg.format(query)
        elif username:
            query["username"] = username
        else:
            msg = "Either email or username is required. Neither provided."
            errs = {"email": email, "username": username, "titlecase": titlecase}
            raise ValidationError(message=msg, errors=errs)
        if casing and casing in ["uppercase", "lowercase", "titlecase"]:
            query["casing"] = casing
        return self.get("name/deducer", query=query)
