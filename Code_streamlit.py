
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(layout="wide")
st.title("Recruitment Dashboard")

if st.button("Recruit Searching"):
 
    jobkorea_data = pd.read_csv('data_jobkorea.csv') 
    saramin_data = pd.read_csv('data_saramin.csv')

    jobkorea_data['site'] = 'jobkorea'
    saramin_data['site'] = 'saramin'
    merged_data = pd.concat([jobkorea_data, saramin_data], axis=0, ignore_index=True)

    selected_columns = ['site', 'Col_Company', 'Col_Recruit']
    result = merged_data[selected_columns]


    st.subheader("Merged Data")
    st.dataframe(result)

    count_df = result['site'].value_counts().reset_index()
    count_df.columns = ['site', 'Count']
    count_df['Ratio'] = (count_df['Count'] / count_df['Count'].sum() * 100).round(2)

    st.subheader("Site Statistics")
    st.dataframe(count_df)

    st.subheader("Recruitment Ratio")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(
        count_df['Count'],
        labels=count_df['site'],
        autopct='%1.1f%%',
        startangle=90,
        colors=['#ff9999', '#66b3ff'],
        explode=(0.05, 0),
        shadow=True,
        textprops={'fontsize': 12}
    )
    ax.set_title('Recruitment Ratio', fontsize=15, pad=20)
    ax.axis('equal')
    ax.legend(title="Sites", loc="upper right", bbox_to_anchor=(1.2, 1))
    st.pyplot(fig) 
