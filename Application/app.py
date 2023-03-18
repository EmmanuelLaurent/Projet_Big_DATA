#Créer un fichier de log pour stocker les erreurs
import logging
logging.basicConfig(filename='error.log',level=logging.DEBUG)

#A exécuter dans le terminal 
#flask run --debugger --reload
from flask import Flask, render_template, request
#pip install flask-bootstrap
from flask_bootstrap import Bootstrap

import os
import xgboost
import pickle
import pandas as pd
import numpy as np

# Obtenir le chemin absolu du fichier modele_xgb_pickle.pkl
dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, 'modele_xgb_pickle.pkl')

with open(model_path, 'rb') as fichier:
    modele_xgb = pickle.load(fichier)

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
  surface_habitable = float(request.form['surface_habitable'])
  etat_maison = int(request.form['etat_maison'])
  hauteur_sous_sol = request.form['hauteur_sous-sol']
  annee_renovation = int(request.form['annee_renovation'])
  exter_qual = request.form['exter_qual']
  kitchen_qual = request.form['kitchen_qual']
  pool_area = float(request.form['pool_area'])
  garage_cars = float(request.form['garage_cars'])
  garage_type = request.form['garage_type']
  ms_zoning = request.form['ms_zoning']
  condition1 = request.form['condition1']
  condition2 = request.form['condition2']
  neighborhood = request.form['neighborhood']
  electrical = request.form['electrical']
  central_air = request.form['central_air']
  bathroom = float(request.form['bathroom'])
  heating = request.form['heating']
  BldgType = request.form['BldgType']

  data = {
    'GarageCars': garage_cars,
    'Total_SF' : surface_habitable,
    'OverallQual' : etat_maison,
    'Total_Bathrooms' : bathroom,
    'PoolArea': pool_area,
    'YearRemodAdd': annee_renovation,
    'BsmtQual_Ex': 0,
    'BsmtQual_Fa': 0,
    'BsmtQual_Gd': 0,
    'BsmtQual_None': 0,
    'BsmtQual_TA': 0,
    'ExterQual_Ex': 0,
    'ExterQual_Fa': 0,
    'ExterQual_Gd': 0,
    'ExterQual_TA': 0,
    'MSZoning_C (all)': 0,
    'MSZoning_FV': 0,
    'MSZoning_RH': 0,
    'MSZoning_RL': 0,
    'MSZoning_RM': 0,
    'Neighborhood_Blmngtn': 0,
    'Neighborhood_Blueste': 0,
    'Neighborhood_BrDale': 0,
    'Neighborhood_BrkSide': 0,
    'Neighborhood_ClearCr': 0,
    'Neighborhood_CollgCr': 0,
    'Neighborhood_Crawfor': 0,
    'Neighborhood_Edwards': 0,
    'Neighborhood_Gilbert': 0,
    'Neighborhood_IDOTRR': 0,
    'Neighborhood_MeadowV': 0,
    'Neighborhood_Mitchel': 0,
    'Neighborhood_NAmes': 0,
    'Neighborhood_NPkVill': 0,
    'Neighborhood_NWAmes': 0,
    'Neighborhood_NoRidge': 0,
    'Neighborhood_NridgHt': 0,
    'Neighborhood_OldTown': 0,
    'Neighborhood_SWISU': 0,
    'Neighborhood_Sawyer': 0,
    'Neighborhood_SawyerW': 0,
    'Neighborhood_Somerst': 0,
    'Neighborhood_StoneBr': 0,
    'Neighborhood_Timber': 0,
    'Neighborhood_Veenker': 0,
    'BldgType_1Fam': 0,
    'BldgType_2fmCon': 0,
    'BldgType_Duplex': 0,
    'BldgType_Twnhs': 0,
    'BldgType_TwnhsE': 0,
    'Heating_Floor' : 0,
    'Heating_GasA' : 0,
    'Heating_GasW' : 0,
    'Heating_Grav' : 0,
    'Heating_OthW' : 0,
    'Heating_Wall' : 0,
    'CentralAir_N' : 0,
    'CentralAir_Y' : 0,
    'Electrical_FuseA': 0,
    'Electrical_FuseF': 0,
    'Electrical_FuseP': 0,
    'Electrical_Mix': 0,
    'Electrical_SBrkr': 0,
    'Condition1_Artery' : 0,
    'Condition1_Feedr' : 0,
    'Condition1_Norm' : 0,
    'Condition1_PosA' : 0,
    'Condition1_PosN' : 0,
    'Condition1_RRAe' : 0,
    'Condition1_RRAn' : 0,
    'Condition1_RRNe' : 0,
    'Condition1_RRNn' : 0,
    'Condition2_Artery' : 0,
    'Condition2_Feedr' : 0,
    'Condition2_Norm' : 0,
    'Condition2_PosA' : 0,
    'Condition2_PosN' : 0,
    'Condition2_RRAe' : 0,
    'Condition2_RRAn' : 0,
    'Condition2_RRNn' : 0,
    'GarageType_2Types': 0,
    'GarageType_Attchd': 0,
    'GarageType_Basment': 0,
    'GarageType_BuiltIn': 0,
    'GarageType_CarPort': 0,
    'GarageType_Detchd': 0,
    'GarageType_None': 0,
    'KitchenQual_Ex': 0,
    'KitchenQual_Fa': 0,
    'KitchenQual_Gd': 0,
    'KitchenQual_TA': 0
  }
  
  if hauteur_sous_sol == 'Ex':
    data['BsmtQual_Ex'] = 1
  elif hauteur_sous_sol == 'Gd':
    data['BsmtQual_Gd'] = 1
  elif hauteur_sous_sol == 'TA':
    data['BsmtQual_TA'] = 1
  elif hauteur_sous_sol == 'Fa':
    data['BsmtQual_Fa'] = 1
  elif hauteur_sous_sol == 'None':
    data['BsmtQual_None'] = 1
    
  if exter_qual == 'Ex':
    data['ExterQual_Ex'] = 1
  elif exter_qual == 'Gd':
    data['ExterQual_Gd'] = 1
  elif exter_qual == 'TA':
    data['ExterQual_TA'] = 1
  elif exter_qual == 'Fa':
    data['ExterQual_Fa'] = 1

  if kitchen_qual == 'Ex':
    data['KitchenQual_Ex'] = 1
  elif kitchen_qual == 'Gd':
    data['KitchenQual_Gd'] = 1
  elif kitchen_qual == 'TA':
    data['KitchenQual_TA'] = 1
  elif kitchen_qual == 'Fa':
    data['KitchenQual_Fa'] = 1

  if garage_type == 'Attchd':
    data['GarageType_Attchd'] = 1
  elif garage_type == '2Types':
    data['GarageType_2Types'] = 1
  elif garage_type == 'Basment':
    data['GarageType_Basment'] = 1
  elif garage_type == 'BuiltIn':
    data['GarageType_BuiltIn'] = 1
  elif garage_type == 'CarPort':
    data['GarageType_CarPort'] = 1
  elif garage_type == 'Detchd':
    data['GarageType_Detchd'] = 1
  elif garage_type == 'None':
    data['GarageType_None'] = 1

  if ms_zoning == 'C (all)':
    data['MSZoning_C (all)'] = 1
  elif ms_zoning == 'FV':
    data['MSZoning_FV'] = 1
  elif ms_zoning == 'RH':
    data['MSZoning_RH'] = 1
  elif ms_zoning == 'RM':
    data['MSZoning_RM'] = 1
  elif ms_zoning == 'RL':
    data['MSZoning_RL'] = 1

  if condition1 == 'Artery':
    data['Condition1_Artery'] = 1
  elif condition1 == 'Feedr':
    data['Condition1_Feedr'] = 1
  elif condition1 == 'Norm':
    data['Condition1_Norm'] = 1
  elif condition1 == 'RRNn':
    data['Condition1_RRNn'] = 1
  elif condition1 == 'RRAn':
    data['Condition1_RRAn'] = 1
  elif condition1 == 'PosN':
    data['Condition1_PosN'] = 1
  elif condition1 == 'PosA':
    data['Condition1_PosA'] = 1
  elif condition1 == 'RRNe':
    data['Condition1_RRNe'] = 1
  elif condition1 == 'RRAe':
    data['Condition1_RRAe'] = 1

  if condition2 == 'Artery':
    data['Condition2_Artery'] = 1
  elif condition2 == 'Feedr':
    data['Condition2_Feedr'] = 1
  elif condition2 == 'Norm':
    data['Condition2_Norm'] = 1
  elif condition2 == 'RRNn':
    data['Condition2_RRNn'] = 1
  elif condition2 == 'RRAn':
    data['Condition2_RRAn'] = 1
  elif condition2 == 'PosN':
    data['Condition2_PosN'] = 1
  elif condition2 == 'PosA':
    data['Condition2_PosA'] = 1
  elif condition2 == 'RRAe':
    data['Condition2_RRAe'] = 1

  if neighborhood == 'Blmngtn':
    data['Neighborhood_Blmngtn'] = 1
  elif neighborhood == 'Blueste':
    data['Neighborhood_Blueste'] = 1
  elif neighborhood == 'BrDale':
    data['Neighborhood_BrDale'] = 1
  elif neighborhood == 'BrkSide':
    data['Neighborhood_BrkSide'] = 1
  elif neighborhood == 'ClearCr':
    data['Neighborhood_ClearCr'] = 1
  elif neighborhood == 'CollgCr':
    data['Neighborhood_CollgCr'] = 1
  elif neighborhood == 'Crawfor':
    data['Neighborhood_Crawfor'] = 1
  elif neighborhood == 'Edwards':
    data['Neighborhood_Edwards'] = 1
  elif neighborhood == 'Gilbert':
    data['Neighborhood_Gilbert'] = 1
  elif neighborhood == 'IDOTRR':
    data['Neighborhood_IDOTRR'] = 1
  elif neighborhood == 'MeadowV':
    data['Neighborhood_MeadowV'] = 1
  elif neighborhood == 'Mitchel':
    data['Neighborhood_Mitchel'] = 1
  elif neighborhood == 'NAmes':
    data['Neighborhood_NAmes'] = 1
  elif neighborhood == 'NoRidge':
    data['Neighborhood_NoRidge'] = 1
  elif neighborhood == 'NPkVill':
    data['Neighborhood_NPkVill'] = 1
  elif neighborhood == 'NridgHt':
    data['Neighborhood_NridgHt'] = 1
  elif neighborhood == 'NWAmes':
    data['Neighborhood_NWAmes'] = 1
  elif neighborhood == 'OldTown':
    data['Neighborhood_OldTown'] = 1
  elif neighborhood == 'SWISU':
    data['Neighborhood_SWISU'] = 1
  elif neighborhood == 'Sawyer':
    data['Neighborhood_Sawyer'] = 1
  elif neighborhood == 'SawyerW':
    data['Neighborhood_SawyerW'] = 1
  elif neighborhood == 'Somerst':
    data['Neighborhood_Somerst'] = 1
  elif neighborhood == 'StoneBr':
    data['Neighborhood_StoneBr'] = 1
  elif neighborhood == 'Timber':
    data['Neighborhood_Timber'] = 1
  elif neighborhood == 'Veenker':
    data['Neighborhood_Veenker'] = 1

  if electrical == 'SBrkr':
    data['Electrical_SBrkr'] = 1
  elif electrical == 'FuseA':
    data['Electrical_FuseA'] = 1
  elif electrical == 'FuseF':
    data['Electrical_FuseF'] = 1
  elif electrical == 'FuseP':
    data['Electrical_FuseP'] = 1
  elif electrical == 'Mix':
    data['Electrical_Mix'] = 1

  if central_air == 'Y':
    data['CentralAir_Y'] = 1
  elif central_air == 'N':
    data['CentralAir_N'] = 1

  if heating == 'Floor':
    data['Heating_Floor'] = 1
  elif heating == 'GasA':
    data['Heating_GasA'] = 1
  elif heating == 'GasW':
    data['Heating_GasW'] = 1
  elif heating == 'Grav':
    data['Heating_Grav'] = 1
  elif heating == 'OthW':
    data['Heating_OthW'] = 1
  elif heating == 'Wall':
    data['Heating_Wall'] = 1

  if BldgType == '1Fam':
    data['BldgType_1Fam'] = 1
  elif BldgType == '2fmCon':
    data['BldgType_2fmCon'] = 1
  elif BldgType == 'Duplex':
    data['BldgType_Duplex'] = 1
  elif BldgType == 'Twnhs':
    data['BldgType_Twnhs'] = 1
  elif BldgType == 'TwnhsE':
    data['BldgType_TwnhsE'] = 1

  prediction = modele_xgb.predict(pd.DataFrame(data, index=pd.Index([0])))
  
  return 'Le prix prédit pour ce logement est de : {} $'.format(int(np.expm1(prediction)[0]))

if __name__ == '__main__':
    app.run(debug=True)