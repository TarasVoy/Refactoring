import pytest
from order_system.facade import OrderProcessor

def test_physical_order():
    processor = OrderProcessor("physical")
    result = processor.process_order("123")
    assert result == "Shipping physical item #123"

def test_digital_order():
    processor = OrderProcessor("digital")
    result = processor.process_order("456")
    assert result == "Sending download link for item #456"

def test_invalid_order_type():
    with pytest.raises(ValueError):
        OrderProcessor("invalid")