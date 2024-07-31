from .models.get_deposit_address_response import GetDepositAddressResponse
from .models.get_deposit_bank_account_response import GetDepositBankAccountResponse
from .models.get_wallet_accounts_response import GetWalletAccountsResponse
from .models.get_wallet_balances_response import GetWalletBalancesResponse
from .models.query_wallet_account_transactions_request import QueryWalletAccountTransactionsRequest
from .models.query_wallet_account_transactions_response import QueryWalletAccountTransactionsResponse
from .base_client import BaseClient


class WalletAPI(BaseClient):
    pass

    def get_balances(self, access_token) -> GetWalletBalancesResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/wallet/balances'
        response_text = self.call_api(url, 'GET', access_token)
        return GetWalletBalancesResponse.from_json(response_text)

    def get_accounts(self, access_token) -> GetWalletAccountsResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/wallet/accounts'
        response_text = self.call_api(url, 'GET', access_token)
        return GetWalletAccountsResponse.from_json(response_text)

    def query_transactions(self, access_token, account_id,
                           query_wallet_transactions_request: QueryWalletAccountTransactionsRequest = None) -> QueryWalletAccountTransactionsResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/wallet/accounts/{account_id}/transactions'

        if query_wallet_transactions_request is None:
            query_wallet_transactions_request = QueryWalletAccountTransactionsRequest()

        response_text = self.call_api(url, 'GET', access_token, query_params=query_wallet_transactions_request.to_str())
        # Adjust the JSON string to match dataclass field names as 'from' is a reserved keyword
        adjusted_json_string = response_text.replace('"from":', '"from_currency":').replace('"to":', '"to_currency":')
        return QueryWalletAccountTransactionsResponse.from_json(adjusted_json_string)

    def get_deposit_address(self, access_token, account_id) -> GetDepositAddressResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/wallet/accounts/{account_id}/deposit/address'
        response_text = self.call_api(url, 'GET', access_token)
        return GetDepositAddressResponse.from_json(response_text)

    def get_deposit_bank_account(self, access_token, account_id) -> GetDepositBankAccountResponse:
        url = f'{self.configuration.host}/v{self.configuration.api_version}/wallet/accounts/{account_id}/deposit/bank-account'
        response_text = self.call_api(url, 'GET', access_token)
        return GetDepositBankAccountResponse.from_json(response_text)
