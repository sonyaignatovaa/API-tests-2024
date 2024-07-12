import requests
from faker import Faker
faker = Faker()

URL = "https://restful-booker.herokuapp.com"


class TestCreateBooking:

    # positive test
    def test_create_booking_valid_data(self):
        """
        1. Try to book new customer
        2. Check that status code is 200
        """
        body = {"firstname": faker.first_name(),
                "lastname": faker.last_name(),
                "totalprice": faker.random_number(),
                "depositpaid": faker.boolean(),
                "bookingdates": {
                    "checkin": faker.date(),
                    "checkout": faker.date()
                },
                "additionalneeds": faker.sentence()}
        response_auth = requests.post(url=f'{URL}/booking', json=body)
        assert response_auth.status_code == 200

    # negative test
    def test_create_booking_invalid_username(self):
        """
        1. Try to book new customer with incorrect username (int instead of string)
        2. Check that status code is 500
        """
        body = {"firstname": 1,
                "lastname": faker.last_name(),
                "totalprice": faker.random_number(),
                "depositpaid": faker.boolean(),
                "bookingdates": {
                    "checkin": faker.date(),
                    "checkout": faker.date()
                },
                "additionalneeds": faker.sentence()}
        response_auth = requests.post(url=f'{URL}/booking', json=body)
        assert response_auth.status_code == 500
