import streamlit as st


# Define a list of options
options = ["Negotiable Instrument Act"]
# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)

if option=="Negotiable Instrument Act":
    
    st.write("""
1.	Short title
2.	Interpretation clause
3.	Promissory note
4.	Bill of exchange
5.	Cheque"
6.	Holder"
7.	Holder in due course"
8.	Value"
9.	Instrument"
10.	Payable on demand"
11.	At a fixed time"
12.	Writing"
13.	Negotiable instruments
14.	Negotiation of negotiable instruments
15.	Endorsement
16.	Endorsement in blank and special endorsement
17.	Effect of endorsement
18.	Transferor by delivery and transferee
19.	Negotiation of instrument payable to bearer
20.	Rights of holder in due course
21.	Effect of material alteration
22.	Liability of maker, drawer and acceptor of negotiable instrument
23.	When the maker of a note is deemed to be an indorser
24.	Liability of indorser
25.	Liability of drawer of cheque
26.	Liability of drawee of cheque
27.	Payment in due course of negotiable instrument
28.	Payment to a banker
29.	Payment by whom?
30.	Discharge of indorser's liability
31.	Discharge from liability
32.	Exoneration of prior parties
33.	Holder's right to duplicate of lost bill
34.	Protection to bankers paying cheques bearing forged endorsements
35.	"Crossing" of cheques
36.	"Cheques" crossed specially
37.	General crossing defined and described
38.	Payment of crossed cheque
39.	Duties of banker on whom crossed cheque is drawn
40.	Protection of paying banker
41.	Collection of cheque by banker
42.	"Notice of dishonour"
43.	By and to whom notice should be given
44.	Mode in which notice may be given
45.	Time within which notice must be given
46.	Delay in giving notice
47.	Notice of dishonour necessary
48.	Excuse for delay in presentment for payment
49.	Presentment of cheque to charge drawer
50.	Presentment for payment
51.	When presentment unnecessary
52.	Liability of maker of note and acceptor of bill who fail to present on due date
53.	When note or bill matures on holiday
54.	When day of maturity is a holiday
55.	Applicability of the Indian Limitation Act, 1963
56.	Accommodation bills and notes
57.	Discharge of liability by payment in due course
58.	Payment to agent
59.	Payment to one of several joint payees
60.	Payment to banker under banker's lien
61.	Payment to rightful owner
62.	Savings of presentment for payment and notice of dishonour
63.	Repeal of Acts
64.	Savings of certain enactments
65.	Power to make rules

This list covers all the sections in the Negotiable Instruments Act.

""")
    
