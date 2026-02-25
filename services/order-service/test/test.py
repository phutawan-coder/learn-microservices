from unittest.mock import patch 
from main import create_order

@patch('main.request.get')
def test_creat_order(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "message": "ok"
    }

    result = create_order()

    assert result["message"] == "ok"

