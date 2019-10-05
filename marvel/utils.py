import hashlib
from datetime import datetime


class Marvel:
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key

    def get_auth_data(self):
        timestamp = datetime.now().timestamp()
        formatted_string = f'{timestamp}{self.private_key}{self.public_key}'
        hashed_data = hashlib.md5(formatted_string.encode('utf-8')).hexdigest()
        data = dict(ts=timestamp, apikey=self.public_key, hash=hashed_data)
        return data
