import streamlit as st

st.title("Banking Terms & Conditions")


# Define a list of radio button options
options = ["Introduction to Banking ","Genearal Banking", "Credit", "Foreign Trade"]

# Add the radio buttons to the sidebar
selected_option = st.sidebar.radio("Select an option", options)

# Display the selected option in the main content area
st.write("You selected:", selected_option)
