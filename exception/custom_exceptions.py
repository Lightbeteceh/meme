class InvalidQueryIDError(Exception):
    pass

class AuthenticationError(Exception):
    pass
```

### 5. Folder `utils/utils.py`:
```python
import os
import random
from exception.custom_exceptions import InvalidQueryIDError
from config.config import get_config

def validate_query_id(query_id):
    if not valid_query_id(query_id):
        raise InvalidQueryIDError("Query ID tidak valid")

def valid_query_id(query_id):
    return len(query_id) == 32 and query_id.isalnum()

def load_session(session_name):
    session_file = f"{session_name}.session"
    if os.path.exists(session_file):
        return session_file
    else:
        return session_name

def get_fake_user_agent():
    # Implementasi untuk mendapatkan user agent palsu
    return "User-Agent"

def get_fake_ip():
    # Implementasi untuk mendapatkan IP palsu jika diperlukan
    return "0.0.0.0"