from flask import Flask, render_template, request, redirect, url_for, jsonify, app
from app.models import db, User, Habit
import json

@app.route('/')
def index():
    return render_template('index.html')

# Liste en mémoire des noms d'utilisateurs enregistrés
registered_usernames = ['admin', 'user1', 'user2']

def check_username_availability(username):
    if username in registered_usernames:
        return True  # Le nom d'utilisateur est déjà pris
    else:
        return False  # Le nom d'utilisateur est disponible

def check_credentials(username, password):
    # Vérifiez ici les informations d'identification de l'utilisateur
    if username == 'admin' and password == 'password':
        return True
    else:
        return False

@app.route('/home')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if check_credentials(username, password):
            return redirect(url_for('habitudes'))
        else:
            error = 'Nom d\'utilisateur ou mot de passe incorrect'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/habitudes')
def habitudes():
    # Récupérez les habitudes de l'utilisateur depuis la base de données ou un fichier
    # et passez-les à la page habitudes.html pour les afficher
    
    # Exemple de données d'habitudes pour tester
    habits = ['Faire de l\'exercice', 'Lire', 'Méditer', 'Boire suffisamment d\'eau']
    
    return render_template('habitudes.html', habits=habits)

def add_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

def add_habit(habit_name):
    habit = Habit(name=habit_name)
    db.session.add(habit)
    db.session.commit()

def get_user_habits():
    # Implémentez cette fonction pour récupérer les habitudes de l'utilisateur depuis la base de données
    return []

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if check_username_availability(username):
            error = 'Le nom d\'utilisateur est déjà pris'
            return render_template('register.html', error=error)

        add_user(username, password)

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/check-username', methods=['POST'])
def check_username():
    username = request.form['username']
    is_taken = check_username_availability(username)
    response = {'is_taken': is_taken}
    return jsonify(response)

@app.route('/create_habit', methods=['POST'])
def create_habit():
    habit_name = request.form['habit_name']
    add_habit(habit_name)
    return redirect(url_for('habitstracker'))

@app.route('/habitstracker')
def habitstracker():
    habits = get_user_habits()
    return render_template('habitstracker.html', habits=habits)

if __name__ == '__main__':
    app.run(debug=True)
