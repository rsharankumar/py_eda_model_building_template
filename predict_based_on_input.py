
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from patsy import dmatrices
from sklearn.model_selection import train_test_split
import sklearn.ensemble as ske
import pickle
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

filename1 = 'Model/rf_model_class.sav'
filename2 = 'Model/rf_model_reg.sav'
filename3 = 'Model/svm_model_reg.sav'

df = pd.DataFrame(columns=["Intercept","T.Javanese", "T.Maine_Coon", "T.Manx", "T.Rex", "T.Siamese", "hair_length", "height", "number_of_vet_visits", "weight"])
parts = int(input("Enter the number of entries to be made:"))
ip = 1
for _ in range(parts):
    ip1 = input("Is the cat's Breed:\n 1 - Javanese\n 2 - Maine Coon\n 3 - Manx\n 4 - Rex\n 5 - Siamese\n")
    ip11 = np.where(ip1 == '1', 1, 0) 
    ip12 = np.where(ip1 == '2', 1, 0)
    ip13 = np.where(ip1 == '3', 1, 0)
    ip14 = np.where(ip1 == '4', 1, 0)
    ip15 = np.where(ip1 == '5', 1, 0)
    ip2 = input("Enter Hair Length:")
    ip3 = input("Enter Height:")
    ip4 = input("Enter Number of Vet Visits:")
    ip5 = input("Enter Weight:")
    #ip6 = input("Enter days from last Vet Visit:")
    df1 = pd.DataFrame(data=[[ip, ip11, ip12, ip13, ip14, ip15,ip2,ip3, ip4, ip5]],columns=["Intercept","T.Javanese", "T.Maine_Coon", "T.Manx", "T.Rex", "T.Siamese", "hair_length", "height", "number_of_vet_visits", "weight"])
    df = pd.concat([df,df1], axis=0)

df.index = range(len(df.index))

# load the model from disk
model1 = pickle.load(open(filename1, 'rb'))
model2 = pickle.load(open(filename2, 'rb'))
model3 = pickle.load(open(filename3, 'rb'))
#Making prediction for the user input
test_pred1 = model1.predict(df)
test_pred2 = model2.predict(df)
test_pred3 = model3.predict(df)
test_pred = (test_pred1 + test_pred2 + test_pred3)/3
print('Life expectancy of the cat: ', test_pred)