import requests

def register_user():
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    data = {"username": username, "password": password}
    response = requests.post("http://server1:5000/register", json=data)
    if response.status_code == 200:
        print("Utilisateur enregistré avec succès !")
    else:
        print("Erreur lors de l'enregistrement.")

def login_user():
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    data = {"username": username, "password": password}
    response = requests.post("http://server1:5000/login", json=data)
    if response.status_code == 200:
        print("Connexion réussie !")
    else:
        print("Erreur lors de la connexion.")

if __name__ == "__main__":
    while True:
        print("\n1. Inscription")
        print("2. Connexion")
        print("3. Quitter")
        choice = input("Choisissez une option : ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            break
        else:
            print("Option invalide.")
