# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 07:56:46 2023

@author: Pedro
"""

#%% Esta celda importa las librerías necesarias 
import numpy as np #Necesaria para el manejo de vectores y matrices 
import pandas as pd #Necesaria para el manejo de datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import matplotlib.pyplot as plt

#%% Importación del DataSet
data=pd.read_csv("C:/Users/Pedro/Documents/TFG/Python/Datasets/solarpowergeneration.csv")

#Veamos las columnas del dataSet
print(data.shape)
