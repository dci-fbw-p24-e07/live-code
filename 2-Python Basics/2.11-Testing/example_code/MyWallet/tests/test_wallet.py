import pytest
from main import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    return Wallet()


@pytest.fixture
def wallet():
    return Wallet(200)

def test_default_balance(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 200
    
def test_wallet_pay_success(wallet):
    wallet.pay(150)
    assert wallet.balance == 50

def test_wallet_get_cash_success():
    wallet = Wallet(30)
    wallet.get_cash(120)
    assert wallet.balance == 150
    
def test_wallet_pay_raises_insufficient_amount_exception():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.pay(30)
