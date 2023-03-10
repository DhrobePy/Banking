import streamlit as st

st.write("Welcome to General Banking Page. Please select desired options in sidebar to explore GB related queries")


# Define a list of options
options = ["Negotiable Instrument Act"]

# Define a function to add a new option to the list
def add_option(new_option):
    options.append(new_option)
    st.session_state.options = options  # Update session state

# Initialize session state
if "options" not in st.session_state:
    st.session_state.options = options

# Add the form to the sidebar
new_option = st.sidebar.text_input("Add a Topic:")
if st.sidebar.button("Add"):
    add_option(new_option)

# Display the list of options in the main content area
st.radio("Topics:", st.session_state.options)

