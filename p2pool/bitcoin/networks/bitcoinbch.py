import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


# Magic number BCH - Bitcoin ABC 0.16.2:
#    mainnet: 0xe3, 0xe1, 0xf3, 0xe8
#    testnet: 0xf4, 0xe5, 0xf3, 0xf4
#    regtest: 0xda, 0xb5, 0xbf, 0xfa
P2P_PREFIX =  'e3e1f3e8'.decode('hex')
P2P_PORT = 5914
ADDRESS_VERSION = 0
RPC_PORT = 15914
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'BCH'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcoin'), 'bitcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://blockdozer.com/insight/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://blockdozer.com/insight/address/'
TX_EXPLORER_URL_PREFIX = 'http://blockdozer.com/insight/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
