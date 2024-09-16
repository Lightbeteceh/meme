from core.client import TelegramClient
from exception.custom_exceptions import InvalidQueryIDError, AuthenticationError
from utils.utils import validate_query_id, load_session, get_fake_user_agent, get_fake_ip

def register_client(session_name, query_id):
    try:
        validate_query_id(query_id)
        session = load_session(session_name)
        client = TelegramClient(session, query_id)
        config = get_config()
        if config["USE_FAKE_USER_AGENT"]:
            client.set_user_agent(get_fake_user_agent())
        if config["USE_FAKE_IP"]:
            client.set_proxy(get_fake_ip())
        client.start()
        return client
    except InvalidQueryIDError as e:
        print(f"Query ID '{query_id}' tidak valid: {e}")
        return None
    except AuthenticationError as e:
        print(f"Gagal mengotentikasi akun dengan query_id '{query_id}': {e}")
        return None