import streamlit as st
st.write("Welcome to the Loans and Advance section of our learning path")



elif option == "Calculation of EPS":
    
    st.markdown("<h1 style='text-align: center;'>Earnings Per Share</h1>", unsafe_allow_html=True)
    st.write("""    EPS stands for earnings per share and is a financial ratio that measures a company's profit per outstanding share of its common stock. It is calculated by dividing the company's net income by the number of outstanding shares of common stock.
Here is an example of how to calculate EPS:
Assume ABC Company has a net income of $1 million for the year and has 500,000 outstanding shares of common stock.
EPS = Net income / Number of outstanding shares
EPS = $1,000,000 / 500,000
EPS = $2.00
This means that ABC Company earned $2.00 in profit for every outstanding share of common stock. EPS is a commonly used financial ratio that is used to evaluate a company's profitability and is often used by investors to compare different companies within an industry. A higher EPS indicates that a company is more profitable on a per-share basis, which can be an indicator of a company's financial health and future growth potential.      
""")
else:
    st.write("This is BASEL-III")

