# Projet BigData : House prices

Ce fichier a pour but de présenter les différentes étapes de notre projet, la répartition des tâches.

## Les grand axes du projet :
- Choix du sujet;
- Définition du besoin;
- Gestion de projet;
- Étude et préparation des données;
- Modélisation;
- Reporting ;
- Développement de l'application;
- Rédaction du rapport.

## Répartition des tâches

- mise en place du lien Git/Jira : Thomas
- mise en place du Gantt : Thomas
- mise à disposition des Metadonnées dans le GitLab : Thomas
- mise en place du dictionnaire des données : Thomas/Antoine
- définition du besoin : Ilyes
- renommage des variables : Emmanuel
- statistiques descriptives : Antoine
- sélection des variables : Ilyes/Emmanuel 
- regroupement des modalités : Emmanuel
- création d'un Schéma du projet décisionnel : Thomas
- mise en place d'un modèle conceptuel de données (MCD/MCMD) : Thomas
- réalisation de la diapositive pour la soutenance intermédiaire : Ilyes/Thomas
- création d'une branche de développement sur GIT : Thomas
- création d'une matrice de corrélation : Emmanuel 
- identifier et corriger les valeurs aberrantes : Ilyes
- évolution du contexte du projet : Emmanuel
- conversion des variables de surface de pieds carrés à mètres carrés : Ilyes
- création d'hypothèses suite à la présentation intermédiaire : Antoine
- faire une première connexion entre Python et PowerBI : Thomas
- BUG connexion entre Python et PowerBI : Thomas
- rédaction du rapport : Ilyes/Antoine
- étude de la sauvegarde et de l'export du modèle : Emmanuel
- création de l'application utiliisateur : Thomas
- travail sur le design du site Web : Thomas/Ilyes
- rédaction des commentaires python : Ilyes/Emmanuel
- commentaire de l'API : Thomas
- modélisation machine learning : Ilyes/Emmanuel
- score Kaggle : Emmanuel
- rapport PowerBI - Création de la template : Thomas/Antoine
- lier les rapports PowerBI à notre API Web : Thomas
- création de la page d'accueil de l'API : Thomas
- liaison du modèle de machine learning à l'API pour la prédiction : Thomas/Emmanuel/Ilyes
- dév des rapports PowerBI : Antoine
- rédaction du fichier README.md : Ilyes/Antoine/Emmanuel/Thomas
- mise en production de la branche 'dev' : Thomas
- renseignement déploiement Application : Thomas

## Comment lancer le code 

Il n'y a pas de prérequis pour lancer le code.

## Les bibliothèques python utilisées

- import pandas as pd
- import os
- import numpy as np
- import seaborn as sns
- import matplotlib.pyplot as plt
- import scipy.stats as ss
- from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
- from sklearn.model_selection import GridSearchCV, - cross_val_score
- from sklearn.model_selection import train_test_split
- from sklearn.linear_model import LogisticRegression
- from sklearn import metrics
- from sklearn.svm import SVC
- from sklearn.svm import LinearSVC
- from sklearn.neighbors import KNeighborsClassifier
- from sklearn.linear_model import SGDClassifier
- from sklearn.model_selection import GridSearchCV, - cross_val_score
- from sklearn.pipeline import make_pipeline, make_union
- from sklearn.neural_network import MLPClassifier
- from sklearn.metrics import roc_curve
- from sklearn.metrics import make_scorer, r2_score
- from sklearn.metrics import roc_auc_score
- from sklearn.linear_model import ElasticNet, Lasso,  BayesianRidge, LassoLarsIC
- from sklearn.ensemble import RandomForestRegressor,  GradientBoostingRegressor
- from sklearn.kernel_ridge import KernelRidge
- from sklearn.pipeline import make_pipeline
- from sklearn.preprocessing import RobustScaler
- from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone
- from sklearn.model_selection import KFold, cross_val_score, train_test_split
- from sklearn.metrics import mean_squared_error
- from sklearn.metrics import r2_score
- from sklearn.metrics import mean_absolute_error
- import scipy.stats as stats
- from scipy.stats import norm
- import xgboost as xgb
- from mlxtend.regressor import StackingCVRegressor
- from xgboost import XGBRegressor
- import statsmodels.api as sm
- import pygwalker as pyg
- import seaborn as sb
- from lightgbm import LGBMRegressor
- from sklearn.linear_model import Ridge, RidgeCV
- from sklearn.svm import SVR
- from mlxtend.regressor import StackingCVRegressor

