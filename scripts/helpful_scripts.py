from brownie import config, accounts, Contract, network, LinkToken


def get_account():
    account = accounts.add(config["wallets"]["from_key"])
    return account


def fund_with_link(contract_address):
    account = get_account()
    link = Contract.from_abi(
        LinkToken._name,
        config["networks"][network.show_active()]["link"],
        LinkToken.abi,
    )
    fee = 0.1 * 10 ** 18
    tx = link.transfer(contract_address, fee, {"from": account})
    tx.wait(1)
    print("Contract funded with link successfully")
    return tx
