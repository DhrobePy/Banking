import streamlit as st
options = ["Ratio of Financial Statement","EPS"]
# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)

if option=="Ratio of Financial Statement":
    st.markdown("<h1 style='text-align: center;'>Ratio's of a Financial Statement</h1>", unsafe_allow_html=True)
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
    st.markdown("<h2 style='text-align: center;'>Liquidity Ratio</h2>", unsafe_allow_html=True)
    st.write("""
    
    Liquidity ratios are a group of financial ratios that measure a company's ability to pay off its short-term obligations with its current assets. Here are a few examples of liquidity ratios and how they can be calculated:

    1.  Current Ratio:
            The current ratio compares a company's current assets to its current liabilities. It measures a company's ability to pay off its short-term debts with its current assets.
            
            Formula: Current Ratio = Current Assets / Current Liabilities

            Example: Let's say a company has current assets of $100,000 and current liabilities of $50,000. The current ratio would be:

                        Current Ratio = $100,000 / $50,000 = 2

            This means the company has $2 of current assets for every $1 of current liabilities, which indicates good short-term liquidity.

    2.  Quick Ratio:
    
            The quick ratio, also known as the acid-test ratio, is a more conservative measure of liquidity that excludes inventory from current assets. It measures a company's ability to pay off its short-term debts with its most liquid assets.
            
            Formula: Quick Ratio = (Current Assets - Inventory) / Current Liabilities

            Example: Let's say a company has current assets of $100,000, inventory of $20,000, and current liabilities of $50,000. The quick ratio would be:

                        Quick Ratio = ($100,000 - $20,000) / $50,000 = 1.6

            This means the company has $1.6 of highly liquid assets for every $1 of current liabilities, which indicates decent short-term liquidity.

    3.  Cash Ratio:
    
            The cash ratio is the most conservative liquidity ratio, as it only takes into account a company's cash and cash equivalents. It measures a company's ability to pay off its short-term debts with its cash reserves.
            
            Formula: Cash Ratio = Cash and Cash Equivalents / Current Liabilities

            Example: Let's say a company has cash and cash equivalents of $30,000 and current liabilities of $50,000. The cash ratio would be:

                        Cash Ratio = $30,000 / $50,000 = 0.6

            This means the company has $0.6 of cash and cash equivalents for every $1 of current liabilities, which may indicate a lower level of short-term liquidity.
    4. Operating Cash Flow :
    
            Operating cash flow is a measure of the cash that a company generates from its core business operations, and it is a key component of a company's cash flow statement. It reflects the amount of cash a company has available for investments, debt payments, and dividends after accounting for its operating expenses.

            Here is an example of how to calculate operating cash flow:

            Assume that a company has the following information for the year:

                    .   Net income: $100,000
                    .   Depreciation expense: $20,000
                    .   Increase in accounts receivable: $10,000
                    .   Decrease in inventory: $5,000
                    .   Increase in accounts payable: $8,000
                    .   Income tax expense: $15,000
            To calculate the company's operating cash flow, we start with the net income figure and add back any non-cash expenses and any changes in working capital that did not involve cash:

                Operating cash flow = Net income + Depreciation expense - Increase in accounts receivable + Decrease in inventory + Increase in accounts payable - Income tax expense

                = $100,000 + $20,000 - $10,000 + $5,000 + $8,000 - $15,000

                = $108,000

            This means that the company generated $108,000 of cash from its operating activities during the year.

            It's worth noting that operating cash flow can provide valuable insight into a company's ability to generate cash from its core operations. However, it's important to compare a company's operating cash flow to its net income and other financial metrics to get a more complete picture of its financial health.

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

