import streamlit as st
import pandas as pd

df = pd.read_table("marketing_campaign.csv")
df['Age'] = 2023 - df['Year_Birth']
df['Kids_number'] = df['Kidhome'] + df['Teenhome']
df.isna().sum()
df['Income']=df['Income'].fillna(df['Income'].median())

st.title('Data Analysis')


st.write(df)


age = st.slider('Select Age', min_value=0, max_value=100, value=(0, 100))
income = st.slider('Select Income', min_value=0, max_value=700000, value=(0, 20000))
children = st.slider('Select Number of Children', int(df['Kids_number'].min()), int(df['Kids_number'].max()))


filtered_data = df[
    (df['Kids_number'] == children) &
    (df['Age'].between(age[0], age[1])) &
    (df['Income'].between(income[0], income[1]))
]

st.write(filtered_data)


st.title('Mean Values')


selected_param = st.selectbox('Select Parameter', ('Age', 'Income', 'Amount of kids', 'spending on meat',
                                                   "spending on fruits", "spending on sweets", "spending on wine",
                                                   "spending on fish"))


def calculate_mean(param):
    if param == 'Age':
        return int(df['Age'].mean())
    elif param == 'Income':
        return int(df['Income'].mean())
    elif param == 'Amount of kids':
        return int(df['Kids_number'].mean())
    elif param == 'spending on meat':
        return int(df['MntMeatProducts'].mean())
    elif param == 'spending on fruits':
        return int(df['MntFruitProducts'].mean())
    elif param == 'spending on sweets':
        return int(df['MntSweetProducts'].mean())
    elif param == 'spending on wine':
        return int(df['MntWines'].mean())
    elif param == 'spending on fish':
        return int(df['MntFishProducts'].mean())

mean_value = calculate_mean(selected_param)
st.write(f'Mean value of {selected_param.lower()}: {mean_value}')
