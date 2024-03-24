from autotx.utils.ethereum.config import contracts_config
from gnosis.eth import EthereumNetwork

MASTER_COPY_ADDRESS = contracts_config["safe"]["master_copy_address"]
PROXY_FACTORY_ADDRESS = contracts_config["safe"]["proxy_factory_address"]
MULTI_SEND_ADDRESS = contracts_config["safe"]["multisend_address"]
GAS_PRICE_MULTIPLIER = 1.1
FORK_RPC_URL = "http://localhost:8545"

class NetworkInfo:
    network: EthereumNetwork
    transaction_service_url: str
    tokens: dict[str, str]

    def __init__(self, network: EthereumNetwork, transaction_service_url: str, tokens: dict[str, str]):
        self.network = network
        self.transaction_service_url = transaction_service_url
        self.tokens = tokens

SUPPORTED_NETWORKS: dict[int, NetworkInfo] = {
    1: NetworkInfo(
       EthereumNetwork.MAINNET, 
       "https://safe-transaction-mainnet.safe.global/",
       tokens={
            "usdc": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "dai": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
            "weth": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            "wbtc": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
            "usdt": "0xdac17f958d2ee523a2206206994597c13d831ec7"
        }
    ),
    10: NetworkInfo(
        EthereumNetwork.OPTIMISM, 
        "https://safe-transaction-optimism.safe.global/",
        tokens={
            "usdc": "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85",
            "dai": "0xda10009cbd5d07dd0cecc66161fc93d7c9000da1",
            "usdt": "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58"
        }
    ),
    324: NetworkInfo(
        EthereumNetwork.ZKSYNC_V2, 
        "https://safe-transaction-zksync.safe.global/",
        tokens={
            "usdc": "0x3355df6d4c9c3035724fd0e3914de96a5a83aaf4",
            "dai": "0x4b9eb6c0b6ea15176bbf62841c6b2a8a398cb656",
            "usdt": "0x493257fD37EDB34451f62EDf8D2a0C418852bA4C"
        }
    ),
    137: NetworkInfo(
        EthereumNetwork.POLYGON, 
        "https://safe-transaction-polygon.safe.global/",
        tokens={
            "usdc": "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359",
            "dai": "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063",
            "usdt": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f"
        }
    ),
    8453: NetworkInfo(
        EthereumNetwork.BASE_MAINNET, 
        "https://safe-transaction-base.safe.global/",
        tokens={
            "usdc": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
            "dai": "0x50c5725949a6f0c72e6c4a641f24049a917db0cb",
        }
    ),
    42161: NetworkInfo(
        EthereumNetwork.ARBITRUM_ONE, 
        "https://safe-transaction-arbitrum.safe.global/",
        tokens={
            "usdc": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
            "dai": "0xda10009cbd5d07dd0cecc66161fc93d7c9000da1",
            "usdt": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9"
        }
    ),
    11155111: NetworkInfo(
        EthereumNetwork.SEPOLIA, 
        "https://safe-transaction-sepolia.safe.global/",
        tokens={
            "weth": "0xfff9976782d46cc05630d1f6ebab18b2324d6b14",
        }
    ),
}
