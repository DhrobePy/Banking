import streamlit as st
import requests
import json

# Web link to the JSON data



# Define a list of options
options = ["IncoTerms-2020","Letter of Credit", "Types of LC","Minimizing Risk"]

# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)

if option=="Minimizing Risk":
  st.markdown("<h1 style='text-align: center;'>Minimizing Risk in LC </h1>", unsafe_allow_html=True)
  st.write("""
  
  In finance, hedging, arbitrage, and speculation are three different strategies used by investors and traders to manage risk and make profits. Here's a brief explanation of each strategy:

Hedging: Hedging is a risk management strategy that involves taking an offsetting position to a primary investment with the aim of reducing the risk of loss. The primary investment may be subject to price fluctuations or other risks, so a hedging position is taken to reduce or eliminate those risks. Hedging can be done using derivatives such as futures, options, and swaps.
Arbitrage: Arbitrage is a strategy that involves taking advantage of price discrepancies in different markets to make a profit. An arbitrageur buys an asset in one market and sells it in another market where the price is higher, making a profit from the price difference. Arbitrage opportunities usually arise due to inefficiencies in the market, and the strategy requires quick execution and a thorough understanding of market conditions.
Speculation: Speculation is a strategy that involves taking a position in an asset with the aim of profiting from price movements. Unlike hedging, speculation is a high-risk strategy that is not focused on risk management but on profit maximization. Speculators use a range of techniques, such as technical analysis, fundamental analysis, and market sentiment analysis, to identify potential price movements and take positions accordingly.
Overall, these strategies are used by traders and investors in different ways, and each strategy has its own risks and rewards.
  
  """)

if option=="Types of LC":
  st.markdown("<h1 style='text-align: center;'>Types of LC</h1>", unsafe_allow_html=True)
  st.write("""

Following are the most commonly used or known types of letter of credit:-

  1.  Revocable Letter of Credit

  2.  Irrevocable Letter of Credit

  3.  Confirmed Letter of Credit

  4.  Unconfirmed Letter of Credit

  5.  LC at Sight

  6.  Usance LC or Deferred Payment LC

  7.  Back to Back LC

  8.  Transferable Letter of Credit

  9.  Un-transferable Letter of Credit

  10. Standby Letter of Credit

  11. Freely Negotiable Letter of Credit

  12. Revolving Letter of Credit

  13. Red Clause LC

  14. Green Clause LC
  
  """)
  
  st.markdown("<h1 style='text-align: center;'>Payment method of LC</h1>", unsafe_allow_html=True)
  st.write("""
  There are several payment methods that can be used in a Letter of Credit (LC) transaction, including:

  1.  Sight Payment: 
    Under a sight LC, the seller can receive payment as soon as the required documents are presented and verified by the bank. The payment is made immediately, typically within a few days, after the documents are submitted.

  2.  Deferred Payment: 
    With a deferred payment LC, the seller receives payment at a specified future date, which is usually after a certain period of time, such as 30, 60, or 90 days after the documents are presented.
  
  3.  Acceptance: 
    Under an acceptance LC, the seller can receive payment by accepting a time draft, which is a type of bill of exchange that requires payment at a specified future date. The seller may discount the draft with a bank to receive early payment.

  4.  Negotiation: 
    The seller may negotiate the LC with the bank, which means that the bank will purchase the documents from the seller and pay them the amount due under the LC. The bank may take a fee or discount the payment.
The payment method used in a particular LC transaction depends on the agreement between the buyer and seller, as well as the nature of the transaction and the parties' preferences. It is important for all parties involved to understand the payment terms and conditions specified in the LC to ensure that the transaction proceeds smoothly and without any disputes or delays.

  
  """)
  
if option=="Letter of Credit":
  st.markdown("<h1 style='text-align: center;'>Letter of Credit</h1>", unsafe_allow_html=True)
  st.write("""
  
  A letter of credit or LC is a written document issued by the importer’s bank (opening bank) on importer’s behalf. Through its issuance, the exporter is assured that the issuing bank will make a payment to the exporter for the international trade conducted between both the parties.

The importer is the applicant of the LC, while the exporter is the beneficiary. In an LC, the issuing bank promises to pay the mentioned amount as per the agreed timeline and against specified documents.

A guiding principle of an LC is that the issuing bank will make the payment based solely on the documents presented, and they are not required to physically ensure the shipping of the goods. If the documents presented are in accord with the terms and conditions of the LC, the bank has no reason to deny the payment.
  """)
  st.markdown("<h1 style='text-align: center;'>Features / Characteristics of letter of credit</h1>", unsafe_allow_html=True)
  st.write("""
  A letter of credit is identified by certain principles. These principles remain the same for all kinds of letters of credit. The main characteristics of letters of credit are as follows:

    1.  Negotiability
A letter of credit is a transactional deal, under which the terms can be modified/changed at the parties assent. In order to be negotiable, a letter of credit should include an unconditional promise of payment upon demand or at a particular point in time.

    2.  Revocability
A letter of credit can be revocable or irrevocable. Since a revocable letter of credit cannot be confirmed, the duty to pay can be revoked at any point of time. In an irrevocable letter of credit, all the parties hold power, it cannot be changed/modified without the agreed consent of all the people.

    3.  Transfer and Assignment
A letter of credit can be transferred, also the beneficiary has the right to transfer/assign the LC. The LC will remain effective no matter how many times the beneficiary assigns/transfers the LC.

    4.  Sight & Time Drafts
The beneficiary will only receive the payment upon maturity of letter of credit from the issuing bank when he presents all the drafts & the necessary documents.
  
  """)
  st.markdown("<h1 style='text-align: center;'>Documents required for a Letter of Credit</h1>", unsafe_allow_html=True)
  st.write("""
  
        1.  Shipping Bill of Lading
        2.  Airway Bill
        3.  Commercial Invoice
        4.  Insurance Certificate
        5.  Certificate of Origin
        6.  Packing List
        7.  Certificate of Inspection
        
        """)
  
  st.markdown("<h1 style='text-align: center;'>Parties involved in an LC</h1>", unsafe_allow_html=True)
  st.write("""
    Main parties involved:

      1.  Applicant :
        An applicant (buyer) is a person who requests his bank to issue a letter of credit.

      2.  Beneficiary :
        A beneficiary is basically the seller who receives his payment under the process.
        
      3.  Issuing bank :
        The issuing bank (also called an opening bank) is responsible for issuing the letter of credit at the request of the buyer.
        
      4.  Advising bank:
        The advising bank is responsible for the transfer of documents to the issuing bank on behalf of the exporter and is generally located in the country of the exporter.

      Other parties involved in an LC arrangement:

      5.  Confirming bank:
        The confirming bank provides an additional guarantee to the undertaking of the issuing bank. It comes into the picture when the exporter is not satisfied with the assurance of the issuing bank.

      6.  Negotiating bank :
        The negotiating bank negotiates the documents related to the LC submitted by the exporter. It makes payments to the exporter, subject to the completeness of the documents, and claims reimbursement under the credit.
      (Note:- Negotiating bank can either be a separate bank or an advising bank)

      7.  Reimbursing bank:
        The reimbursing bank is where the paying account is set up by the issuing bank. The reimbursing bank honors the claim that settles the negotiation/acceptance/payment coming in through the negotiating bank.
      
      8.  Second Beneficiary The second beneficiary is one who can represent the original beneficiary in their absence. In such an eventuality, the exporter’s credit gets transferred to the second beneficiary, subject to the terms of the transfer.
      
      """)
  st.markdown("<h3 style='text-align: center;'>Process of Issung LC </h3>", unsafe_allow_html=True)
  
  st.image('https://images.ctfassets.net/vkoe68wv76dt/7t4GJfpPwSzOd9wDIQzGxJ/8d00935317e93f11ddc5cbfd2fce4456/Letter_of_Credit_-_Process_Flow_Chart__1___1_.png',caption="process of LC")
  
  st.write(""""
  
The process of getting an LC consists of four primary steps, which are enlisted here:

Step 1 - Issuance of LC
  After the parties to the trade agree on the contract and the use of LC, the importer applies to the issuing bank to issue an LC in favor of the exporter. The LC is sent by the issuing bank to the advising bank. The latter is generally based in the exporter’s country and may even be the exporter’s bank. The advising bank (confirming bank) verifies the authenticity of the LC and forwards it to the exporter.

Step 2 - Shipping of goods
  After receipt of the LC, the exporter is expected to verify the same to their satisfaction and initiate the goods shipping process.

Step 3 - Providing Documents to the confirming bank
  After the goods are shipped, the exporter (either on their own or through the freight forwarders) presents the documents to the advising/confirming bank.

Step 4 - Settlement of payment from importer and possession of goods
  The bank, in turn, sends them to the issuing bank and the amount is paid, accepted, or negotiated, as the case may be. The issuing bank verifies the documents and obtains payment from the importer. It sends the documents to the importer, who uses them to get possession of the shipped goods.
  
  
  Example of Issuing LC:
  
  Suppose Mr A (an Indian Exporter) has a contract with Mr B (an importer from the US) for sending a shipment of goods. Both parties being unknown to each other decide to go for an LC arrangement.

The letter of credit assures Mr A that he will receive the payment from the buyer and Mr B that he will have a systematic and documented process along with the evidence of goods having been shipped.

From this point on, this is how a letter of credit transaction would unveil between Mr A & Mr B:-

Mr B (buyer) goes to his bank that is the issuing bank (also called an opening bank) and issues a Letter of Credit.

The issuing bank further processes the LC to the advising bank (Mr A's bank).

The advising bank checks the authenticity of the LC and sends it to Mr A.

Now that Mr A has received the confirmation he will ship the goods and while doing so he will receive a Bill of Lading along with other necessary documents.

Further, he will send these documents to the negotiating bank.

The negotiating bank will make sure that all necessary requirements are fulfilled and accordingly make the payment to Mr A (the seller).

Additionally, the negotiating bank will send all the necessary documents to the issuing bank.

Which again the issuing bank will send to Mr B (Buyer) to confirm the authenticity.

Once Mr B has confirmed he will make the payment to the issuing bank.

And the issuing bank will pass on the funds to the negotiating bank.


  """)

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

  
  
  
  
  
  
  
  


  

