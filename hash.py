import hashlib as h
import json

#hash a block
def hash_block(block):
    return h.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()