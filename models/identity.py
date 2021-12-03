"""All declarations and functions about identity."""
from models.common import create_hash

from cryptos import Bitcoin
from faker import Faker

faker = Faker()

class Identity:
    """Class Identity."""

    def __init__(self, name, email):
        """Init function."""
        # TODO: Crear una transaccion dummy de satoshis
        self._name=name
        self._email = email
        self._privkey, self._pubkey, self._address = self._gen_keys()

    @property
    def name(self):
        """Return name."""
        return self._name

    @property
    def email(self):
        """Return email."""
        return self._email

    @property
    def pubkey(self):
        """Return pubkey."""
        return self._pubkey

    @property
    def address(self):
        """Return address."""
        return self._address

    def _gen_keys(self):
        """Create a priv_key, a pub_key and an address from name and email."""
        btc = Bitcoin()
        passphrase = f"{self.name} {self.email}"
        privkey = create_hash(passphrase)
        pubkey = btc.privtopub(privkey)
        address = btc.pubtoaddr(pubkey)
        return privkey, pubkey, address


    def __str__(self):
        """String representation."""
        return self.name


class Identities:
    """Store all identities."""

    def __init__(self):
        """Init function."""
        self.identities = []


    def __str__(self):
        """String representation."""
        return str(self.identities)


    def __len__(self):
        """Len representation."""
        return len(self.identities)


    def gen_x_identities(self, num):
        """Generates <num> identities with faker names."""

        for i in range(num):      # pylint: disable=unused-variable
            name = f"{faker.first_name().lower()}"
            email = f"{name}.{faker.last_name().lower()}@{faker.domain_name()}"
            self.gen_identity(name, email)

    def gen_x_nodes(self, num):
        """Generates <num> nodes."""

        for i in range(1,num+1):
            node_name = f"nodo{i}"
            email = f"{node_name}@example.com"
            self.gen_identity(node_name, email)


    def gen_identity(self, name, email):
        """Generate identity with data."""

        identity = Identity(name, email)
        self.identities.append(identity)


    def search_by_name(self, name):
        """Search by name."""
        for elem in self.identities:
            if elem.name == name:
                return elem
        return None


    def get_pubkey_by_name(self, name):
        """Return pubkey by name."""
        identity = self.search_by_name(name)
        if identity:
            return identity.pubkey
        return None
