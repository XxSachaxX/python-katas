from biller import bill

def test_biller_exists():
    assert callable(bill)
