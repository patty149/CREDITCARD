# -*- coding: utf-8 -*-
"""creditcard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ryIfoNOV9EI9Wr8JH2m0qQQFdRTrqmnK
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

crecord = pd.read_csv('credit_record.csv')
app = pd.read_csv('application_record.csv')

app.info()

crecord.info()

app['ID'].nunique()

crecord['ID'].nunique()

len(set(crecord['ID']).intersection(set(app['ID'])))

sns.heatmap(app.isnull())

sns.heatmap(crecord.isnull())

app = app.drop_duplicates('ID', keep='last')

plt.figure(figsize=(14, 7))



gender_counts = app['CODE_GENDER'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'pink'])
plt.title('Gender Distribution')

plt.figure(figsize=(8,6))
sns.violinplot(x='FLAG_OWN_CAR', y='AMT_INCOME_TOTAL', data=app, palette='muted')
plt.title('Income Distribution by Car Ownership')
plt.xlabel('Owns Car')
plt.ylabel('Income Amount')

plt.figure(figsize=(12,6))

plt.subplot(1, 2, 1)
sns.countplot(x='FLAG_OWN_CAR', hue='CODE_GENDER', data=app, palette='Set2')
plt.title('Car Ownership by Gender')
plt.xlabel('Own Car')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
sns.countplot(x='FLAG_OWN_REALTY', hue='CODE_GENDER', data=app, palette='Set1')
plt.title('Realty Ownership by Gender')
plt.xlabel('Own Realty')
plt.ylabel('Count')

plt.figure(figsize=(10,6))
avg_income_by_age = app.groupby('AGE_YEARS')['AMT_INCOME_TOTAL'].mean().sort_index()
avg_income_by_age.plot(kind='line', color='purple', lw=2)
plt.title('Average Income by Age')
plt.xlabel('Age (Years)')
plt.ylabel('Average Income')

family_status_counts = app['NAME_FAMILY_STATUS'].value_counts()
sns.barplot(x=family_status_counts.index, y=family_status_counts.values, palette='Set2')
plt.xticks(rotation=45)
plt.title('Family Status Distribution')

plt.figure(figsize=(10,6))
sns.boxplot(x='CNT_CHILDREN', y='AMT_INCOME_TOTAL', data=app, palette='Set2')
plt.title('Income Distribution by Number of Children')
plt.xlabel('Number of Children')
plt.ylabel('Income Amount')

numeric_cols = app[['CNT_CHILDREN', 'AMT_INCOME_TOTAL', 'DAYS_BIRTH', 'DAYS_EMPLOYED', 'CNT_FAM_MEMBERS']]
correlation_matrix = numeric_cols.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')

app.drop('OCCUPATION_TYPE', axis=1, inplace=True)

ot = pd.DataFrame(app.dtypes =='object').reset_index()
object_type = ot[ot[0] == True]['index']
object_type

num_type = pd.DataFrame(app.dtypes != 'object').reset_index().rename(columns =  {0:'yes/no'})
num_type = num_type[num_type['yes/no'] ==True]['index']

a = app[object_type]['CODE_GENDER'].value_counts()
b = app[object_type]['FLAG_OWN_CAR'].value_counts()
c = app[object_type]['FLAG_OWN_REALTY'].value_counts()
d = app[object_type]['NAME_INCOME_TYPE'].value_counts()
e = app[object_type]['NAME_EDUCATION_TYPE'].value_counts()
f = app[object_type]['NAME_FAMILY_STATUS'].value_counts()
g = app[object_type]['NAME_HOUSING_TYPE'].value_counts()

print( a,"\n",b,'\n', c, '\n', d, '\n', e, '\n', f, '\n', g)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for x in app:
    if app[x].dtypes=='object':
        app[x] = le.fit_transform(app[x])

app.head(10)

app[num_type].head()

fig, ax= plt.subplots(nrows= 3, ncols = 3, figsize= (14,6))

sns.scatterplot(x='ID', y='CNT_CHILDREN', data=app, ax=ax[0][0], color= 'orange')
sns.scatterplot(x='ID', y='AMT_INCOME_TOTAL', data=app, ax=ax[0][1], color='orange')
sns.scatterplot(x='ID', y='DAYS_BIRTH', data=app, ax=ax[0][2])
sns.scatterplot(x='ID', y='DAYS_EMPLOYED', data=app, ax=ax[1][0])
sns.scatterplot(x='ID', y='FLAG_MOBIL', data=app, ax=ax[1][1])
sns.scatterplot(x='ID', y='FLAG_WORK_PHONE', data=app, ax=ax[1][2])
sns.scatterplot(x='ID', y='FLAG_PHONE', data=app, ax=ax[2][0])
sns.scatterplot(x='ID', y='FLAG_EMAIL', data=app, ax=ax[2][1])
sns.scatterplot(x='ID', y='CNT_FAM_MEMBERS', data=app, ax=ax[2][2], color= 'orange')

q_hi = app['CNT_CHILDREN'].quantile(0.999)
q_low = app['CNT_CHILDREN'].quantile(0.001)
app = app[(app['CNT_CHILDREN']>q_low) & (app['CNT_CHILDREN']<q_hi)]

q_hi = app['AMT_INCOME_TOTAL'].quantile(0.999)
q_low = app['AMT_INCOME_TOTAL'].quantile(0.001)
app= app[(app['AMT_INCOME_TOTAL']>q_low) & (app['AMT_INCOME_TOTAL']<q_hi)]

q_hi = app['CNT_FAM_MEMBERS'].quantile(0.999)
q_low = app['CNT_FAM_MEMBERS'].quantile(0.001)
app= app[(app['CNT_FAM_MEMBERS']>q_low) & (app['CNT_FAM_MEMBERS']<q_hi)]

fig, ax= plt.subplots(nrows= 3, ncols = 3, figsize= (14,6))

sns.scatterplot(x='ID', y='CNT_CHILDREN', data=app, ax=ax[0][0], color= 'orange')
sns.scatterplot(x='ID', y='AMT_INCOME_TOTAL', data=app, ax=ax[0][1], color='orange')
sns.scatterplot(x='ID', y='DAYS_BIRTH', data=app, ax=ax[0][2])
sns.scatterplot(x='ID', y='DAYS_EMPLOYED', data=app, ax=ax[1][0])
sns.scatterplot(x='ID', y='FLAG_MOBIL', data=app, ax=ax[1][1])
sns.scatterplot(x='ID', y='FLAG_WORK_PHONE', data=app, ax=ax[1][2])
sns.scatterplot(x='ID', y='FLAG_PHONE', data=app, ax=ax[2][0])
sns.scatterplot(x='ID', y='FLAG_EMAIL', data=app, ax=ax[2][1])
sns.scatterplot(x='ID', y='CNT_FAM_MEMBERS', data=app, ax=ax[2][2], color= 'orange')

crecord['Months from today'] = crecord['MONTHS_BALANCE']*-1
crecord = crecord.sort_values(['ID','Months from today'], ascending=True)
crecord.head(10)

crecord['STATUS'].value_counts()

crecord['STATUS'].replace({'C': 0, 'X' : 0}, inplace=True)
crecord['STATUS'] = crecord['STATUS'].astype('int')
crecord['STATUS'] = crecord['STATUS'].apply(lambda x:1 if x >= 2 else 0)

crecord['STATUS'].value_counts(normalize=True)

crecordgb = crecord.groupby('ID').agg(max).reset_index()
crecordgb.head()

df = app.join(crecordgb.set_index('ID'), on='ID', how='inner')
df.drop(['Months from today', 'MONTHS_BALANCE'], axis=1, inplace=True)
df.head()

df.info()

X = df.iloc[:,1:-1]
y = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)

from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
X_scaled = pd.DataFrame(mms.fit_transform(X_train), columns=X_train.columns)
X_test_scaled = pd.DataFrame(mms.transform(X_test), columns=X_test.columns)

from imblearn.over_sampling import SMOTE
oversample = SMOTE()
X_balanced, y_balanced = oversample.fit_resample(X_scaled, y_train)
X_test_balanced, y_test_balanced = oversample.fit_resample(X_test_scaled, y_test)

y_train.value_counts()

y_balanced.value_counts()

y_test.value_counts()

y_test_balanced.value_counts()

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

classifiers = {
    "LogisticRegression" : LogisticRegression(),
    "KNeighbors" : KNeighborsClassifier(),
    "SVC" : SVC(),
    "DecisionTree" : DecisionTreeClassifier(),
    "RandomForest" : RandomForestClassifier(),
    "XGBoost" : XGBClassifier()
}

train_scores = []
test_scores = []

for key, classifier in classifiers.items():
    classifier.fit(X_balanced, y_balanced)
    train_score = classifier.score(X_balanced, y_balanced)
    train_scores.append(train_score)
    test_score = classifier.score(X_test_balanced, y_test_balanced)
    test_scores.append(test_score)

print(train_scores)
print(test_scores)

xgb = XGBClassifier()
model = xgb.fit(X_balanced, y_balanced)
prediction = xgb.predict(X_test_balanced)

from sklearn.metrics import classification_report
print(classification_report(y_test_balanced, prediction))