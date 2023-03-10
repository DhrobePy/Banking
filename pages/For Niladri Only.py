import streamlit as st

def get_list():
    if 'my_list' not in st.session_state:
        # Initialize the list if it doesn't exist in session state
        st.session_state.my_list = ['Topic Name']
    return st.session_state.my_list

def add_item_to_list():
    # Create a form to add new items to the list
    new_item = st.text_input('Add new Topic to list:')
    if new_item:
        # Get the current list from session state and append the new item
        my_list = get_list()
        my_list.append(new_item)
        # Update the list in session state
        st.session_state.my_list = my_list

# Call the function to add new items to the list
add_item_to_list()

# Get the current list from session state
my_list = get_list()

# Display the list
st.write('My list:')
for item in my_list:
    st.write('- ' + item)
