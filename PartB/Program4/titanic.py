import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

titanic_df = pd.read_csv('titanictrain.csv')

# Convert Survived Column to strings for easier reading
titanic_df['Survived'] = titanic_df['Survived'].map({
    0: 'Died',
    1: 'Survived'
})

print("**** Headers before dropping columns ****")
print(titanic_df.head(5))

print("\n**** Data Transformation ****\n")

print("**** Headers after dropping columns - inplace ****")
titanic_df.drop(['Parch', 'PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
print(titanic_df.head(5))

print("**** Headers after dropping colums - reassign ****")
titanic_df = titanic_df.drop(['SibSp', 'Fare'], axis=1)
print(titanic_df.head(5))

titanic_df['Pclass'] = titanic_df['Pclass'].map({
    1: 'Luxury Class',
    2: 'Economy Class',
    3: 'Lower Class'
})

print("**** Headers after transforming Pclass column ****")
print(titanic_df.head(5))

print("**** Headers after adding default value for Embarked column ****")
titanic_df['Embarked'].fillna('S')

titanic_df['Embarked'] = titanic_df['Embarked'].map({
    'C':'Cherbourg',
    'Q':'Queenstown',
    'S':'Southmpton'
})

print("**** Headers after transforming Embarked column")
print(titanic_df.head(5))


print("\n**** Data Visualization ****\n")
print("Visualization #1 : Survival Rate based on Passenger Sitting Class")

ax = sns.countplot(x='Pclass', hue='Survived', palette='Set1', data=titanic_df)
ax.set(title='Passenger status (Survived/Died) against Passenger Class', xlabel='Passenger Class', ylabel='Total')
plt.show()

print("Visualization #2 : Survival Rate based on Gender")
print(pd.crosstab(titanic_df['Sex'], titanic_df.Survived))
ax = sns.countplot(x='Sex', hue='Survived', palette='Set2', data=titanic_df)
ax.set(title='Total survivors according to sex', xlabel='Sex', ylabel='Total')
plt.show()

print("Visualization #3 : Survival Rate Based on Passenger Age Group")

interval = (0,18,35,60,120)
categories = ['Child', 'Adult', 'Middle-Aged', 'Elder']

titanic_df['Age_cuts'] = pd.cut(titanic_df.Age, interval, labels = categories)

ax = sns.countplot(x = 'Age_cuts', data = titanic_df, hue='Survived', palette='Set3')

ax.set(xlabel='Age Categorical', ylabel='Total', title='Age Categorical Survival Distribution')
plt.show()

print("Visualization #4 : Survival Rate Based on Passenger Embarked Port")
print(pd.crosstab(titanic_df['Embarked'], titanic_df.Survived))

ax = sns.countplot(x='Embarked', hue='Survived', palette='Set1', data=titanic_df)
ax.set(title='Survuval distribution according to Embarkment place', xlabel='Embarkment Place', ylabel='Survived')
plt.show()
