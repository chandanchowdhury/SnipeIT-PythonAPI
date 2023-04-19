import requests


class Fieldsets(object):
    def __init__(self):
        pass

    def get(self, server, token):
        """Get list of fieldsets

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API

        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})

        Returns:
            string -- List of fieldsets in JSON format.
        """
        self.uri = '/api/v1/fields'
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, timeout=300,  headers=headers)
        return results.json()

    def create(self, server, token, payload):
        """Create new fieldsets data.

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Input parameters

        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/fieldsets'
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.post(self.server, timeout=300,  headers=headers, data=payload)
        return results.json()

    def getDetailsByID(self, server, token, fieldsetsID):
        """Get detailed information of label by ID

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            fieldsetsID {string} -- ID of the fieldsets

        Returns:
            string -- Detailed information of fieldsets by ID
        """
        self.uri = '/api/v1/fieldsets/{0}'.format(fieldsetsID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, timeout=300,  headers=headers)
        return results.json()

    def delete(self, server, token, fieldsetsID):
        """Delete fieldsets data

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            fieldsetsID {string} -- ID of the fieldsets

        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/fieldsets/{0}'.format(fieldsetsID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.delete(self.server, timeout=300,  headers=headers)
        return results.json()

    def updatefieldsets(self, server, token, fieldsetsID, payload):
        """[summary]

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            fieldsetsID {string} -- ID of the fieldsets
            payload {string} -- Input parameters

        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/fieldsets/{0}'.format(fieldsetsID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.patch(self.server, timeout=300,  headers=headers, data=payload)
        return results.json()
