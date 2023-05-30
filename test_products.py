import json
import pytest
from parameterized import parameterized
from cerberus import Validator
from assertpy import assert_that


AUTH_TOKEN = 'generated_auth_token'
BAD_AUTH_TOKEN = 'bad_generated_auth_token'

#
# This test case covers the basic response from successfully receiving a valid response from the endpoint.
# It builds a schema, then validates it against the returns response bodys schema.
#
# The schema building/validation is done using the cerberus library.
#
@pytest.mark.development
def test_response_body(get_response_body):
    # Arrange
    schema = {
        'products':{
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'id': {'type':'integer'}, 
                    'name': {'type':'string'}, 
                    'category': {'type':'string'}, 
                    'price': {'type':'float'}, 
                    'in_stock': {'type':'boolean'}
                }
            }
        }
    }
    v = Validator(schema)

    # Act
    # Using the fixture to return the json data rather than requests since there is no real endpoint.
    #r = requests.get('/products', headers={'Authorization': AUTH_TOKEN})
    r = get_response_body

    # Assert
    is_valid = v.validate(r)
    #is_valid = v.validate(r.json())                    In a normal api response, would pull out the json return to compare against
    #asset_that(r.status_code() == 200).is_true()       Here the status code is checked, commented out since using dummy api request
    assert_that(is_valid).is_true()


#
# This test case will not pass since there is no endpoint to reach, but it outlines the basic idea of how I would go about testing a 400 error.
#
@pytest.mark.broken
def test_bad_request(get_response_body):
    # Arrange

    # Act
    r = requests.get('/products', headers={'Authorization': AUTH_TOKEN})

    # Assert
    assert_that(r.status_code() == 400).is_true()


#
# This test case will not pass since there is no endpoint to reach, but it outlines the basic idea of how I would go about testing a 401 error.
#
@pytest.mark.broken
def test_unauthorized_request(get_response_body):
    # Arrange

    # Act
    r = requests.get('/products', headers={'Authorization': BAD_AUTH_TOKEN})

    # Assert
    assert_that(r.status_code() == 401).is_true()
    