import streamlit as st

# Define a list of options
options = ["BASEL-I", "BASEL-II", "BASEL-III", "Tier-1 Capital", "Tier-2 Capital","Nano Lending"]

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
    
    Drawback of BASEL-I:
The main drawback of Basel I was that it did not take into account the varying degrees of risk within each asset class. This meant that some assets with the same risk weight had very different levels of risk, which led to the underestimation of the actual risk held by banks. In response to this, Basel II was introduced in 2004, which incorporated more sophisticated risk measurement techniques and revised capital requirements.


            """)
    
    
    
    
    
    
elif option == "BASEL-II":
    st.write("This is option 2.")
    
elif option == "Tier-1 Capital":
    st.write("""
    
    Tier-1 Capital:
        Tier 1 capital is the core measure of a bank's financial strength and consists of capital that can absorb losses without a bank being required to       cease operations. The components of Tier 1 capital include:
    
        1.Common Equity Tier 1 (CET1): 
            CET1 includes a bank's common stock and retained earnings, as well as other comprehensive income. CET1 is considered the highest quality form of capital because it is fully loss-absorbing and is not subject to any restrictions on distributions or redemptions.
    
        2.Additional Tier 1 capital: 
            Additional Tier 1 capital includes instruments that can absorb losses but are more risky than CET1, such as perpetual preferred stock and contingent convertible bonds (CoCos). These instruments have features that allow them to be written down or converted to equity if the bank's capital falls below a certain level.
    
    Both CET1 and Additional Tier 1 capital are considered high-quality capital because they can absorb losses without causing a bank to become insolvent. Tier 1 capital is used to absorb losses before Tier 2 capital, which is a lower-quality form of capital.Overall, Tier 1 capital provides a measure of a bank's ability to withstand losses and continue operating without the need for external support. It is a key metric for regulators and investors in assessing a bank's financial strength and stability.
    
    """)

elif option== "Nano Lending":
    st.markdown("<h1 style='text-align: center;'>Nano Lending</h1>", unsafe_allow_html=True)
    
    st.write("""
    
    Nano lending, also known as microfinance or microcredit, is a type of lending that provides small loans to individuals or businesses that do not have access to traditional banking services. The concept of microcredit was first developed by economist Muhammad Yunus in the 1970s in Bangladesh, and it has since become a popular form of lending in developing countries around the world.

The idea behind nano lending is to provide small loans to individuals who lack collateral or a credit history, making it difficult for them to access traditional bank loans. These loans are typically used to start or expand small businesses or to finance basic needs such as housing, education, or healthcare.

In Bangladesh, microcredit has played a significant role in reducing poverty and empowering women. The Grameen Bank, founded by Muhammad Yunus in 1983, has provided microcredit to millions of poor people, especially women, in Bangladesh. The bank operates on the principle of "group lending," where small groups of borrowers are responsible for each other's loans, creating a system of mutual support and accountability.

Another example of nano lending in Bangladesh is BRAC, a development organization that provides microfinance services to poor people in rural areas. BRAC's microfinance program includes not only loans but also savings, insurance, and financial literacy training, creating a comprehensive approach to financial inclusion.

Overall, nano lending has emerged as a powerful tool for poverty reduction and economic empowerment, especially in developing countries. It has helped millions of people to access credit and build their own businesses, improving their standard of living and contributing to economic growth.


""")

    
    
else:
    st.write("This is BASEL-III")




