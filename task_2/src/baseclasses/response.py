from ..enums.global_enums import GlobalErrorMessages

class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_headers = response.headers
        self.response_status = response.status_code

    def validate_data_model(self, shema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                shema.model_validate(item)
        else:
            shema.model_validate(self.response_json)

    def validate_list(self, shema):
        for obj in self.response_json:
            shema.model_validate(obj)


    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def assert_response_data(self, expected_data):
        assert self.response_json == expected_data, GlobalErrorMessages.NOT_EXPECTED_RESPONSE_DATA.value
        return self

    def assert_response_headers(self, expected_headers):
        for key, value in expected_headers.items():
            assert self.response_headers[key] == value, GlobalErrorMessages.NOT_EXPECTED_HEADERS.value
        return self

