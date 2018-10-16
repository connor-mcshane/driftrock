from src.driftrock_api import DriftRockAPI
from src.models import User, Purchase

import pytest

import httpretty
import requests
import json


@httpretty.activate
def test_get_request():
    """
    Ensure that _get_request() properly handles http requets. Ideally more cases would
    be explored (i.e exceptions being raised etc)
    """

    resp_body = json.dumps({"status":"ok"})
    httpretty.register_uri(httpretty.GET, DriftRockAPI.BASE_URL + "status", body=resp_body, status=200)
    api_handle = DriftRockAPI()

    response = api_handle._get_request("status")
    assert response["status"]


@httpretty.activate
def test_resource_status_not_ok():
    """
    Mock the GET uri and ensure that method under test returns the correct boolean
    """

    api_handle = DriftRockAPI()

    resp_body = json.dumps({"status":"ok"})
    httpretty.register_uri(httpretty.GET, DriftRockAPI.BASE_URL + "status", body=resp_body, status=200)
    status_not_ok = api_handle.resource_status_not_ok()
    assert status_not_ok == False 

    resp_body = json.dumps({"status":"not ok"})
    httpretty.register_uri(httpretty.GET, DriftRockAPI.BASE_URL + "status", body=resp_body, status=200)
    status_not_ok = api_handle.resource_status_not_ok()
    assert status_not_ok == True 


@httpretty.activate
def test_get_all_users():
    """
    Mock the GET uri, ensure correct Users are returned
    """

    api_handle = DriftRockAPI()
    user1_dict = {"id":"slim-shady", "email":"slim@mail.com"}
    user2_dict = {"id":"stock-shady", "email":"stock@mail.com"}

    resp_body = json.dumps({"data": [user1_dict, user2_dict]})

    httpretty.register_uri(httpretty.GET, DriftRockAPI.BASE_URL + "users", body=resp_body, status=200)
    user_list = api_handle.get_all_users()
    assert isinstance(user_list, list)
    assert user_list[0].id == "slim-shady"
    assert user_list[0].email == "slim@mail.com"
    assert user_list[1].id == "stock-shady"
    assert user_list[1].email == "stock@mail.com"


@httpretty.activate
def test_get_all_purchases():
    """
    Mock the GET uri, ensure correct Purchases are returned
    """

    api_handle = DriftRockAPI()

    purchase1_dict = {"user_id":"slim-shady",  "item": "hoodie", "spend": 20}
    purchase2_dict = {"user_id":"stock-shady",  "item": "hoodie", "spend": 20}
    resp_body = json.dumps({"data": [purchase1_dict, purchase2_dict]})

    httpretty.register_uri(httpretty.GET, DriftRockAPI.BASE_URL + "purchases", body=resp_body, status=200)
    purchase_list = api_handle.get_all_purchases()

    assert isinstance(purchase_list, list)
    assert purchase_list[0].user_id == "slim-shady"
    assert purchase_list[0].item == "hoodie"
    assert purchase_list[0].spend == 20
    assert purchase_list[1].user_id == "stock-shady"
    assert purchase_list[1].item == "hoodie"
    assert purchase_list[1].spend == 20

