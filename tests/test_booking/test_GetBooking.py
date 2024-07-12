import requests
from faker import Faker
faker = Faker()

URL = "https://restful-booker.herokuapp.com"


class TestGetBooking:

    # positive test
    def test_get_booking_valid_id(self):
        """
        1. Try to get booking with id = 1
        2. Check that status code is 200
        """
        id = 1
        response_auth = requests.get(url=f'{URL}/booking/{id}')
        assert response_auth.status_code == 200

    # negative test
    def test_get_booking_invalid_id(self):
        """
        1. Try to get booking with random id
        2. Check that status code is 404
        """
        id = faker.random_number()
        response_auth = requests.post(url=f'{URL}/booking/{id}')
        assert response_auth.status_code == 404
