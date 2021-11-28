"""Test Identity Class and Functions."""
from faker import Faker
from cryptos import Bitcoin
from models.identity import Identity, Identities


faker = Faker()

def test_create_identity():
    """Test Create Identity."""
    btc = Bitcoin()
    name = faker.first_name().lower()
    email = faker.email()
    identity = Identity(name, email)
    assert identity.name == name
    assert identity.email == email
    assert identity._privkey is not None    # pylint: disable=protected-access
    assert identity.pubkey is not None
    assert identity.address == btc.pubtoaddr(identity.pubkey)


def test_create_identities():
    """Test Create Identities."""
    identities = Identities()
    assert str(identities) == str([])


def test_gen_4_identities():
    """Test Create Identities."""
    identities = Identities()
    identities.gen_x_identities(4)
    assert len(identities.identities) == 4
    assert str(identities) == str(identities.identities)


def test_search_by_name():
    """Test Search by name."""
    identities = Identities()
    identities.gen_x_identities(4)
    second_identity = identities.identities[1]
    name = second_identity.name
    elem = identities.search_by_name(name)
    assert elem == second_identity


def test_get_pubkey_by_name():
    """Get pubkey by name."""
    identities = Identities()
    identities.gen_x_identities(4)
    first_identity = identities.identities[0]
    name = first_identity.name
    pubkey = first_identity.pubkey
    first_pubkey = identities.get_pubkey_by_name(name)
    assert first_pubkey == pubkey
