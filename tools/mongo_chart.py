import streamlit as st
import pandas as pd
import altair as alt
from tools.mongo_tools import mongo_db


def st_mongo_chart():
    records = mongo_db.get_records() 

    # Prepare the DataFrame with custom labels
    data = []
    for record in records:
        day = pd.to_datetime(record['timestamp']).strftime("%Y-%m-%d")
        tag = record.get('tag', 'none')
        model = record.get('model', 'none')  # Use 'none' if 'model' is not in record

        # Determine the label based on the tag
        if tag == 'feedback':
            label = 'feedback'
        elif tag == 'generated_text':
            label = model
        else:
            print(f"Unknown tag: {tag}")
            print(record)

        data.append({'day': day, 'label': label, 'count': 1})

    df = pd.DataFrame(data)
    
    if df.empty:
        return

    # Aggregate counts by day and label
    agg_df = df.groupby(['day', 'label']).count().reset_index()

    chart = alt.Chart(agg_df).mark_bar().encode(
        x='day:T',  # X-axis displays the day
        y='count:Q',  # Y-axis shows the count
        color=alt.Color('label:N',  # Use 'label' for color encoding
                        legend=alt.Legend(title='Labels', orient='bottom', direction='horizontal')),
        tooltip=['day', 'label', 'count']  # Tooltip shows day, label, and count
    ).properties(
        width=600,
        height=400
    )

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)