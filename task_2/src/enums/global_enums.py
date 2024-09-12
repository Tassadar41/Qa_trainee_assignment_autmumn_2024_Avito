from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Recived status code is not equal to expected"
    NOT_EXPECTED_RESPONSE_DATA = "Recived not expected data in response"
    NOT_EXPECTED_HEADERS = "Recived headers not equal to expected"
    ID_NOT_UNIQUE = "New post id is not unique"
