import hmac
import hashlib
import base64


class WebhookSignatureUtil:
    @staticmethod
    def is_valid(payload: str, secret_key: str, signature_to_verify: str) -> bool:
        """
        Validates the provided signature against the generated signature.

        :param payload: The payload data to be signed.
        :param secret_key: The secret key used for generating the signature.
        :param signature_to_verify: The signature to verify against.
        :return: Returns True if the signatures match, otherwise False.
        """
        return signature_to_verify == WebhookSignatureUtil.generate_signature(payload, secret_key)

    @staticmethod
    def generate_signature(payload: str, secret_key: str) -> str:
        """
        Generates an HMAC-SHA256 signature and encodes it in Base64.

        :param payload: The payload data to be signed.
        :param secret_key: The secret key used for generating the signature.
        :return: The generated Base64-encoded signature.
        """
        # Create an HMAC-SHA256 hash
        hash_bytes = hmac.new(secret_key.encode(), payload.encode(), hashlib.sha256).digest()

        # Encode the hash in Base64
        return base64.b64encode(hash_bytes).decode()
