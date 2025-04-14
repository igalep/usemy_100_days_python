import pprint
import hvac



class VaultAccess:
    _vault_client = None

    def __new__(cls, *args, **kwargs):
        if cls._vault_client is None:
            cls._vault_client = super(VaultAccess, cls).__new__(cls)
        return cls._vault_client

    def __init__(self):
        self.url = 'http://127.0.0.1:8200'

        if not hasattr(self, '_initialized'):
            self.client = hvac.Client(url=self.url, token='myroot')

        if not self.client.is_authenticated():
            raise Exception("Vault authentication failed.")

        self._initialized = True

    def write_data(self, **kwargs):
        self.client.secrets.kv.v2.create_or_update_secret(path='myapp', secret= kwargs)

    def pull_data(self, **kwargs):
        return self.client.secrets.kv.v2.read_secret_version(path=kwargs['path'], version=kwargs['version'])
