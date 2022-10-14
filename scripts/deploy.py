from scripts.helpful_scripts import get_account, fund_with_link
from brownie import randomNumber, config, network, accounts
import time


def deploy_contract():
    account = get_account()
    fee = 0.1 * 10 ** 18
    contract = randomNumber.deploy(
        config["networks"][network.show_active()]["vrfCoordinator"],
        config["networks"][network.show_active()]["link"],
        config["networks"][network.show_active()]["keyHash"],
        fee,
        {"from": account},
    )
    fund_with_link(contract.address)
    tx = contract.getRandomness({"from": account})
    tx.wait(1)
    time.sleep(200)
    print(f"The random number is {contract.randomNumber()}")
    print(f"The dice rolled is {contract.rollDice()}")


def main():
    deploy_contract()
