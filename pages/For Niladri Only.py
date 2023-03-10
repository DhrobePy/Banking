import streamlit as st

def get_list():
    if 'my_list' not in st.session_state:
        st.session_state.my_list = ['Topic 1']
    return st.session_state.my_list

def add_item_to_list():
    new_item = st.text_input('Add new Topic to the list:')
    if new_item:
        my_list = get_list()
        my_list.append(new_item)
        st.session_state.my_list = my_list

def delete_item_from_list():
    my_list = get_list()
    item_to_delete = st.selectbox('Select a topic to delete that is already included in timeline:', my_list)
    if st.button('Delete'):
        my_list.remove(item_to_delete)
        st.session_state.my_list = my_list

add_item_to_list()
delete_item_from_list()

my_list = get_list()

st.write('Topics to cover:')
for item in my_list:
    st.write('- ' + item)
