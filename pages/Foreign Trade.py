import streamlit as st
import requests
import json

# Web link to the JSON data



# Define a list of options
options = ["IncoTerms-2020", "Shadow Banking"]

# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)


if option == "IncoTerms-2020":
  st.markdown("<h1 style='text-align: center;'>IncoTerms-2020</h1>", unsafe_allow_html=True)

  st.image('https://myseatime.com/blogadm/wp-content/uploads/2015/12/Incoterms.jpg', caption='Simple Explanation of IncoTerms-2020')
  
  st.write("""
           Incoterms, or International Commercial Terms, are standardized terms used in international trade to define the responsibilities of buyers and sellers with regard to the delivery of goods. The latest version of Incoterms, Incoterms 2020, came into effect on January 1, 2020. Here is a list of the 11 Incoterms 2020, along with a brief explanation of each:

  1. EXW (Ex Works): 
    The seller is responsible for making the goods available at their premises. The buyer is responsible for all costs and risks associated with transporting the goods from the seller's premises to their final destination.

  2. FCA (Free Carrier): 
    The seller is responsible for delivering the goods to a carrier or other nominated party at a specified location. The buyer is responsible for all costs and risks associated with transporting the goods from the specified location to their final destination.
  
  3. FAS (Free Alongside Ship): 
    The seller is responsible for delivering the goods alongside a vessel at a specified port. The buyer is responsible for loading the goods onto the vessel and for all costs and risks associated with transporting the goods from the port to their final destination.
  
  4. FOB (Free on Board): 
    The seller is responsible for delivering the goods onto a vessel at a specified port. The buyer is responsible for all costs and risks associated with transporting the goods from the port to their final destination.
    
  5. CFR (Cost and Freight): 
    The seller is responsible for delivering the goods onto a vessel at a specified port and for paying the cost of freight to the port of destination. The buyer is responsible for all costs and risks associated with transporting the goods from the port to their final destination.

  6. CIF (Cost, Insurance and Freight): 
    The seller is responsible for delivering the goods onto a vessel at a specified port and for paying the cost of freight and insurance to the port of destination. The buyer is responsible for all costs and risks associated with transporting the goods from the port to their final destination.

  7. CPT (Carriage Paid To): 
    The seller is responsible for delivering the goods to a carrier or other nominated party at a specified location and for paying the cost of carriage to the destination. The buyer is responsible for all costs and risks associated with transporting the goods from the destination to their final destination.

  8. CIP (Carriage and Insurance Paid To): 
    The seller is responsible for delivering the goods to a carrier or other nominated party at a specified location and for paying the cost of carriage and insurance to the destination. The buyer is responsible for all costs and risks associated with transporting the goods from the destination to their final destination.
    
  9. DAP (Delivered At Place): 
    The seller is responsible for delivering the goods to a specified location at the destination. The buyer is responsible for all costs and risks associated with transporting the goods from the specified location to their final destination.

  10. DPU (Delivered at Place Unloaded): 
    The seller is responsible for delivering the goods to a specified location at the destination and unloading them. The buyer is responsible for all costs and risks associated with transporting the goods from the specified location to their final destination.
    
  11. DDP (Delivered Duty Paid): 
    The seller is responsible for delivering the goods to a specified location at the destination and for paying all costs associated with importing the goods, including taxes and customs duties. The buyer is responsible for unloading the goods and for all costs and risks associated with transporting the goods from the specified location to their final destination.


It's important to note that Incoterms do not cover all aspects of international trade, such as payment terms and intellectual property rights. They are intended to be a standardized set of terms to help facilitate the delivery of goods, and should be used in conjunction with other relevant trade agreements and contracts.

""")
  st.markdown("<h2 style='text-align: center;'>IncoTerms Based on Risk on Buyers Part</h2>", unsafe_allow_html=True)
  st.write("""
  
  Here's a list of Incoterms based on the level of risk they carry for the buyer, ranked from least to most risky:

  1. EXW (Ex Works): 
    This term carries the least amount of risk for the buyer, as the seller's responsibility ends when they make the goods available at their premises. The buyer is responsible for all costs and risks associated with transporting the goods from the seller's premises to the final destination.
    
  2. FCA (Free Carrier): 
    Under this term, the seller delivers the goods to a carrier or a named place, and the buyer assumes the risk from that point onwards. However, the buyer is responsible for arranging and paying for the transportation of the goods from the named place.
  
  3. CPT (Carriage Paid To): 
    Under this term, the seller delivers the goods to a carrier or a named place, and is responsible for the cost of transportation to the destination. However, the buyer assumes the risk from the point the goods are handed over to the carrier.

  4. CIP (Carriage and Insurance Paid To): 
    This term is similar to CPT, but the seller is also responsible for obtaining insurance for the goods during transportation.
  5. DAT (Delivered at Terminal): 
    Under this term, the seller delivers the goods to a named terminal at the destination, and is responsible for all costs and risks associated with transporting the goods to that point. The buyer assumes the risk from the point the goods are unloaded at the terminal.

  6. DAP (Delivered at Place): 
    Under this term, the seller delivers the goods to a named place at the destination, and is responsible for all costs and risks associated with transporting the goods to that point. The buyer assumes the risk from the point the goods are unloaded at the named place.
  7. DDP (Delivered Duty Paid): 
    This term carries the highest level of risk for the buyer, as the seller is responsible for delivering the goods to the destination and paying all associated costs, including customs duties and taxes. The buyer assumes the risk only when the goods are made available at the destination.
  """)
  st.markdown("<h3 style='text-align: center;'>The seven Incoterms® 2020 rules for any mode(s) of transport are: </h3>", unsafe_allow_html=True)
  
  st.image('https://myseatime.com/blogadm/wp-content/uploads/2015/12/Incoterms-mode-of-transport.jpg', caption="Mode of Transport")
  
  st.write("""
  
  The seven Incoterms® 2020 rules for any mode(s) of transport are: 

    EXW - Ex Works (insert place of delivery)

    FCA  - Free Carrier (Insert named place of delivery) 

    CPT  - Carriage Paid to (insert place of destination) 

    CIP -  Carriage and Insurance Paid To (insert place of destination)  

    DAP - Delivered at Place (insert named place of destination)  

    DPU - Delivered at Place Unloaded (insert of place of destination)  

    DDP - Delivered Duty Paid (Insert place of destination).  

    Note: the DPU Incoterms replaces the old DAT, with additional requirements for the seller to unload the goods from the arriving means of transport. 

""")
st.markdown("<h4 style='text-align: center;'>The four Incoterms® 2020 rules for Sea and Inland Waterway Transport are:  </h4>", unsafe_allow_html=True)

st.write("""
     FAS - Free Alongside Ship (insert name of port of loading) 

     FOB - Free on Board (insert named port of loading) 

     CFR - Cost and Freight (insert named port of destination) 

     CIF -  Cost Insurance and Freight (insert named port of destination)
     
     """)

elif option=="Shadow Banking":
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
  

