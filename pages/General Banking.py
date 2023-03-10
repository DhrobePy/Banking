import streamlit as st

st.write("Welcome to General Banking Page. Please select desired options in sidebar to explore GB related queries")


options = ["Negotiable Instument Act"]

# Define a function to add a new option to the list
def add_option(new_option):
    options.append(new_option)

# Add the form to the sidebar
new_option = st.sidebar.text_input("Add a new Topic:")
if st.sidebar.button("Add"):
    add_option(new_option)

# Display the list of options in the main content area
st.sidebar.radio(options)
