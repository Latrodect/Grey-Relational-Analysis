# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 19:12:37 2019

@author: hbaha
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

"""
Take Data with csv and Normalizing Data

"""
print("Enter the full file path of the csv file of the data you want to find the gra of.")
csv_Path = input("Full path of csv file:")
csv = pd.read_csv(csv_Path)

min_max_scaler = preprocessing.MinMaxScaler()
print(csv)
ColsSize = int(input("How many Max Normalization column you got:"))
ListsEbe = []
for i in range(ColsSize):
    Ebeis = input("Max Normalization column names :")
    ListsEbe.append(Ebeis)
X = csv.drop(ListsEbe,axis=1)
Adding = []
for z in range(len(ListsEbe)):
    Max = csv[ListsEbe[z]].max()
    Min = csv[ListsEbe[z]].min()
    Fark = Max - Min
    Normalized = ((csv[ListsEbe[z]] - Min) / Fark)
    Adding.append(1 - Normalized)

EbeiDataFrame = pd.DataFrame(Adding)
csv.to_excel('İnputTable.xlsx')
Scaled = min_max_scaler.fit_transform(X)
df = pd.DataFrame(Scaled)
df.to_excel('ScaledData.xlsx')

"""
Calculate Grey Relational Coefficient
"""
List = []
for p in range(len(ListsEbe)):
    List.append(p)
EbeiDataFrameT = EbeiDataFrame.T
EbeiDataFrameT.columns = List 
Renamed = EbeiDataFrameT
countEb = len(EbeiDataFrameT.columns)
Sequence_list2 = []
DeltaMin= 0
DeltaMax = 1
Theta = 0.5
cap = []
for i in range(countEb):
    df_Drop_z = Renamed[i]
    df_Drop_z_Max = df_Drop_z.max()
    df_Drop_z_Min = df_Drop_z.min()
    Standart_Deviation_Sequence = []
    Standart_Deviation_b = df_Drop_z_Max - df_Drop_z
    pow_Total = DeltaMin + Theta
    inline_Total = (Theta * df_Drop_z_Max) + df_Drop_z
    GreyRelationalCoefficient = (((Theta * df_Drop_z_Max) + df_Drop_z_Min) / (df_Drop_z + (Theta * df_Drop_z_Max)))
  
    Sequence_list2.append(GreyRelationalCoefficient)
DataFrameCoefficient3 = pd.DataFrame(Sequence_list2)
DataFrameTransposed4 = DataFrameCoefficient3.T 




count = len(df.columns)
count2 = count
Sequence_list = []
DeltaMin= 0
DeltaMax = 1
Theta = 0.5
cap = []
for i in range(count):
    df_Drop_a = df[i]
    df_Drop_a_Max = df_Drop_a.max()
    df_Drop_a_Min = df_Drop_a.min()
    Standart_Deviation_Sequence = []
    Standart_Deviation_b = df_Drop_a_Max - df_Drop_a
    pow_Total = DeltaMin + Theta
    inline_Total = (Theta * df_Drop_a_Max) + df_Drop_a
    GreyRelationalCoefficient = (((Theta * df_Drop_a_Max) + df_Drop_a_Min) / (df_Drop_a + (Theta * df_Drop_a_Max)))
  
    Sequence_list.append(GreyRelationalCoefficient)
DataFrameCoefficient = pd.DataFrame(Sequence_list)
DataFrameTransposed = DataFrameCoefficient.T 
DataFrameTransposed2 = DataFrameCoefficient.T 
for v in range(len(Adding)):
    DataFrameTransposed[count2] = DataFrameTransposed4[v]
    count2 = count2 + 1

DataFrameTransposed.to_excel('GrayRelationalAnalysisCoefficient.xlsx')
print("-------------------------------------------------------------------------------------")
print("The maximum normalization columns you select are added to the bottom of the list. You should pay attention to this when giving your column weights.")
print("-------------------------------------------------------------------------------------")
print(DataFrameTransposed)
CountFor = len(DataFrameTransposed.columns)
Total = np.zeros((CountFor,1))
Totals = 0
for x in range(CountFor):
    w = float(input("Give Weights for Each Columns:"))
    DataFrameColumnSums = DataFrameTransposed[x]
    Columns = DataFrameColumnSums * w 
    DataFrameTransposed[x] = Columns
DataFrameTransposed['RANK'] = DataFrameTransposed.sum(axis=1)
DataFrameTransposed.to_excel('GreyRelationalRank.xlsx')
print(DataFrameTransposed)

""" Plotting GRA RANK  """

Counting = len(DataFrameTransposed.index)
y_pos = np.arange(Counting)
performance = DataFrameTransposed['RANK']
plt.scatter(y_pos,performance)
plt.ylabel('RANKS')
plt.title('Grey Relational Grade')
plt.savefig('GRA')
plt.show()


    


