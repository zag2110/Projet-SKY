from flask import Flask, request, jsonify
import bcrypt
import os

app = Flask(__name__)

@app.route('/hash', methods=['POST'])
def hash_password():
    data = request.get_json()
    password = data.get('password')

    # Générer un salt pour le hachage
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return jsonify({"hash": hashed_password.decode('utf-8'), "salt": salt.decode('utf-8')}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
