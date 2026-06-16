from datetime import date
import pytest
import sys
from seasons import calculate_minutes, minutes_to_words


def test_calculate_minutes():
    # Setting a rigid target date for testing consistency (e.g., 2020-01-01)
    target_today = date(2020, 1, 1)

    # Exactly 1 year prior (365 days because 2019 wasn't a leap year)
    # 365 * 24 * 60 = 525,600
    assert calculate_minutes("2019-01-01", target_today) == 525600

    # Exactly 2 years prior (2019 had 365 days, 2018 had 365 days)
    # 730 * 24 * 60 = 1,051,200
    assert calculate_minutes("2018-01-01", target_today) == 1051200


def test_minutes_to_words():
    # Test typical structure constraints (Capitalized start, no "and")
    assert (
        minutes_to_words(525600)
        == "Five hundred twenty-five thousand six hundred minutes"
    )
    assert (
        minutes_to_words(1051200)
        == "One million fifty-one thousand two hundred minutes"
    )


def test_invalid_date_format():
    # Verify that an invalid ISO format structure triggers a system exit
    with pytest.raises(SystemExit):
        calculate_minutes("January 1, 2020", date(2020, 1, 1))
    with pytest.raises(SystemExit):
        calculate_minutes("2020-12-32", date(2020, 1, 1))
