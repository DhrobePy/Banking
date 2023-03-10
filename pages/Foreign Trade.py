import streamlit as st

import json

# Define a list of options
options = ["IncoTerms-2020"]

# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)



if option == "IncoTerms-2020":
  st.markdown("<h1 style='text-align: center;'>IncoTerms-2020</h1>", unsafe_allow_html=True)
  
  # Load JSON data from a file
with open('https://github.com/DhrobePy/Banking/blob/5e7633e670cd56077b7d3d22f0ed3ad8071c9109/incoterm.json') as f:
    data = json.load(f)

# Display the JSON data in a Streamlit component
st.json(data)
  st.image('https://github.com/DhrobePy/Banking/blob/5e7633e670cd56077b7d3d22f0ed3ad8071c9109/incoterm.json', caption='Simple Explanation of IncoTerms-2020')
  
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
  

