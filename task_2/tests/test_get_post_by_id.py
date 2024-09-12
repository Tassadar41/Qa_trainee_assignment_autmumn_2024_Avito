import pytest
import requests

from ..data.configuration import SERVICE_URL, GET_POST_BY_ID
from ..src.baseclasses.response import Response
from ..src.pydantic_shemas.shema_get_post_by_id import Post
from ..data.data_get_post_by_id import data as expected_post_data, headers as expected_response_headers, correct_post_id, \
    wrong_post_id
from ..data.injections_data import simplesql, dangersql, xss, path_traversal, command_injection


@pytest.mark.parametrize('expected_status_code, post_id', [
    (200, correct_post_id),
    (404, wrong_post_id)
])
def test_valid_status_code(expected_status_code, post_id):
    r = requests.get(url=SERVICE_URL + GET_POST_BY_ID + post_id)
    response = Response(r)
    response.assert_status_code(expected_status_code)



@pytest.mark.parametrize('post_id, time_out', [
    (correct_post_id, 1),
])
def test_response_take_in_time(post_id, time_out):
    r = requests.get(url=SERVICE_URL + GET_POST_BY_ID + post_id, timeout=time_out)



@pytest.mark.parametrize('post_id, expected_status_code', [
    (correct_post_id, 200),
])
def test_valid_data_model(post_id, expected_status_code):
    r = requests.get(url=SERVICE_URL + GET_POST_BY_ID + post_id)
    response = Response(r)
    response.assert_status_code(expected_status_code).validate_data_model(Post)



@pytest.mark.parametrize('post_id, post_data, expected_status_code', [
    (correct_post_id, expected_post_data, 200),
])
def test_valid_response_data(post_id, post_data,expected_status_code):
    r = requests.get(url=SERVICE_URL + GET_POST_BY_ID + post_id)
    response = Response(r)
    response.assert_status_code(expected_status_code).assert_response_data(post_data)



@pytest.mark.parametrize('post_id, expected_headers, expected_status_code', [
    (correct_post_id, expected_response_headers, 200),
])
def test_valid_response_headers(post_id, expected_headers, expected_status_code):
    r = requests.get(url=SERVICE_URL + GET_POST_BY_ID + post_id)
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
    r = requests.get(url=SERVICE_URL + GET_POST_BY_ID + injection)
    response = Response(r)
    response.assert_status_code(expected_status_code)
