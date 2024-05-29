import streamlit as st
import helper
st.title('Restaurant Recommendation')
cuisine = st.sidebar.selectbox('Pick a Cuisine', ('Nigerian','Italian','Chinese', 'Indian','Thailand'))


if cuisine:
    response = helper.generateRestuarantNameMenu(cuisine)
    st.write(response)
    # st.header(response['restuarant_name'])
    # menus = response['menus'].split(',')
    # st.write('**Menu Items**')
    # for menu in menus:
    #     st.write('-',menu)
