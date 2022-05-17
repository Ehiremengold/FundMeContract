import os
from unittest import mock
from brownie import accounts, network, FundMe, MockV3Aggregator, config
from web3 import Web3
from scripts.utils import deploy_mock, get_account, LOCAL_ENVIROMENT_NETWORKS


def deploy_fundme_contract():
    account = get_account()
    print(f"the active network is {network.show_active()}")
    # removed the parenthesis after showactive() test if it works
    if network.show_active() not in LOCAL_ENVIROMENT_NETWORKS:
        # if we're on a live testnet or mainnet
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address

    fund_contract = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    return fund_contract


def main():
    deploy_fundme_contract()
