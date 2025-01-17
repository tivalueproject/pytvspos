import base58
import logging
import time
from .crypto import hashChain, bytes2str, str2bytes
from .setting import ADDRESS_LENGTH, ADDRESS_CHECKSUM_LENGTH, DEFAULT_SUPER_NODE_NUM
from .error import NetworkException
from .wrapper import Wrapper
from pytvspos import is_offline
import pytvspos


class Chain(object):

    def __init__(self, chain_name, chain_id, address_version, api_wrapper):
        self.chain_name = chain_name
        self.chain_id = chain_id
        self.address_version = address_version
        self.api_wrapper = api_wrapper

    def height(self):
        if is_offline():
            pytvspos.throw_error("Cannot check height in offline mode.", NetworkException)
            return 0
        else:
            return self.api_wrapper.request('/blocks/height')['height']

    def self_check(self, super_node_num=DEFAULT_SUPER_NODE_NUM):
        try:
            # check connected peers
            peers = self.get_connected_peers()
            if not peers:
                logging.error("The node {} does not connect any peers.".format(self.api_wrapper.node_host))
                return False
            # check height
            h2 = h1 = self.height()
            delay = max(int(60 / super_node_num), 1)
            count = 0
            while h2 <= h1 and count <= super_node_num:
                time.sleep(delay)
                h2 = self.height()
                count += 1
            if h2 <= h1:
                logging.error("The height is not update. Full node has problem or stopped.")
                return False
            # Add more check if need
            logging.debug("OK. Full node is alive.")
            return True
        except NetworkException:
            logging.error("Fail to connect full node.")
            return False

    def check_with_other_node(self, node_host, super_node_num=DEFAULT_SUPER_NODE_NUM):
        if is_offline():
            pytvspos.throw_error("Cannot check height in offline mode.", NetworkException)
            return False
        try:
            h1 = self.height()
        except NetworkException:
            logging.error("Fail to connect {}.".format(node_host))
            return False
        try:
            other_api = Wrapper(node_host)
            h2 = other_api.request('/blocks/height')['height']
        except NetworkException:
            logging.error("Fail to connect {}.".format(node_host))
            return False
        # Add more check if need
        return h2 - h1 <= super_node_num

    def get_connected_peers(self):
        if is_offline():
            pytvspos.throw_error("Cannot check peers in offline mode.", NetworkException)
            return []
        response = self.api_wrapper.request('/peers/connected')
        if not response.get("peers"):
            return []
        else:
            return [peer["address"] for peer in response.get("peers")]

    def lastblock(self):
        return self.api_wrapper.request('/blocks/last')

    def block(self, n):
        return self.api_wrapper.request('/blocks/at/%d' % n)

    def tx(self, id):
        return self.api_wrapper.request('/transactions/info/%s' % id)

    def unconfirmed_tx(self, id):
        return self.api_wrapper.request('/transactions/unconfirmed/info/%s' % id)

    def slot_info(self, slot_id):
        return self.api_wrapper.request('/consensus/slotInfo/%s' % slot_id)

    def validate_address(self, address):
        addr = bytes2str(base58.b58decode(address))
        if addr[0] != chr(self.address_version):
            logging.error("Wrong address version")
        elif addr[1] != self.chain_id:
            logging.error("Wrong chain id")
        elif len(addr) != ADDRESS_LENGTH:
            logging.error("Wrong address length")
        elif addr[-ADDRESS_CHECKSUM_LENGTH:] != hashChain(str2bytes(addr[:-ADDRESS_CHECKSUM_LENGTH]))[:ADDRESS_CHECKSUM_LENGTH]:
            logging.error("Wrong address checksum")
        else:
            return True
        return False

    def public_key_to_address(self, public_key):
        unhashedAddress = chr(self.address_version) + str(self.chain_id) + hashChain(public_key)[0:20]
        addressHash = hashChain(str2bytes(unhashedAddress))[0:4]
        address = bytes2str(base58.b58encode(str2bytes(unhashedAddress + addressHash)))
        return address
