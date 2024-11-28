from flask import Flask, request, jsonify
from tink import daead
from tink import tink_config
import base64

# Initialize Tink
tink_config.register()

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt_data():
    data = request.get_json()
    ciphertext = data.get('hash')

    # Générer la clé de chiffrement AES-SIV
    keyset_handle = daead.DeterministicAeadKeyManager().generate_new_keyset_handle()
    cipher = keyset_handle.primitive(daead.DeterministicAead)

    # Convertir le hash en bytes et le chiffrer
    plaintext = ciphertext.encode('utf-8')
    encrypted_data = cipher.encrypt_deterministically(plaintext, b'additional_data')

    # Retourner les données chiffrées en base64
    encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')

    return jsonify({"ciphertext": encrypted_base64}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
