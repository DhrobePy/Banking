import streamlit as st

# Define a list of options
options = ["BASEL-I", "BASEL-II", "BASEL-III", "Tier-1 Capital", "Tier-2 Capital"]

# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)

# Display the selected option
if option == "BASEL-I":
    
    st.markdown("<h1 style='text-align: center;'>BASEL-I</h1>", unsafe_allow_html=True)
    st.write("""
    
    Basel I, also known as the Basel Accord, was developed in 1988 by the Basel Committee on Banking Supervision. The accord aimed to establish a set of international banking standards to ensure banks had enough capital to withstand financial shocks and reduce the risk of bank failures.  
    
    The key features of Basel I include:
        1. Minimum Capital Requirement: Basel I introduced a minimum capital requirement of 8% of a bank's risk-weighted assets. Banks were required to hold this capital in the form of Tier 1 and Tier 2 capital.
        The calculation of CAR under Basel I can be simplified as follows:
            CAR = (Tier 1 Capital + Tier 2 Capital) / Risk-Weighted Assets
        2. Risk Weighted Assets: Basel I classified assets into five risk categories and assigned them risk weights ranging from 0% to 100%. The risk weights were used to calculate the amount of capital a bank was required to hold against its assets.
        3. Uniform Standards: Basel I established uniform standards for banks across different countries, which helped to level the playing field and promote fair competition.
        
""")
    
    st.write("""
    
    Tier-1 Capital:
        Tier 1 capital is the core measure of a bank's financial strength and consists of capital that can absorb losses without a bank being required to       cease operations. The components of Tier 1 capital include:
    
        1.Common Equity Tier 1 (CET1): 
            CET1 includes a bank's common stock and retained earnings, as well as other comprehensive income. CET1 is considered the highest quality form of capital because it is fully loss-absorbing and is not subject to any restrictions on distributions or redemptions.
    
        2.Additional Tier 1 capital: 
            Additional Tier 1 capital includes instruments that can absorb losses but are more risky than CET1, such as perpetual preferred stock and contingent convertible bonds (CoCos). These instruments have features that allow them to be written down or converted to equity if the bank's capital falls below a certain level.
    
    Both CET1 and Additional Tier 1 capital are considered high-quality capital because they can absorb losses without causing a bank to become insolvent. Tier 1 capital is used to absorb losses before Tier 2 capital, which is a lower-quality form of capital.Overall, Tier 1 capital provides a measure of a bank's ability to withstand losses and continue operating without the need for external support. It is a key metric for regulators and investors in assessing a bank's financial strength and stability.
    
    """)



                                                            
    st.write("""
    
    Drawback of BASEL-I:
The main drawback of Basel I was that it did not take into account the varying degrees of risk within each asset class. This meant that some assets with the same risk weight had very different levels of risk, which led to the underestimation of the actual risk held by banks. In response to this, Basel II was introduced in 2004, which incorporated more sophisticated risk measurement techniques and revised capital requirements.


            """)
    
    
    
    
    
    
elif option == "BASEL-II":
    st.write("This is option 2.")
    
    
    
else:
    st.write("This is BASEL-III")




