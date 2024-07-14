import requests
from faker import Faker
faker = Faker()


class TestAuth:

    # positive test
    def test_auth_valid_data(self, url):
        """
        1. Try to get auth token with default data
        2. Check that response contains token
        """
        body = {"username": "admin",
                "password": "password123"}
        response_auth = requests.post(url=f'{url}/auth', json=body)
        assert "token" in response_auth.text

    # negative test
    def test_auth_invalid_data(self, url):
        """
        1. Try to get auth token with random data
        2. Check that response contains text "Bad credentials"
        """
        body = {"username": faker.user_name(),
                "password": faker.password()}
        response_auth = requests.post(url=f'{url}/auth', json=body)
        assert "Bad credentials" in response_auth.text
