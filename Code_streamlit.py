
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.title("Title")

def display_recruitment_ratio():
    jobkorea_data = pd.read_csv('/content/drive/MyDrive/git/data_jobkorea.csv')
    saramin_data = pd.read_csv('/content/drive/MyDrive/git/data_saramin.csv')

    jobkorea_data['site'] = 'jobkorea'
    saramin_data['site'] = 'saramin'

    merged_data = pd.concat([jobkorea_data, saramin_data], axis=0, ignore_index=True)

    selected_columns = ['site', 'Col_Company', 'Col_Recruit']
    result = merged_data[selected_columns]

    #st.write("### 채용 사이트별 데이터:")
    st.dataframe(result)  # 상위 5행 출력

    count_df = result['site'].value_counts().reset_index()
    count_df.columns = ['site', 'Count']

    count_df['Ratio'] = (count_df['Count'] / count_df['Count'].sum() * 100).round(2)

    #st.write("### 채용 사이트별 채용 건수 및 비율:")
    st.dataframe(count_df)

    labels = count_df['site']
    sizes = count_df['Count']
    colors = ['#ff9999', '#66b3ff']
    explode = (0.05, 0)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=explode,
        shadow=True,
        textprops={'fontsize': 12}
    )
    ax.set_title('Recruitment Ratio', fontsize=15, pad=20)
    ax.axis('equal')

    ax.legend(
        title="Sites",
        loc="upper right",
        bbox_to_anchor=(1.2, 1)
    )

    st.pyplot(fig)

#st.title("Recruit Searching")
with st.container(border=True):
    if st.button("Recruit Searching"):
        display_recruitment_ratio()
