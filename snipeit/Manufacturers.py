import requests


class Manufacturers(object):
    def __init__(self):
        """Class to access manufacturers API.
        """
        pass

    def get(self, server, token):
        """Get list of manufacturers

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API

        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})

        Returns:
            string -- List of manufacturers in JSON format.
        """
        self.uri = '/api/v1/manufacturers'
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, timeout=300,  headers=headers)
        return results.json()

    def create(self, server, token, payload):
        """Create new manufacturers data.

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Input parameters

        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/manufacturers'
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.post(self.server, timeout=300,  headers=headers, data=payload)
        return results.json()

    def getDetailsByID(self, server, token, manufacturersID):
        """Get detailed information of label by ID

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            manufacturersID {string} -- ID of the manufacturers

        Returns:
            string -- Detailed information of manufacturers by ID
        """
        self.uri = '/api/v1/manufacturers/{0}'.format(manufacturersID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, timeout=300,  headers=headers)
        return results.json()

    def delete(self, server, token, manufacturersID):
        """Delete manufacturers data

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            manufacturersID {string} -- ID of the manufacturers

        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/manufacturers/{0}'.format(manufacturersID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.delete(self.server, timeout=300,  headers=headers)
        return results.json()

    def update(self, server, token, manufacturersID, payload):
        """[summary]

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            manufacturersID {string} -- ID of the manufacturers
            payload {string} -- Input parameters

        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/manufacturers/{0}'.format(manufacturersID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.patch(self.server, timeout=300,  headers=headers, data=payload)
        return results.json()
