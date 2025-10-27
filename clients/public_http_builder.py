from httpx import Client

def get_public_http_client() -> Client:
    """
    This function creates an instance of httpx.Client with basic configuration.

    :return: A ready-to-use httpx.Client object.
    """
    return Client(timeout=100, base_url="http://localhost:8000")