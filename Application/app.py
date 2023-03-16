#Créer un fichier de log pour stocker les erreurs
import logging
logging.basicConfig(filename='error.log',level=logging.DEBUG)

#A exécuter dans le terminal 
#flask run --debugger --reload
from flask import Flask, render_template, request
#pip install flask-bootstrap
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Route pour servir les fichiers statiques
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# Route pour la page d'accueil (Présentation)
@app.route('/')
def index():
    return render_template('index.html')

# Route pour la page de Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route pour la page de Data
@app.route('/data')
def data():
    return render_template('data.html')

# Route pour afficher le formulaire de prédiction
@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

# Route pour traiter les données du formulaire
@app.route('/predict', methods=['POST'])
def predict():
    surface_habitable = request.form['surface_habitable']
    nombre_chambres = request.form['nombre_chambres']
    presence_piscine = request.form['presence_piscine']
    
    # Code pour prédire le prix de la maison en fonction des données envoyées
    # ...
    # ...
    # ...

    return 'Le prix prédit pour cette maison est : XXXX €'

if __name__ == '__main__':
    app.run(debug=True)