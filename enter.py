from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Page de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        username = request.form['username']
        password = request.form['password']

        # Vérifier les informations de connexion (exemple simple)
        if username == 'mon_utilisateur' and password == 'mon_mot_de_passe':
            return redirect('/dashboard')  # Redirection vers le tableau de bord après connexion
        else:
            error = 'Identifiants invalides. Veuillez réessayer.'

        return render_template('login.html', error=error)

    return render_template('login.html')

# Page du tableau de bord
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)