import pytest
import json
import requests

@pytest.fixture
def get_response_body():
    response_json = {
        "products": [
            {"id":1, "name":"Product A", "category":"Electronics", "price":99.99, "in_stock":True},
            {"id":2, "name":"Product B", "category":"Books", "price":14.99, "in_stock":False},
            {"id":3, "name":"Product C", "category":"Electronics", "price":199.99, "in_stock":True}
        ]
    }
    return response_json