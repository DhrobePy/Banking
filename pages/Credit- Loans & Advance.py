import streamlit as st
st.write("Welcome to the Loans and Advance section of our learning path")

options = ["Ratio of Financial Statement","EPS"]

# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)


if option=="Ratio of Financial Statement":
    
    st.write("""
    Here is a list of some of the most common financial ratios that can be calculated from a company's financial statement:

    1.  Liquidity ratios
            .   Current ratio
            .   Quick ratio
            .   Cash ratio
            .   Operating cash flow ratio
    2.  Profitability ratios
            .   Gross profit margin
            .   Operating profit margin
            .   Net profit margin
            .   Return on assets (ROA)
            .   Return on equity (ROE)
            .   Earnings per share (EPS)
    3.  Debt ratios
            .   Debt-to-equity ratio
            .   Debt-to-assets ratio
            .   Interest coverage ratio
            .   Long-term debt-to-equity ratio
    4.  Efficiency ratios
            .   Inventory turnover ratio
            .   Accounts receivable turnover ratio
            .   Accounts payable turnover ratio
            .   Total asset turnover ratio
            .   Fixed asset turnover ratio
            .   Working capital turnover ratio
    5.  Market value ratios
            .   Price-to-earnings (P/E) ratio
            .   Price-to-sales (P/S) ratio
            .   Price-to-book (P/B) ratio
            .   Dividend yield ratio
It's worth noting that not all of these ratios will be relevant for every company or industry. The choice of which ratios to use will depend on the specific context and purpose of the analysis.
    
    """)

if option == "EPS":
    
    st.markdown("<h1 style='text-align: center;'>Earnings Per Share</h1>", unsafe_allow_html=True)
    st.write("""    
    
        EPS stands for earnings per share and is a financial ratio that measures a company's profit per outstanding share of its common stock. It is calculated by dividing the company's net income by the number of outstanding shares of common stock.
        
        Here is an example of how to calculate EPS:
        
        Assume ABC Company has a net income of $1 million for the year and has 500,000 outstanding shares of common stock.
        
                    EPS = Net income / Number of outstanding shares
                    
                    EPS = $1,000,000 / 500,000
                    
                    EPS = $2.00
                    
        This means that ABC Company earned $2.00 in profit for every outstanding share of common stock. EPS is a commonly used financial ratio that is used to evaluate a company's profitability and is often used by investors to compare different companies within an industry. A higher EPS indicates that a company is more profitable on a per-share basis, which can be an indicator of a company's financial health and future growth potential. 
        
""")
else:
    st.write("End of Options")

