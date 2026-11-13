
from hypothesis import given, strategies as st
import pytest

from food_delivery import parse_order, delivery_eta, coupon_discount


# ------------------------------------------------
# 1. FUZZ TESTING: parse_order()
# ------------------------------------------------

@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    try:
        result = parse_order(s)

    except ValueError:
        # Invalid input should be rejected cleanly
        return

    except Exception as e:
        pytest.fail(f"parse_order crashed with {type(e).__name__}: {e}")

    assert isinstance(result, dict)

    for name, qty in result.items():
        assert name.strip() != ""
        assert isinstance(qty, int)
        assert qty > 0


# ------------------------------------------------
# 2. FUZZ TESTING: delivery_eta()
# ------------------------------------------------

@given(st.text() | st.none())
def test_delivery_eta_no_crash(s):
    try:
        result = delivery_eta(s)

    except ValueError:
        # Invalid input should be rejected cleanly
        return

    except Exception as e:
        pytest.fail(f"delivery_eta crashed with {type(e).__name__}: {e}")

    assert isinstance(result, int)
    assert result >= 15


# ------------------------------------------------
# 3. FUZZ TESTING: coupon_discount()
# ------------------------------------------------

@given(st.text() | st.none())
def test_coupon_discount_no_crash(s):
    try:
        result = coupon_discount(s)

    except ValueError:
        # Invalid coupon should be rejected cleanly
        return

    except Exception as e:
        pytest.fail(f"coupon_discount crashed with {type(e).__name__}: {e}")

    normalized = s.upper()

    assert normalized.startswith("SAVE")
    assert normalized[4:].isdigit()
    assert result == int(normalized[4:])
    assert result >= 0
