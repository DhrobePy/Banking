import streamlit as st

# Define a list of options
options = ["IncoTerms-2020"]

# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)



if option == "IncoTerms-2020":
  st.markdown("<h1 style='text-align: center;'>IncoTerms-2020</h1>", unsafe_allow_html=True)
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
  

