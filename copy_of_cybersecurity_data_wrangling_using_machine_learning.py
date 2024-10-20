# -*- coding: utf-8 -*-
"""Copy of cybersecurity_data_wrangling_using_machine-learning

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1woU5YQ_-NDrtCOBuGb6OANsIiCCmUV7m
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ipaddress
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency
from datetime import datetime, timedelta
import math
import missingno as msno
plt.style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')



df=pd.read_csv('/Cybersecurity_attacks.csv')
df.shape

df.columns

df.head(4)

df[['Start Time','Last Time']] = df['Time'].str.split('-',expand=True)
df.head(5)

df.shape

df['.'].unique()

df = df.drop(['.','Time'],axis=1)
df.head()

df.shape

figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,5))
msno.matrix(df, ax=ax1,sparkline=False, color=(0.1, 0.25, 0.35))
msno.bar(df, ax=ax2, color=(0.25, 0.7, 0.25))
plt.show()

df.isnull().sum()

df["Attack subcategory"] = df ["Attack subcategory"].fillna("Not Registered yet")

df.isnull().sum()

df[pd.isnull(df).any(axis=1)].shape

df[df.duplicated()].shape

print('Dimensions before dropping duplicated rows:' + str(df.shape))
df= df.drop(df[df.duplicated()].index)
print('Dimensions after dropping duplicated rows:' + str(df.shape))

df[df.duplicated()]

invalid_SP = (df['Source Port'] < 0) | (df['Source Port'] > 65535)
invalid_DP = (df['Destination Port'] < 0) | (df['Destination Port'] > 65535)
df[invalid_SP | invalid_DP]

df = df[~(invalid_SP | invalid_DP)].reset_index(drop=True)
df.shape

print('Total number of different Protocols:',len(df['Protocol'].unique()))
print('Total number of different Attack categories:',len(df['Attack category'].unique()))
df['Protocol'].unique()

df['Attack category'].unique()

df['Protocol'] = df['Protocol'].str.upper().str.strip()
df['Attack category'] = df['Attack category'].str.upper().str.strip()
df['Attack category'] = df['Attack category'].str.strip().replace('BACKDOORS, BACKDOOR')

df

print('total number of diffrent Protocols:',len(df['Protocol'].unique()))
print('total number of diffrent Attack categorise:',len(df['Attack category'].unique()))

df[pd.isnull(df['Attack Reference'])][:5]

print(df[pd.isnull(df['Attack Reference'])]['Attack category'].value_counts())

print(df['Attack category'].value_counts())

((df[pd.isnull(df['Attack Reference'])] ['Attack category'].value_counts()/df['Attack category'].value_counts())*100).dropna().sort_values(ascending=True)

tcp_ports = pd.read_csv('TCP-ports.csv')
tcp_ports['Service'] = tcp_ports['Service'].str.upper()
tcp_ports.head()

# @title Port

from matplotlib import pyplot as plt
tcp_ports['Port'].plot(kind='hist', bins=20, title='Port')
plt.gca().spines[['top', 'right',]].set_visible(False)

print('Dimensions before merging dataframes: ', (df.shape))
newdf = pd.merge(df, tcp_ports[['Port', 'Service']], left_on="Destination Port", right_on="Port", how="left")
newdf = newdf.rename(columns={'Service': 'Destination Port Service'})
print("Dimensions after merging dataframes: " + str(newdf.shape))

newdf = newdf.drop(columns=['Port']) # Changed 'port' to 'Port'
newdf.head()

newdf['Attack category'].unique()

newdf['Attack subcategory'].value_counts()

newdf['Attack category'].value_counts()*100/newdf['Attack category'].value_counts().sum()

