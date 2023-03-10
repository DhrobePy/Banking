import streamlit as st

st.write("Introduction to Banking Industry, Here you will get all other regulatory informations of Banks and related industry")

import streamlit as st

# Define a list of options
options = ["BASEL-I", "BASEL-II", "BASEL-III"]

# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)

# Display the selected option
if option == "BASEL-I":
    st.markdown("<h1 style='text-align: center;'>BASEL-I'</h1>", unsafe_allow_html=True)

    st.write(""
             Basel I, also known as the Basel Accord, was developed in 1988 by the Basel Committee on Banking Supervision. The accord aimed to establish a set of international banking standards to ensure banks had enough capital to withstand financial shocks and reduce the risk of bank failures.

The key features of Basel I include:

Minimum Capital Requirement: Basel I introduced a minimum capital requirement of 8% of a bank's risk-weighted assets. Banks were required to hold this capital in the form of Tier 1 and Tier 2 capital.
Risk Weighted Assets: Basel I classified assets into five risk categories and assigned them risk weights ranging from 0% to 100%. The risk weights were used to calculate the amount of capital a bank was required to hold against its assets.
Uniform Standards: Basel I established uniform standards for banks across different countries, which helped to level the playing field and promote fair competition.
The calculation of CAR under Basel I can be simplified as follows:

CAR = (Tier 1 Capital + Tier 2 Capital) / Risk-Weighted Assets

The main drawback of Basel I was that it did not take into account the varying degrees of risk within each asset class. This meant that some assets with the same risk weight had very different levels of risk, which led to the underestimation of the actual risk held by banks. In response to this, Basel II was introduced in 2004, which incorporated more sophisticated risk measurement techniques and revised capital requirements.


             "")
    
    
    
    
elif option == "BASEL-II":
    st.write("This is option 2.")
    
    
    
else:
    st.write("This is BASEL-III")




