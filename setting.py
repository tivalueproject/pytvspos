VSYS = 100000000
DEFAULT_TX_FEE = int(0.1 * VSYS)
DEFAULT_FEE_SCALE = 100
DEFAULT_SUPER_NODE_NUM = 15

DEFAULT_PAYMENT_FEE = DEFAULT_TX_FEE
DEFAULT_LEASE_FEE = DEFAULT_TX_FEE
DEFAULT_CANCEL_LEASE_FEE = DEFAULT_TX_FEE
DEFAULT_CONTEND_SLOT_FEE = 50000 * VSYS
DEFAULT_RELEASE_SLOT_FEE = DEFAULT_TX_FEE
DEFAULT_DBPUT_FEE = 1 * VSYS

MAX_ATTACHMENT_SIZE = 140
MAX_DB_KEY_SIZE = 30
MIN_DB_KEY_SIZE = 1
MAX_NONCE = 4294967295
MAX_TX_HISTORY_LIMIT = 10000
MIN_CONTEND_SLOT_BALANCE = 1000000 * VSYS

THROW_EXCEPTION_ON_ERROR = True
CHECK_FEE_SCALE = True

DEFAULT_CHAIN = 'mainnet'
DEFAULT_CHAIN_ID = 'M'

TESTNET_CHAIN = 'testnet'
TESTNET_CHAIN_ID = 'T'

DEFAULT_TESTNET_NODE = ''
DEFAULT_TESTNET_API_KEY = ''


DEFAULT_NODE = 'http://127.0.0.1:9922'
DEFAULT_API_KEY = ''

ADDRESS_VERSION = 5
ADDRESS_CHECKSUM_LENGTH = 4
ADDRESS_HASH_LENGTH = 20
ADDRESS_LENGTH = 1 + 1 + ADDRESS_CHECKSUM_LENGTH + ADDRESS_HASH_LENGTH

PAYMENT_TX_TYPE = 2
LEASE_TX_TYPE = 3
LEASE_CANCEL_TX_TYPE = 4
CONTEND_SLOT_TX_TYPE = 6
RELEASE_SLOT_TX_TYPE = 7
DBPUT_TX_TYPE = 10

LEASE_TX_ID_BYTES = 32



