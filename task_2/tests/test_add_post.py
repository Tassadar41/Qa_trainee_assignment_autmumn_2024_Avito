import pytest
import requests
import re

from ..data.configuration import SERVICE_URL, ADD_POST, GET_POSTS_BY_SELLERID
from ..src.baseclasses.response import Response
from ..src.pydantic_shemas.shema_add_post import AddPost
from ..data.data_add_post import headers as expected_response_headers, sellerID_for_tests
from ..data.injections_data import simplesql, dangersql, xss, path_traversal, command_injection, json_injection
from ..src.baseclasses.post import post_add_obj
from ..src.enums.global_enums import GlobalErrorMessages


@pytest.mark.parametrize('expected_status_code, name, price, sellerId, contacts, like, view_count', [
    (200, "Phone", 777, 111111, 32, 35, 14),
    (200, "Phone", 777, 999999, 32, 35, 14),
    (400, "Phone", 777, 1000000, 32, 35, 14),
    (400, "Phone", 777, 111110, 32, 35, 14)
])
def test_valid_status_code(expected_status_code, name, price, sellerId, contacts, like, view_count):
    data = post_add_obj(name, price, sellerId, contacts, like, view_count)
    r = requests.post(url=SERVICE_URL + ADD_POST, json=data)
    response = Response(r)
    response.assert_status_code(expected_status_code)


@pytest.mark.parametrize('time_out, name, price, sellerId, contacts, like, view_count', [
    (1, "Phone", 777, sellerID_for_tests, 32, 35, 14),
])
def test_response_take_in_time(time_out, name, price, sellerId, contacts, like, view_count):
    data = post_add_obj(name, price, sellerId, contacts, like, view_count)
    r = requests.post(url=SERVICE_URL + ADD_POST, json=data, timeout=time_out)


@pytest.mark.parametrize('name, price, sellerId, contacts, like, view_count, expected_status_code', [
    ("Phone", 777, sellerID_for_tests, 32, 35, 14, 200),
])
def test_valid_data_model(name, price, sellerId, contacts, like, view_count, expected_status_code):
    data = post_add_obj(name, price, sellerId, contacts, like, view_count)
    r = requests.post(url=SERVICE_URL + ADD_POST, json=data)
    response = Response(r)
    response.assert_status_code(expected_status_code).validate_data_model(AddPost)


@pytest.mark.parametrize('name, price, sellerId, contacts, like, view_count, expected_headers, expected_status_code', [
    ("Phone", 777, sellerID_for_tests, 32, 35, 14, expected_response_headers, 200),
])
def test_valid_response_headers(name, price, sellerId, contacts, like, view_count, expected_headers, expected_status_code):
    data = post_add_obj(name, price, sellerId, contacts, like, view_count)
    r = requests.post(url=SERVICE_URL + ADD_POST, json=data)
    response = Response(r)
    response.assert_status_code(expected_status_code).assert_response_headers(expected_headers)


@pytest.mark.parametrize('name, price, sellerId, contacts, like, view_count, expected_status_code', [
    (simplesql, 777, sellerID_for_tests, 32, 35, 14, 404),
    (dangersql, 777, sellerID_for_tests, 32, 35, 14,  404),
    (xss, 777, sellerID_for_tests, 32, 35, 14, 404),
    (path_traversal, 777, sellerID_for_tests, 32, 35, 14, 404),
    (command_injection, 777, sellerID_for_tests, 32, 35, 14, 404),
])
def test_injections(name, price, sellerId, contacts, like, view_count, expected_status_code):
    data = post_add_obj(name, price, sellerId, contacts, like, view_count)
    r = requests.post(url=SERVICE_URL + ADD_POST, json=data)
    response = Response(r)
    response.assert_status_code(expected_status_code)

@pytest.mark.parametrize('json, expected_status_code', [
    (json_injection, 404),
])
def test_json_injections(json, expected_status_code):
    r = requests.post(url=SERVICE_URL + ADD_POST, json=json)
    response = Response(r)
    response.assert_status_code(expected_status_code)
    

@pytest.mark.parametrize('name, price, sellerId, contacts, like, view_count, expected_status_code', [
    ("Phone", "test", "test", 0, 0, 0, 400),
    ("Phone", 856, 855677, -1, -1, -1, 400),
    ("Phone", "test", "test", "text", "text", "text", 400),
    ("12345", "test", 855677, "text", 15, 6, 400),
    ("12345", "test", 855677, 32, 0, -1, 400),
    ("12345", 856, 855677, 0, -1, "text", 400),
    ("12345", 856, "test", -1, "text", 6, 400),
    ("Phone", 856, 855677, 0, "text", 6, 400),
    ("Phone", "test", 855677, -1, 15, 0, 400),
    ("Phone", 856, "test", "text", 15, -1, 400),
    ("Phone", 856, 855677, 32, 0, "text", 400),
    ("12345", "test", "test", 32, -1, 6, 400),
    ("12345", 856, 855677, 32, "text", 0, 400),
    ("12345", 856, "test", 0, 15, -1, 400),
    ("12345", "test", 855677, -1, 15, "text", 400),
    ("12345", 856, 855677, "text", 0, 6, 400),
    ("Phone", 856, "test", -1, 0, 6, 400),
    ("Phone", 856, 855677, "text", -1, 0, 400),
    ("Phone", "test", 855677, 32, "text", -1, 400),
    ("Phone", 856, "test", 32, 15, "text", 400),
    ("Phone", "test", 855677, 0, 15, 6, 400),
])
def test_pairwaise_add_post(name, price, sellerId, contacts, like, view_count, expected_status_code):
    data = post_add_obj(name, price, sellerId, contacts, like, view_count)
    r = requests.post(url=SERVICE_URL + ADD_POST, json=data)
    response = Response(r)
    response.assert_status_code(expected_status_code)

