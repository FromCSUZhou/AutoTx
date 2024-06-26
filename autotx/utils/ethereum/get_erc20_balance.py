from web3 import Web3

from autotx.utils.ethereum.eth_address import ETHAddress
from .erc20_abi import ERC20_ABI

def get_erc20_balance(web3: Web3, token_address: ETHAddress, account: ETHAddress) -> float:
    erc20 = web3.eth.contract(address=token_address.hex, abi=ERC20_ABI)
    decimals = erc20.functions.decimals().call()

    return erc20.functions.balanceOf(account.hex).call() / 10 ** decimals
