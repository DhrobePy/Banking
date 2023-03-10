import streamlit as st

st.write("Welcome to General Banking Page. Please select desired options in sidebar to explore GB related queries")


# Define a list of options
options = ["Negotiable Instrument Act"]
# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)

if option=="Negotiable Instrument Act":
    
    st.write("""
    
    Short title
Interpretation clause
"Promissory note"
"Bill of exchange"
"Cheque"
"Holder"
"Holder in due course"
"Value"
"Instrument"
"Payable on demand"
"At a fixed time"
"Writing"
Negotiable instruments
Negotiation of negotiable instruments
Endorsement
Endorsement in blank and special endorsement
Effect of endorsement
Transferor by delivery and transferee
Negotiation of instrument payable to bearer
Rights of holder in due course
Effect of material alteration
Liability of maker, drawer and acceptor of negotiable instrument
When the maker of a note is deemed to be an indorser
Liability of indorser
Liability of drawer of cheque
Liability of drawee of cheque
Payment in due course of negotiable instrument
Payment to a banker
Payment by whom?
Discharge of indorser's liability
Discharge from liability
Exoneration of prior parties
Holder's right to duplicate of lost bill
Protection to bankers paying cheques bearing forged endorsements
"Crossing" of cheques
"Cheques" crossed specially
General crossing defined and described
Payment of crossed cheque
Duties of banker on whom crossed cheque is drawn
Protection of paying banker
Collection of cheque by banker
"Notice of dishonour"
By and to whom notice should be given
Mode in which notice may be given
Time within which notice must be given
Delay in giving notice
Notice of dishonour necessary
Excuse for delay in presentment for payment
Presentment of cheque to charge drawer
Presentment for payment
When presentment unnecessary
Liability of maker of note and acceptor of bill who fail to present on due date
When note or bill matures on holiday
When day of maturity is a holiday
Applicability of the Indian Limitation Act, 1963
Accommodation bills and notes
Discharge of liability by payment in due course
Payment to agent
Payment to one of several joint payees
Payment to banker under banker's lien
Payment to rightful owner
Savings of presentment for payment and notice of dishonour
Repeal of Acts
Savings of certain enactments
Power to make rules
This list covers all the sections in the Negotiable Instruments Act.

""")
    
