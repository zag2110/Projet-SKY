from flask import Flask, render_template, request, redirect, url_for
import requests
import bcrypt

# URL des serveurs (Server 1 et Server 2)
server1_url = "http://localhost:5000/hash"
server2_url = "http://localhost:5001/encrypt"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hachage du mot de passe avec Server 1
        response = requests.post(server1_url, json={"password": password})
        if response.status_code == 200:
            data = response.json()
            hashed_password = data['hash']
            salt = data['salt']
            print(f"Password hashed with salt: {salt}")

            # Envoi du hash chiffré au serveur 2
            encrypted_response = requests.post(server2_url, json={"hash": hashed_password})
            if encrypted_response.status_code == 200:
                encrypted_hash = encrypted_response.json()['ciphertext']
                print(f"Encrypted password hash: {encrypted_hash}")
                # Ici tu peux ajouter le hash chiffré à la base de données (Server 1)
                return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Récupération du hash chiffré depuis la base de données (Server 1)
        encrypted_hash = ""  # Remplace cela par la vraie récupération depuis la base de données

        # Déchiffrement avec Server 2
        response = requests.post(server2_url, json={"hash": encrypted_hash})
        if response.status_code == 200:
            decrypted_hash = response.json()['ciphertext']
            print(f"Decrypted hash: {decrypted_hash}")
            # Comparaison du mot de passe avec le hash déchiffré (via bcrypt)
            if bcrypt.checkpw(password.encode('utf-8'), decrypted_hash.encode('utf-8')):
                return "Login successful!"
            else:
                return "Invalid password!"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
