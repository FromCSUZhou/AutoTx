from gnosis.eth import EthereumClient
from web3 import Web3
from gnosis.safe import Safe
from .constants import MASTER_COPY_ADDRESS

def is_valid_safe(client: EthereumClient, safe_address: str) -> bool:
    w3 = client.w3

    if w3.eth.get_code(Web3.to_checksum_address(safe_address)) != w3.to_bytes(hexstr="0x"):
        safe = Safe(Web3.to_checksum_address(safe_address), client)
        master_copy_address = safe.retrieve_master_copy_address()
        return master_copy_address == MASTER_COPY_ADDRESS
    else:
        return False