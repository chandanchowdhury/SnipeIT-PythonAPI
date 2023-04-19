import requests


class Company(object):
    """Class to access Companies API
    """
    def __init__(self):
        pass

    def get(self, server, token):
        """Gets company list

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API

        Returns:
            string -- List of companies from the server, in JSON formatted
        """
        self.uri = '/api/v1/companies'
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, timeout=300,  headers=headers)
        return results.content

    def create(self, server, token, payload):
        """Create new company data.

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Company Name

        Returns:
            string -- Status data from the server, in JSON formatted
        """
        self.uri = '/api/v1/companies'
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.post(self.server, timeout=300,  headers=headers, data=payload)
        return results.json()

    def getDetailsByID(self, server, token, companiesID):
        """Gets company details by ID

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            companiesID {[type]} -- [description]

        Returns:
            string -- Detailed information of company from the server, in JSON formatted
        """
        self.uri = '/api/v1/companies/{0}'.format(str(companiesID))
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, timeout=300,  headers=headers)
        return results.json()

    def delete(self, server, token, CompanyID):
        """Delete company information

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            CompanyID {[type]} -- [description]

        Returns:
            string -- Response message from the server, in JSON formatted
        """
        self.uri = '/api/v1/companies/{0}'.format(CompanyID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.delete(self.server, timeout=300,  headers=headers)
        return results.json()

    def updateCompany(self, server, token, CompanyID, payload):
        """Updates company name.

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            CompanyID {string} -- ID of company to be updated
            payload {string} -- Company name to be updated

        Returns:
            string -- Response message from the server, in JSON formatted
        """
        self.uri = '/api/v1/companies/{0}'.format(CompanyID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.patch(self.server, timeout=300,  headers=headers, data=payload)
        return results.json()
