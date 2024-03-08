import streamlit as st
import pandas as pd
import plotly.express as px

#import streamlit_extras
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title="InformedVotr", page_icon=":ballot_box_with_ballot:", layout="wide")
st.subheader("Hi, Welcome to InformedVotr. :wave:")

# Sample data with state codes
data = {'State': ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'],
        'Value': [10, 20, 15, 25, 3, 10, 20, 15, 25, 3, 10, 20, 15, 25, 3, 10, 20, 15, 25, 3, 10, 20, 15, 25, 3, 10, 20, 15, 25, 3, 10, 20, 15, 25, 3, 10, 20, 15, 25, 3, 10, 20, 15, 25, 3, 10, 20, 15, 25, 3]}
#data = {'State': ['CA', 'MI'], 'Value': [st.button("Reset2", type="primary"), st.button("Reset", type="primary")]}
df = pd.DataFrame(data)
#if st.button('CA'):
#    st.write("CALIFORNIA")
#if st.button('MI'):
#    st.write("MICHIGAN")

# 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA'
# 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD'
# 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH'
# 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC'
# 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])

with col1:
    st.button('AK')
    st.button('HI')
    st.button('ME')
    st.button('NJ')
    st.button('SD')
with col2:
    st.button('AL')
    st.button('IA')
    st.button('MI')
    st.button('NM')
    st.button('TN')
with col3:
    st.button('AR')
    st.button('ID')
    st.button('MN')
    st.button('NV')
    st.button('TX')
with col4:
    st.button('AZ')
    st.button('IL')
    st.button('MO')
    st.button('NY')
    st.button('UT')
with col5:
    #st.button('CA')
    if st.button('CA'):
        switch_page("THISBETTERWORK")
    st.button('IN')
    st.button('MS')
    st.button('OH')
    st.button('VA')
with col6:
    st.button('CO')
    st.button('KS')
    st.button('MT')
    st.button('OK')
    st.button('VT')
with col7:
    st.button('CT')
    st.button('KY')
    st.button('NC')
    st.button('OR')
    st.button('WA')
with col8:
    st.button('DE')
    st.button('LA')
    st.button('ND')
    st.button('PA')
    st.button('WI')
with col9:
    st.button('FL')
    st.button('MA')
    st.button('NE')
    st.button('RI')
    st.button('WV')
with col10:
    st.button('GA')
    st.button('MD')
    st.button('NH')
    st.button('SC')
    st.button('WY')


#if st.button('CA'):
    #switch_page("State.py")


# Create a choropleth map
fig = px.choropleth(
    df,
    locations='State',
    locationmode='USA-states',
    #color='Value',
    scope="usa",
    color_continuous_scale="Viridis",
    title='Click on each state to learn more about state-specific bill proposals.'
)

# Render the map using Streamlit and handle click events
click = st.plotly_chart(fig, use_container_width=True, sharing='streamlit', when='always', key="choropleth_map")

# Handle click events
if click:
    click_data = st.session_state.click_data
    if click_data and 'points' in click_data and click_data['points']:
        clicked_state = click_data['points'][0]['location']
        st.write(f"You clicked on {clicked_state}")
