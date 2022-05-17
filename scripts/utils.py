from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
FORKED_LOCAL_ENVIROMENT = ["mainnet-fork-dev", "mainnet-fork"]
LOCAL_ENVIROMENT_NETWORKS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_ENVIROMENT_NETWORKS
        or network.show_active() in FORKED_LOCAL_ENVIROMENT
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mock():
    if len(MockV3Aggregator) <= 0:
        print("Deploying Mocks...")
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
