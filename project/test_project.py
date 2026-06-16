import os
import pytest
from project import add_transaction, calculate_balance, get_category_total, export_csv


@pytest.fixture
def sample_transactions():
    """Provides a fresh setup of transactions for testing."""
    return [
        {"type": "income", "amount": 2000.0, "category": "Salary", "date": "2026-06-01"},
        {"type": "expense", "amount": 50.0, "category": "Food", "date": "2026-06-02"},
        {"type": "expense", "amount": 120.0, "category": "Utilities", "date": "2026-06-03"},
        {"type": "expense", "amount": 30.0, "category": "Food", "date": "2026-06-04"}
    ]


def test_add_transaction():
    empty_list = []
    updated_list = add_transaction(empty_list, "income", 150.75, "Freelance", "2026-06-05")

    assert len(updated_list) == 1
    assert updated_list[0]["type"] == "income"
    assert updated_list[0]["amount"] == 150.75
    assert updated_list[0]["category"] == "Freelance"


def test_calculate_balance(sample_transactions):
    balance, income, expenses = calculate_balance(sample_transactions)
    # 2000 - (50 + 120 + 30) = 1800
    assert balance == 1800.0
    assert income == 2000.0
    assert expenses == 200.0


def test_get_category_total(sample_transactions):
    # Standard check
    assert get_category_total(sample_transactions, "Food") == 80.0
    assert get_category_total(sample_transactions, "Salary") == 2000.0
    # Case insensitivity check
    assert get_category_total(sample_transactions, "food") == 80.0
    # Non-existent category check
    assert get_category_total(sample_transactions, "Entertainment") == 0.0


def test_export_csv(sample_transactions):
    test_filename = "test_output.csv"

    # Assert successful write execution flags True
    assert export_csv(sample_transactions, test_filename) is True
    assert os.path.exists(test_filename) is True

    # Clean up the created test file after confirmation
    if os.path.exists(test_filename):
        os.remove(test_filename)

    # Assert empty list returns False
    assert export_csv([], test_filename) is False
