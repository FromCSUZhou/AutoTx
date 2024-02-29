from langchain.tools import tool


class SafeTools:
    @tool("Create transaction")
    def create_transaction(payload):
        """
        Creates transaction in safe. It recieves an array of transactions, which will be
        converted to a multisend transaction if necessary, if not, it just create a single transaction

        :param payload: str, a string representations of an array of ethereum transactions

        example payload:
        [{
            to: str
            value: str
            data: str
        }]

        :return safe_transaction_hash: str, hash of the recently created safe transaction
        """
        
        return "0xSAFE_TRANSACTION_HASH"

    @tool("Execute signed transaction in safe")
    def execute_transaction(safe_transaction_hash):
        """
        :param safe_transaction_hash: str, hash of the transaction to be executed

        :return hash: str, hash of transaction executed
        """
        return "0xEXECUTED_TRANSACTION_HASH"

    @tool("Sign transaction")
    def sign_transaction(safe_transaction_hash):
        """
        :param safe_transaction_hash: str, hash of the transaction to be signed

        :return signature: str, signature added to transaction from hash given
        """
        return "0xSIGNATURE"
