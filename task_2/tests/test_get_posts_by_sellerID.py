import pytest
import requests

from ..data.configuration import SERVICE_URL, GET_POSTS_BY_SELLERID
from ..src.baseclasses.response import Response
from ..src.pydantic_shemas.shema_get_post_by_id import Post
from ..data.data_get_posts_by_sellerID import nonexistent_lover_threshold_sellerID, nonexistent_upper_threshold_sellerID, \
    existent_lover_threshold_sellerID, existent_upper_threshold_sellerID, data as expected_selerID_data, \
    headers as expected_response_headers, sellerID_for_tests
from ..data.injections_data import simplesql, dangersql, xss, path_traversal, command_injection


@pytest.mark.parametrize('expected_status_code, seller_id', [
    (200, existent_lover_threshold_sellerID),
    (200, existent_upper_threshold_sellerID),
])
def test_valid_status_code(expected_status_code, seller_id):
    r = requests.get(url=SERVICE_URL + seller_id + GET_POSTS_BY_SELLERID)
    response = Response(r)
    response.assert_status_code(expected_status_code)



@pytest.mark.parametrize('seller_id, time_out', [
    (existent_lover_threshold_sellerID, 1),
])
def test_response_take_in_time(seller_id, time_out):
    r = requests.get(url=SERVICE_URL + seller_id + GET_POSTS_BY_SELLERID, timeout=time_out)



@pytest.mark.parametrize('seller_id, expected_status_code', [
    (existent_lover_threshold_sellerID, 200),
])
def test_valid_data_model(seller_id, expected_status_code):
    r = requests.get(url=SERVICE_URL + seller_id + GET_POSTS_BY_SELLERID)
    response = Response(r)
    response.assert_status_code(expected_status_code).validate_list(Post)



@pytest.mark.parametrize('seller_id, selerID_data, expected_status_code', [
    (sellerID_for_tests, expected_selerID_data, 200),
])
def test_valid_response_data(seller_id, selerID_data, expected_status_code):
    r = requests.get(url=SERVICE_URL + seller_id + GET_POSTS_BY_SELLERID)
    response = Response(r)
    response.assert_status_code(expected_status_code).assert_response_data(selerID_data)



@pytest.mark.parametrize('seller_id, expected_headers, expected_status_code', [
    (existent_lover_threshold_sellerID, expected_response_headers, 200),
])
def test_valid_response_headers(seller_id, expected_headers, expected_status_code):
    r = requests.get(url=SERVICE_URL + seller_id + GET_POSTS_BY_SELLERID)
    response = Response(r)
    response.assert_status_code(expected_status_code).assert_response_headers(expected_headers)


@pytest.mark.parametrize('injection, expected_status_code', [
    (simplesql, 404),
    (dangersql, 404),
    (xss, 404),
    (path_traversal, 404),
    (command_injection, 404),
])
def test_injections(injection, expected_status_code):
    r = requests.get(url=SERVICE_URL + injection + GET_POSTS_BY_SELLERID)
    response = Response(r)
    response.assert_status_code(expected_status_code)
