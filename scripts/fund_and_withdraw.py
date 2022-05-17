from brownie import network, accounts, FundMe
from scripts.utils import get_account


def fund():
    fundme = FundMe[-1]
    account = get_account()
    entrance_fee = fundme.getEntranceFee()
    print(f"This is the {entrance_fee}")
    print("Funding...")
    fundme.fund({"from": account, "value": entrance_fee})


def withdraw():
    fundme = FundMe[-1]
    account = get_account()
    print("Withdraw...")
    fundme.withdraw({"from": account})


def main():
    fund()
    # withdraw()
