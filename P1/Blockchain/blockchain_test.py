from blockchain import Block, BlockChain
from datetime import datetime
import hashlib
import pytest


def test_calc_hash():
    sha = hashlib.sha256()
    data = "some information"
    timestamp = datetime.utcnow().isoformat()
    prev_hash = str(None)
    sha.update(data.encode("utf-8") + timestamp.encode("utf-8") +
               prev_hash.encode("utf-8"))
    block = Block(timestamp, data, prev_hash)
    assert sha.hexdigest() == block.calc_hash()


def test_blockchain():
    blockChain = BlockChain()

    assert blockChain.genesis_block == None

    blockChain = BlockChain()
    blockChain.add_block("Ola mundo")
    blockChain.add_block("Hello word")

    assert blockChain.genesis_block.block.data == "Ola mundo"
    assert blockChain.size == 2
    assert blockChain.tail.block.previous_hash == blockChain.genesis_block.block.hash

    with pytest.raises(ValueError):
        blockChain.add_block(None)

    with pytest.raises(ValueError):
        blockChain.add_block("")
