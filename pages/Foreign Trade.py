import streamlit as st
import requests
import json

# Web link to the JSON data



# Define a list of options
options = ["IncoTerms-2020", "Shadow Banking"]

# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)


if option == "IncoTerms-2020":
  st.write("Fuck You")

elif option == "Shadow Banking":
  st.markdown("<h4 style='text-align: center;'>Shadow Banking </h4>", unsafe_allow_html=True)

  st.write("""


    Shadow banking refers to a system of financial intermediaries that operate outside of traditional banking regulations and practices. These intermediaries provide credit, liquidity, and other financial services to clients, but are not subject to the same regulatory oversight as traditional banks.

    Examples of shadow banking activities include hedge funds, money market funds, and certain types of insurance companies, which may engage in activities such as securities lending, repurchase agreements, and structured finance transactions.

    In Bangladesh, examples of shadow banking activities include microfinance institutions, leasing companies, and non-bank financial institutions. These entities provide credit and other financial services to individuals and businesses, but are not subject to the same regulatory requirements as traditional banks.

    
    Here are some more examples of shadow banking activities and how they work:

  1. Money market funds: 
    These are mutual funds that invest in short-term, low-risk securities such as government bonds and commercial paper. They are not considered banks, but they operate like banks by taking deposits from investors and using the funds to make investments. Money market funds are typically used by investors as a safe place to park their cash, but they are not insured by the FDIC like bank deposits. In 2008, the Reserve Primary Fund, a money market fund, "broke the buck" due to its exposure to Lehman Brothers' commercial paper, which caused widespread panic in the money market fund industry.

  2. Hedge funds: 
    Hedge funds are private investment vehicles that use a variety of investment strategies to generate high returns for their investors. They are not subject to the same regulations as mutual funds, and typically require a large minimum investment. Hedge funds often use leverage (borrowed money) to increase their returns, which can make them more risky. In 1998, Long-Term Capital Management, a hedge fund that used complex derivatives trades, collapsed and had to be bailed out by the Federal Reserve.

  3. Peer-to-peer (P2P) lending: 
    P2P lending platforms connect borrowers with individual lenders who are willing to lend money. These platforms use technology to match borrowers with lenders and facilitate the lending process. P2P lending can provide borrowers with access to credit at lower interest rates than traditional banks, but the loans are not insured and the creditworthiness of the borrowers may be harder to assess. In Bangladesh, there are several P2P lending platforms such as iPay and Samadhan.
  
  4. Microfinance institutions: 
    Microfinance institutions provide financial services to low-income individuals and small businesses who may not have access to traditional banking services. These services can include loans, savings accounts, and insurance. Microfinance institutions typically charge higher interest rates than traditional banks, but they are often more flexible in their lending practices. In Bangladesh, Grameen Bank is a well-known microfinance institution that has been providing financial services to rural communities for decades.


While these shadow banking activities can provide benefits such as increased access to credit and financial services, they can also pose risks to the stability of the financial system. Because they are not subject to the same regulatory oversight as traditional banks, they may engage in riskier activities and have less transparency. Therefore, it is important for regulators to monitor and regulate shadow banking activities to ensure the stability of the financial system.

""")
  

