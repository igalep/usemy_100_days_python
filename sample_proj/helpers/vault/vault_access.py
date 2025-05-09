import hvac
from .token_git_ignored import VAULT_TOKEN



class VaultAccess:
    """
    A singleton implementation for interacting with a Vault server.

    This class is designed to provide operations for a Vault server, enabling
    secure storage and retrieval of secrets. It ensures a single client instance
    is used throughout the application to interact with the Vault server. The class
    primarily supports writing and reading secrets to/from a key-value store using
    the `hvac` client.

    :ivar url: The URL of the Vault server.
    :type url: str
    :ivar client: The `hvac` client instance used for interacting with the Vault server.
    :type client: hvac.Client
    :ivar _initialized: A boolean flag to indicate whether the instance has been
        initialized.
    :type _initialized: bool
    """
    _vault_client = None

    def __new__(cls, *args, **kwargs):
        if cls._vault_client is None:
            cls._vault_client = super(VaultAccess, cls).__new__(cls)
        return cls._vault_client

    def __init__(self):
        self.url = 'http://127.0.0.1:8200'

        if not hasattr(self, '_initialized'):
            self.client = hvac.Client(url=self.url, token=VAULT_TOKEN)
            #/Users/igalep/Dev/projects/python/vault_unseal_key_local_docker
        if not self.client.is_authenticated():
            raise Exception("Vault authentication failed.")

        self._initialized = True

    def write_data(self, **kwargs):
        """
        Writes data to a specified secret path in the key-value store.

        This method utilizes a secret client to create or update a secret
        at a specified path with user-provided key-value pairs. It operates
        in the context of a specified mount point within the storage system.

        :param kwargs: Arbitrary keyword arguments, including:
            - path: str, the path in the key-value store where the secret will be written.
            - secret: dict, the key-value pairs of the secret to be stored.
            - mount: str, the mount point for the key-value store operation.

        :return: None
        """
        self.client.secrets.kv.v2.create_or_update_secret(path=kwargs['path'], secret=kwargs['secret'], mount_point=kwargs['mount'])

    def pull_data(self, **kwargs):
        """
        Pulls data from a key-value secret store using specified parameters.

        :param kwargs: Arbitrary keyword arguments. Accepted keys:
            - path (str): The path at which the secret is stored.
            - version (Optional[int]): The version of the secret to retrieve,
              if applicable.
        :return: The secret data retrieved from the store.
        :rtype: dict
        """
        return self.client.secrets.kv.v2.read_secret_version(path=kwargs['path'], version=kwargs.get('version'),
                                                             mount_point=kwargs['mount']).get('data',{}).get('data', {})
