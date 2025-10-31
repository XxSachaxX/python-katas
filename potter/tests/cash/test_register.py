from potter.cash.register import Register

def test_has_cash_float():
    initial_cash_float = 20000
    initial_inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
        }
    }
    register = Register(initial_cash_float, initial_inventory)
    actual_cash_float = register.cash_float

    assert actual_cash_float == 20000, f"Expected register to have cash float {initial_cash_float}, but has {actual_cash_float}"

def test_has_inventory():
    initial_inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
        }
    }

    initial_cash_float = 20000
    register = Register(initial_cash_float, initial_inventory)
    actual_inventory = register.inventory

    assert actual_inventory == initial_inventory, f"Expected inventory: {initial_inventory}, got: {actual_inventory}"
