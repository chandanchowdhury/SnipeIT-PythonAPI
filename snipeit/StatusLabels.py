import requests


class StatusLabels(object):
    """Class to access status labels API.
    """
    def __init__(self):
        pass

    def get(self, server, token, limit=None, order='asc', offset=None):
        """Get list of status labels.

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            order {string} -- Display order of data (asc / desc default:{asc})

        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})

        Returns:
            string -- list of status label in JSON format
        """
        if limit is not None:
            self.uri = '/api/v1/statuslabels?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/statuslabels?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, timeout=300,  headers=headers)
        return results.json()

    def search(self, server, token, limit=None, order='asc', keyword=None, offset=None):
        """Get list of statuslabels based on search keyword

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API

        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})

        Returns:
            string -- List of statuslabels in JSON format.
        """
        if keyword is None:
            keyword = ""

        if limit is not None:
            self.uri = '/api/v1/statuslabels?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/statuslabels?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))
        self.server = server + self.uri + '&search={0}'.format(keyword)
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, timeout=300,  headers=headers)
        return results.json()

    def create(self, server, token, payload):
        """Create new status label

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- input parameters

        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/statuslabels'
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.post(self.server, timeout=300,  headers=headers, data=payload)
        return results.json()

    def getDetailsByID(self, server, token, labelID):
        """Get detailed information of label by ID

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            labelID {string} -- ID of the label

        Returns:
            string -- Detailed information of label by ID
        """
        self.uri = '/api/v1/statuslabels/{0}'.format(labelID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, timeout=300,  headers=headers)
        return results.json()

    def getAssetListByID(self, server, token, labelID):
        """Get asset list based on label by ID

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            labelID {string} -- ID of the label

        Returns:
            string -- Detailed information of label by ID
        """
        self.uri = '/api/v1/statuslabels/{0}/assetlist'.format(labelID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, timeout=300,  headers=headers)
        return results.json()

    def delete(self, server, token, labelID):
        """[summary]

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            labelID {[type]} -- ID of the label

        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/statuslabels/{0}'.format(labelID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.delete(self.server, timeout=300,  headers=headers)
        return results.json()

    def update(self, server, token, labelID, payload):
        """[summary]

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            labelID {[type]} -- ID of the label
            payload {[type]} -- Input parameters

        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/statuslabels/{0}'.format(labelID)
        self.server = server + self.uri
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        results = requests.patch(self.server, timeout=300,  headers=headers, data=payload)
        return results.json()
