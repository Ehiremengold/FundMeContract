# arrange
# act
# assert
from logging import exception
from brownie import network, accounts, exceptions
from scripts.deploy import deploy_fundme_contract
from scripts.utils import get_account, LOCAL_ENVIROMENT_NETWORKS
import pytest


def test_can_fund_and_withdraw():
    # Arrange
    account = get_account()
    fundme_contract = deploy_fundme_contract()
    entrance_fee = fundme_contract.getEntranceFee() + 100
    # Act
    tx = fundme_contract.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    # Assert
    assert fundme_contract.addressToAmountFunded(account.address) == entrance_fee

    # Act
    tx2 = fundme_contract.withdraw({"from": account})
    expected_amount = 0
    tx2.wait(1)
    # Assert
    assert fundme_contract.addressToAmountFunded(account.address) == expected_amount


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_ENVIROMENT_NETWORKS:
        pytest.skip("only for local testing...")
    bad_account = accounts[2]
    fundme_contract = deploy_fundme_contract()
    with pytest.raises(exceptions.VirtualMachineError):
        fundme_contract.withdraw({"from": bad_account})
