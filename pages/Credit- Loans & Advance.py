import streamlit as st
options = ["Ratio of Financial Statement","EPS", "Cash Cycle"]
# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)


if option=="Cash Cycle":
    st.markdown("<h1 style='text-align: center;'>Calculation of Cash Cycle</h1>", unsafe_allow_html=True)
    st.write("""
    
    The cash cycle of a trading business is the length of time it takes to convert its inventory and other current assets into cash. It measures the time it takes for a business to pay for inventory, sell it, and collect payment from customers. To calculate the cash cycle, you need to follow these steps:

        .   Determine the days inventory outstanding (DIO): This measures the average number of days it takes for the business to sell its inventory.
                DIO = (Average Inventory / Cost of Goods Sold) x 365

        .   Determine the days payable outstanding (DPO): This measures the average number of days it takes for the business to pay its suppliers.
                DPO = (Accounts Payable / Cost of Goods Sold) x 365

        .   Determine the days sales outstanding (DSO): This measures the average number of days it takes for the business to collect payment from its customers.
                DSO = (Accounts Receivable / Sales) x 365

        .   Calculate the cash cycle: This is the number of days it takes for the business to convert its inventory and other current assets into cash.
                Cash Cycle = DIO + DSO - DPO


For example, let's say a trading business has the following financial information:

            .   Average Inventory: $50,000
            .   Cost of Goods Sold: $200,000
            .   Accounts Payable: $25,000
            .   Sales: $300,000
            .   Accounts Receivable: $40,000
Using the above formula, we can calculate the cash cycle as follows:

            .   DIO = ($50,000 / $200,000) x 365 = 91.25 days
            .   DPO = ($25,000 / $200,000) x 365 = 45.63 days
            .   DSO = ($40,000 / $300,000) x 365 = 48.33 days

            .   Cash Cycle = 91.25 + 48.33 - 45.63 = 93.95 days

    Therefore, it takes the trading business approximately 94 days to convert its inventory and other current assets into cash. This information can be useful in managing the business's working capital and cash flow.



    """)
    
    
    
    
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
    st.markdown("<h2 style='text-align: center;'>Profitablity Ratio</h2>", unsafe_allow_html=True)
    st.write("""
    
    Profitability ratios are a group of financial ratios that measure a company's ability to generate profits relative to its revenue, assets, or equity. Here are a few examples of profitability ratios and how they can be calculated:

    1.  Gross Profit Margin:
    
        The gross profit margin measures the percentage of revenue that is left after deducting the cost of goods sold. It shows how much profit a company is generating from each dollar of sales.
        Formula: 
                Gross Profit Margin = (Revenue - Cost of Goods Sold) / Revenue

        Example: 
                Let's say a company has revenue of $1,000,000 and a cost of goods sold of $600,000. The gross profit margin would be:

                Gross Profit Margin = ($1,000,000 - $600,000) / $1,000,000 = 0.4 or 40%

                This means that the company is generating 40 cents of gross profit for every dollar of sales.

    2.  Net Profit Margin:
    
        The net profit margin measures the percentage of revenue that is left after deducting all expenses, including taxes and interest. It shows how much profit a company is generating from each dollar of sales after all expenses are taken into account.
        
        Formula: 
                Net Profit Margin = Net Income / Revenue

        Example: 
                Let's say a company has a net income of $150,000 and revenue of $1,000,000. The net profit margin would be:

                    Net Profit Margin = $150,000 / $1,000,000 = 0.15 or 15%

                This means that the company is generating 15 cents of net profit for every dollar of sales.

    3.  Return on Equity (ROE):
    
        The return on equity measures the amount of net income a company generates for each dollar of equity. It shows how effectively a company is using its equity to generate profits.
        Formula: 
                Return on Equity = Net Income / Shareholders' Equity

        Example: 
                Let's say a company has a net income of $150,000 and shareholders' equity of $1,000,000. The return on equity would be:

                    Return on Equity = $150,000 / $1,000,000 = 0.15 or 15%

                This means that the company is generating 15 cents of net income for each dollar of shareholders' equity.

        It's worth noting that profitability ratios are important indicators of a company's financial health and are often used by investors and analysts to evaluate a company's performance. However, they should be analyzed in conjunction with other financial ratios and metrics to get a more complete picture of a company's financial situation.
        
    """)
    
    
    st.markdown("<h2 style='text-align: center;'>Debt Ratio</h2>", unsafe_allow_html=True)
    st.write("""
    Debt ratios are financial ratios that measure a company's leverage, or the amount of debt it has relative to its assets or equity. Here are a few examples of debt ratios and how they can be calculated:

        1.  Debt-to-Equity Ratio:
            The debt-to-equity ratio measures the amount of debt a company has relative to its equity. It shows how much debt a company is using to finance its operations.
            
                Formula: 
                        Debt-to-Equity Ratio = Total Debt / Shareholders' Equity
                Example: 
                        Let's say a company has total debt of $1,500,000 and shareholders' equity of $2,000,000. The debt-to-equity ratio would be:
                            Debt-to-Equity Ratio = $1,500,000 / $2,000,000 = 0.75 or 75%
                            
                This means that the company has $0.75 of debt for every $1 of equity.
                
                
        2.  Debt-to-Assets Ratio:
            The debt-to-assets ratio measures the amount of debt a company has relative to its total assets. It shows the percentage of a company's assets that are financed by debt.
                Formula: 
                    Debt-to-Assets Ratio = Total Debt / Total Assets
                Example: 
                    Let's say a company has total debt of $1,500,000 and total assets of $4,000,000. The debt-to-assets ratio would be:
                        Debt-to-Assets Ratio = $1,500,000 / $4,000,000 = 0.375 or 37.5%
                        
                 This means that 37.5% of the company's assets are financed by debt.


        3.  Interest Coverage Ratio:
            The interest coverage ratio measures a company's ability to meet its interest obligations on its debt. It shows how many times a company's operating income covers its interest expenses.
                Formula: 
                    Interest Coverage Ratio = Operating Income / Interest Expense
                Example: 
                    Let's say a company has operating income of $500,000 and interest expense of $50,000. The interest coverage ratio would be:
                    
                        Interest Coverage Ratio = $500,000 / $50,000 = 10
            This means that the company's operating income is 10 times greater than its interest expense, indicating that the company has a strong ability to meet its interest obligations.

            It's worth noting that debt ratios are important indicators of a company's financial health, as high levels of debt can increase a company's financial risk. However, debt ratios should be analyzed in conjunction with other financial ratios and metrics to get a more complete picture of a company's financial situation.
    
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

