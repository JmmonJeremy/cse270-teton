import requests

def test_users_login_unauthorized(mocker):

    # Mock response object
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""

    # Mock requests.get to return the mock response
    mocker.patch("requests.get", return_value=mock_response)

    response = requests.get(
        "http://127.0.0.1:8000/users",
        params={
            "username": "admin",
            "password": "admin"
        }
    )

    # Verify expected result
    assert response.status_code == 401
    assert response.text.strip() == ""


def test_users_login_success(mocker):

    # Mock response object
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""

    # Mock requests.get
    mocker.patch("requests.get", return_value=mock_response)

    response = requests.get(
        "http://127.0.0.1:8000/users",
        params={
            "username": "admin",
            "password": "qwerty"
        }
    )

    # Verify expected result
    assert response.status_code == 200
    assert response.text.strip() == ""