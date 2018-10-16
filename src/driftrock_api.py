import requests
import sys
from src.models import User, Purchase


class DriftRockAPI(object):
    """
    Wrapper class, a class was used to so the session() object could be 
    shared between method invocations.
    """

    BASE_URL = "https://driftrock-dev-test.herokuapp.com/"

    def __init__(self):
        self.session = requests.session()

    def _get_request(self, endpoint):
        """
        Make an API request and do some basic error checking, returns a 
        json object
        """
        try:
            response = self.session.get(self.BASE_URL + endpoint, timeout=10)
            response.raise_for_status()
            response_json = response.json()

        except (requests.exceptions.HTTPError, ValueError) as error:
            print(error)
            sys.exit(1)

        return response_json

    def resource_status_not_ok(self):
        """
        Query the status of the API, returns a boolean
        """

        response_json = self._get_request("status")

        return response_json["status"] != "ok"

    def get_all_users(self):
        """
        Return a list of User objects from the API
        """
        response_json = self._get_request("users")

        user_list = [
            User(entry["id"], entry["email"])
            for entry in response_json["data"]
        ]

        return user_list

    def get_all_purchases(self):
        """
        Return a list of Purchases from the API
        """
        response_json = self._get_request("purchases")

        purchase_list = [Purchase(entry["user_id"], entry["item"], entry["spend"]) \
                         for entry in response_json["data"]]

        return purchase_list
