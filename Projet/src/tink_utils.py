from tink import daead
from tink import tink_config

# Initialisation de Tink
tink_config.register()

def encrypt_with_aes_siv(data, keyset_handle):
    cipher = keyset_handle.primitive(daead.DeterministicAead)
    encrypted_data = cipher.encrypt_deterministically(data.encode('utf-8'), b'additional_data')
    return encrypted_data
