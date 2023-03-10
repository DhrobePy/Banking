import streamlit as st

# Define a list of options
options = ["BASEL-I", "BASEL-II", "BASEL-III", "Tier-1 Capital", "Tier-2 Capital","Nano Lending", "Shadow Banking","For Niladri Only"
          ,"Capital","Calculation of EPS", "Stress Testing"]

# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)

# Display the selected option
if option == "Stress Testing":
    
    st.markdown("<h1 style='text-align: center;'>Stress Testing</h1>", unsafe_allow_html=True)
    st.write("""
    
    Stress testing is a risk management technique used by financial institutions to evaluate how well their portfolios or balance sheets would perform under adverse scenarios or stress events. These scenarios are designed to be severe and unlikely but still plausible, such as a significant market downturn, a credit crisis, or a major operational failure.

Here's an example of stress testing:

Suppose a bank holds a portfolio of mortgages worth $1 billion, and the bank wants to evaluate how this portfolio would perform under adverse conditions. The bank may design a stress test scenario where there is a significant economic downturn, leading to high unemployment and a sharp decline in housing prices.

Under this scenario, the bank may estimate that a certain percentage of borrowers would default on their mortgages, and that the value of the mortgage portfolio would decline significantly. The bank would then simulate these conditions using financial models and assess the impact on its capital adequacy and profitability.

The bank may find that under this scenario, its capital would be depleted, and it may need to raise additional funds or take other measures to mitigate the losses. Alternatively, the bank may find that its portfolio is resilient and that it would be able to weather the adverse conditions without significant losses.

By conducting stress tests, financial institutions can identify potential vulnerabilities in their portfolios and take appropriate measures to manage risk and improve their resilience to adverse events. Stress testing is an important tool for risk management and is used by regulators and supervisors to ensure the safety and stability of the financial system.

""")


    st.markdown("<h1 style='text-align: center;'>BASEL-I</h1>", unsafe_allow_html=True)
    st.write(""""

There are different methods of stress testing, each of which uses a different approach to simulate the impact of adverse scenarios on financial institutions' portfolios or balance sheets. Here are some examples of stress testing methods:

Scenario analysis: 
          This method involves designing scenarios that reflect plausible but severe events that could impact the financial institution's portfolios or balance sheets. For example, a bank might design a scenario where interest rates increase suddenly and sharply, leading to a significant increase in loan defaults and a decline in the value of the bank's assets.
Sensitivity analysis: This method involves testing the impact of changes in individual risk factors on the financial institution's portfolios or balance sheets. For example, a bank might test how changes in interest rates, exchange rates, or commodity prices would impact its profitability and capital adequacy.

Reverse stress testing: 
          This method involves identifying an extreme adverse scenario and working backward to identify the conditions that would lead to such a scenario. For example, a bank might identify a scenario where it would become insolvent, and then work backward to identify the combination of events that would lead to this outcome.
          
Macro stress testing: 
          This method involves assessing the impact of adverse scenarios on the broader economy and financial system, as well as on individual financial institutions. For example, a regulator might conduct a macro stress test to assess the impact of a severe recession on the banking system, including the potential for systemic risk and contagion.
          
Overall, stress testing is an important tool for risk management in the financial sector. By simulating the impact of adverse scenarios, financial institutions can identify potential vulnerabilities and take appropriate measures to mitigate risk and improve their resilience to adverse events.

""")


if option == "BASEL-I":
    
    st.markdown("<h1 style='text-align: center;'>BASEL-I</h1>", unsafe_allow_html=True)
    st.write("""
    
    Basel I, also known as the Basel Accord, was developed in 1988 by the Basel Committee on Banking Supervision. The accord aimed to establish a set of international banking standards to ensure banks had enough capital to withstand financial shocks and reduce the risk of bank failures.  
    
    The key features of Basel I include:
    
        1. Minimum Capital Requirement: Basel I introduced a minimum capital requirement of 8% of a bank's risk-weighted assets. Banks were required to hold this capital in the form of Tier 1 and Tier 2 capital.
        The calculation of CAR under Basel I can be simplified as follows:
        
            CAR = (Tier 1 Capital + Tier 2 Capital) / Risk-Weighted Assets
            
        2. Risk Weighted Assets: Basel I classified assets into five risk categories and assigned them risk weights ranging from 0% to 100%. The risk weights were used to calculate the amount of capital a bank was required to hold against its assets.
        
        3. Uniform Standards: Basel I established uniform standards for banks across different countries, which helped to level the playing field and promote fair competition.
        
        
""")
    st.markdown("<h2 style='text-align: center;'>Drawback of BASEL-I</h2>", unsafe_allow_html=True)
    st.write("""
    
The main drawback of Basel I was that it did not take into account the varying degrees of risk within each asset class. This meant that some assets with the same risk weight had very different levels of risk, which led to the underestimation of the actual risk held by banks. In response to this, Basel II was introduced in 2004, which incorporated more sophisticated risk measurement techniques and revised capital requirements.


            """)
      
elif option == "BASEL-II":
    st.write("This is option 2.")
    
elif option == "Tier-1 Capital":
    
    st.markdown("<h1 style='text-align: center;'>Tier-1 Capital</h1>", unsafe_allow_html=True)
    st.write("""
    The components of Tier 1 capital in Bangladesh are similar to those of other countries and include the following:

Common Equity: Common equity represents the funds invested in the bank by its shareholders and is the most important component of Tier 1 capital. Common equity includes the value of the bank's common stock, additional paid-in capital, and retained earnings.
For example, Eastern Bank Limited, one of the largest commercial banks in Bangladesh, reported a total common equity of BDT 20.37 billion as of December 31, 2020.

Retained Earnings: Retained earnings represent the portion of the bank's profits that have been retained and not paid out as dividends to shareholders. This component is critical as it provides a source of internal financing for the bank's operations and helps to support growth and expansion.
For example, BRAC Bank Limited, a leading commercial bank in Bangladesh, reported retained earnings of BDT 21.26 billion as of December 31, 2020.

Disclosed Reserves: Disclosed reserves are reserves that have been set aside by the bank for specific purposes, such as to cover potential losses or to meet regulatory requirements. These reserves are typically disclosed in the bank's financial statements and can be used to absorb unexpected losses or to strengthen the bank's capital position.
For example, Dutch-Bangla Bank Limited, one of the largest private commercial banks in Bangladesh, reported disclosed reserves of BDT 10.12 billion as of December 31, 2020.

Non-cumulative Perpetual Preferred Stock: This represents a type of preferred stock that does not require the bank to pay dividends that have been deferred in the past. This component provides the bank with additional flexibility in managing its capital position.
For example, Prime Bank Limited, a leading commercial bank in Bangladesh, issued non-cumulative perpetual preferred stock worth BDT 2 billion in 2019 to strengthen its Tier 1 capital position.

In summary, the components of Tier 1 capital in Bangladesh include common equity, retained earnings, disclosed reserves, and non-cumulative perpetual preferred stock. These components provide the bank with a strong cushion against potential losses and help ensure its safety and soundness.

    
    """)
    st.markdown("<h2 style='text-align: center;'>Components of Tier-1 Capital</h2>", unsafe_allow_html=True)
    st.write("""
    
    Common Equity Tier 1 (CET1) capital is a core component of a bank's capital structure and is considered the highest quality form of capital. The components of CET1 capital include:

    1. Common stock: Common stock represents ownership in the bank and is the most basic form of CET1 capital. It includes the par value of the bank's common shares, as well as any additional paid-in capital in excess of the par value.

    2. Retained earnings: Retained earnings are profits that the bank has earned but has not distributed as dividends. Retained earnings are a key source of CET1 capital because they represent the bank's accumulated earnings that can be used to absorb losses.
    
    3. Other comprehensive income (OCI): OCI includes gains and losses that are not included in the bank's net income, such as unrealized gains or losses on investments or changes in the value of pension plans. OCI can be included in CET1 capital if it meets certain criteria.
    
    4. Minority interests: Minority interests refer to the portion of a subsidiary's equity that is not owned by the bank. If the bank owns less than 100% of a subsidiary, the minority interest can be included in CET1 capital if it meets certain criteria.


    Overall, CET1 capital is a key measure of a bank's financial strength and is used by regulators to assess a bank's ability to absorb losses. The components of CET1 capital represent the highest quality form of capital because they are fully loss-absorbing and can be used to absorb losses without causing the bank to become insolvent.
    
    """)
    st.markdown("<h2 style='text-align: center;'>Equity Capital</h2>", unsafe_allow_html=True)
    st.write("""
    Equity capital is the portion of a company's capital that represents the ownership interest of its shareholders. Equity capital is raised by issuing common stock or preferred stock to investors in exchange for their investment in the company. The funds raised through equity capital are used by the company to finance its operations, invest in new projects, or to pay off debt.

The key features of equity capital are as follows:

          1.No fixed payments: 
                    Equity capital does not require any fixed payments to be made to shareholders, unlike debt financing. Instead, shareholders receive returns in the form of dividends or capital appreciation.
          2.No maturity date: 
                    Equity capital does not have a maturity date, which means that there is no obligation to repay the capital to investors. As long as the company is in operation, the equity capital remains invested in the company.
          3.Ownership stake: 
                    Shareholders who invest in equity capital become part-owners of the company and have voting rights in important company decisions.
          4.Risk and return: 
          Equity capital is considered a higher risk investment than debt financing, but it also has the potential for higher returns if the company performs well.
          Equity capital is an important component of a company's capital structure and plays a crucial role in its growth and expansion. By issuing equity capital, companies can raise funds without incurring debt, which can improve their financial flexibility and reduce their financial risk. However, issuing equity capital also dilutes the ownership stake of existing shareholders, which can be a concern for some investors.

""")
    st.markdown("<h1 style='text-align: center;'>Disclosed Reserve</h1>", unsafe_allow_html=True)
    
    st.write("""
    Disclosed reserves are reserves that have been set aside by a company for a specific purpose and are disclosed in the company's financial statements. These reserves are created by appropriating a portion of the company's profits or retained earnings to be used for a specific purpose, such as to cover potential losses, meet regulatory requirements, or fund future projects.

Disclosed reserves can serve several purposes, such as:

1. Buffer against potential losses: Disclosed reserves can be used to cover potential losses that may arise due to unforeseen events or market conditions. By setting aside a portion of their profits, companies can build a reserve that can be used to offset losses and protect their financial position.
2. Regulatory compliance: Disclosed reserves may be required by regulators to ensure that companies have sufficient financial resources to meet their obligations. For example, banks are required to maintain certain levels of reserves to cover potential loan losses.
3. Future projects: Disclosed reserves can be used to fund future projects or investments that are expected to generate long-term benefits for the company. By setting aside funds for these purposes, companies can reduce their reliance on external financing and improve their financial flexibility.
Disclosed reserves are typically disclosed in the notes to a company's financial statements, which provide additional information about the company's financial position and performance. Companies may also be required to disclose the specific purpose for which the reserves have been created, as well as any restrictions on their use.
    """)

elif option== "Nano Lending":
    st.markdown("<h1 style='text-align: center;'>Nano Lending</h1>", unsafe_allow_html=True)
    
    st.write("""
    
    Nano lending, also known as microfinance or microcredit, is a type of lending that provides small loans to individuals or businesses that do not have access to traditional banking services. The concept of microcredit was first developed by economist Muhammad Yunus in the 1970s in Bangladesh, and it has since become a popular form of lending in developing countries around the world.

The idea behind nano lending is to provide small loans to individuals who lack collateral or a credit history, making it difficult for them to access traditional bank loans. These loans are typically used to start or expand small businesses or to finance basic needs such as housing, education, or healthcare.

In Bangladesh, microcredit has played a significant role in reducing poverty and empowering women. The Grameen Bank, founded by Muhammad Yunus in 1983, has provided microcredit to millions of poor people, especially women, in Bangladesh. The bank operates on the principle of "group lending," where small groups of borrowers are responsible for each other's loans, creating a system of mutual support and accountability.

Another example of nano lending in Bangladesh is BRAC, a development organization that provides microfinance services to poor people in rural areas. BRAC's microfinance program includes not only loans but also savings, insurance, and financial literacy training, creating a comprehensive approach to financial inclusion.

Overall, nano lending has emerged as a powerful tool for poverty reduction and economic empowerment, especially in developing countries. It has helped millions of people to access credit and build their own businesses, improving their standard of living and contributing to economic growth.

Nano lending typically involves a platform or marketplace that connects borrowers with lenders. The platform handles the loan application process, credit checks, and repayment schedules, and facilitates the transfer of funds between the borrower and lender.

The main advantage of nano lending is that it provides access to credit to individuals or businesses who might not otherwise be able to obtain loans from traditional banks or financial institutions. It can also provide a way for lenders to earn a higher return on their investments than they might get from other types of investments.

However, nano lending can also be risky for both borrowers and lenders, as the loans are typically unsecured and may have higher interest rates than traditional loans. Additionally, the lack of regulation in the industry means that borrowers and lenders may not be fully protected in the event of default or fraud. It's important for anyone considering nano lending, whether as a borrower or lender, to thoroughly research and understand the risks involved before participating in any lending platform.

""")

elif option == "For Niladri Only":
    st.markdown("<h1 style='text-align: center;'>Tomar Laigga Banaisi Dada</h1>", unsafe_allow_html=True)
    st.write("Box a kono topic mone porle add koro, ami add kore nicchi materials")

    
    
elif option == "Shadow Banking":
  st.markdown("<h4 style='text-align: center;'>Shadow Banking </h4>", unsafe_allow_html=True)

  st.write("""


    Shadow banking refers to a system of financial intermediaries that operate outside of traditional banking regulations and practices. These intermediaries provide credit, liquidity, and other financial services to clients, but are not subject to the same regulatory oversight as traditional banks.

    Examples of shadow banking activities include hedge funds, money market funds, and certain types of insurance companies, which may engage in activities such as securities lending, repurchase agreements, and structured finance transactions.

    In Bangladesh, examples of shadow banking activities include microfinance institutions, leasing companies, and non-bank financial institutions. These entities provide credit and other financial services to individuals and businesses, but are not subject to the same regulatory requirements as traditional banks.

    
Here are some more examples of shadow banking activities and how they work:

Money market funds: 
                 These are mutual funds that invest in short-term, low-risk securities such as government bonds and commercial paper. They are not considered banks, but they operate like banks by taking deposits from investors and using the funds to make investments. Money market funds are typically used by investors as a safe place to park their cash, but they are not insured by the FDIC like bank deposits. In 2008, the Reserve Primary Fund, a money market fund, "broke the buck" due to its exposure to Lehman Brothers' commercial paper, which caused widespread panic in the money market fund industry.

Hedge funds: 
                Hedge funds are private investment vehicles that use a variety of investment strategies to generate high returns for their investors. They are not subject to the same regulations as mutual funds, and typically require a large minimum investment. Hedge funds often use leverage (borrowed money) to increase their returns, which can make them more risky. In 1998, Long-Term Capital Management, a hedge fund that used complex derivatives trades, collapsed and had to be bailed out by the Federal Reserve.

Peer-to-peer (P2P) lending: 
                P2P lending platforms connect borrowers with individual lenders who are willing to lend money. These platforms use technology to match borrowers with lenders and facilitate the lending process. P2P lending can provide borrowers with access to credit at lower interest rates than traditional banks, but the loans are not insured and the creditworthiness of the borrowers may be harder to assess. In Bangladesh, there are several P2P lending platforms such as iPay and Samadhan.
  
Microfinance institutions: 
                 Microfinance institutions provide financial services to low-income individuals and small businesses who may not have access to traditional banking services. These services can include loans, savings accounts, and insurance. Microfinance institutions typically charge higher interest rates than traditional banks, but they are often more flexible in their lending practices. In Bangladesh, Grameen Bank is a well-known microfinance institution that has been providing financial services to rural communities for decades.


While these shadow banking activities can provide benefits such as increased access to credit and financial services, they can also pose risks to the stability of the financial system. Because they are not subject to the same regulatory oversight as traditional banks, they may engage in riskier activities and have less transparency. Therefore, it is important for regulators to monitor and regulate shadow banking activities to ensure the stability of the financial system.

""")    
elif option == "Capital":
    st.markdown("<h4 style='text-align: center;'>Different Types of Capital in Bank </h4>", unsafe_allow_html=True)

    st.write("""
    Banks typically have various types of capital to meet their regulatory requirements and support their operations. The different types of capital are as follows:

    Tier 1 capital: This is the highest quality capital and consists of common equity and disclosed reserves. Examples of Tier 1 capital in Bangladeshi banks include retained earnings and common shares.
    
    Tier 2 capital: This is a supplementary capital that includes items such as subordinated debt and undisclosed reserves. Examples of Tier 2 capital in Bangladeshi banks include subordinated bonds and term deposits.
    
    Tier 3 capital: This is a short-term capital that can be used to support market risk. Examples of Tier 3 capital in Bangladeshi banks include short-term debt and preference shares.
""")
          
elif option == "Tier-2 Capital":
    
    st.markdown("<h1 style='text-align: center;'>Tier-2 Capital</h1>", unsafe_allow_html=True)
    st.write("""
    Tier 2 capital is a component of a bank's capital that is considered less reliable than Tier 1 capital but still contributes to its overall capital adequacy. Tier 2 capital includes a range of instruments that can be used to absorb losses in the event of financial distress. Tier 2 capital instruments have longer-term maturities than Tier 1 capital instruments and can be written off or converted to equity in the event of the bank's insolvency.
""")

    st.write("""
    The following are some examples of Tier 2 capital instruments:

          1. Subordinated debt: 
          Subordinated debt is a type of debt that ranks below senior debt in the event of a liquidation or bankruptcy. It is issued with longer-term           maturities and higher interest rates than senior debt to compensate for the additional risk. Subordinated debt holders are typically paid only after  senior debt holders have been paid in full.

          Here is an example of subordinated debt:

          Let's say XYZ Bank issues subordinated debt with a face value of $10 million and a maturity of 10 years. The subordinated debt has a coupon rate of 7%, which means that XYZ Bank will pay $700,000 in interest to the subordinated debt holders every year.

          If XYZ Bank faces financial difficulties and is unable to meet its financial obligations, senior debt holders will be paid in full before the subordinated debt holders receive any payments. This means that if XYZ Bank is liquidated and there is only $8 million available to pay creditors, senior debt holders will receive their full $8 million share, while the subordinated debt holders will only receive the remaining $2 million.

          Subordinated debt is an important component of a bank's capital structure and is used to meet regulatory requirements for Tier 2 capital. It allows banks to raise funds at a lower cost than equity capital while still providing some protection to senior debt holders.

          2. Preference shares: 
          Preference shares, also known as preferred stock or preference stock, are a type of equity security that has priority over common stock in terms of dividend payments and liquidation proceeds.

          Here is an example of preference shares:

          Let's say ABC Company issues 10,000 preference shares at a face value of $100 per share. The preference shares have a fixed dividend rate of 5%, which means that the holders of preference shares will receive a dividend of $5 per share per year. This dividend is paid before any dividend is paid to the common stockholders.

          In the event of liquidation, the holders of preference shares have priority over common stockholders in receiving the proceeds. For example, if ABC Company is liquidated and there are $1 million in assets to be distributed among shareholders, preference shareholders will receive their $1 million share before any amount is paid to common stockholders.

          Preference shares may also have features such as callable or convertible options. Callable preference shares can be redeemed by the issuer before their maturity date. Convertible preference shares can be converted into common shares at a predetermined conversion rate.

          Overall, preference shares are a way for companies to raise capital without issuing debt or diluting the ownership of existing shareholders. They offer a fixed dividend rate and priority in receiving the proceeds in the event of liquidation. However, they also have limitations and risks, such as the potential for fluctuation in dividend payments and the possibility of losing value if interest rates rise.

          3. Undisclosed reserves: 
          Undisclosed reserves are reserves that are not disclosed on a bank's balance sheet and can be used to absorb losses in the event of financial distress. However, undisclosed reserves are not widely used as a Tier 2 capital instrument due to their lack of transparency.

          Here is an example of undisclosed reserves:

          Let's say XYZ Bank has been profitable for several years and has accumulated a significant amount of profits. However, instead of declaring these profits as dividends or using them to strengthen its disclosed reserves, XYZ Bank decides to keep some of the profits as undisclosed reserves.

          In the event of financial distress, XYZ Bank can use these undisclosed reserves to absorb losses without having to disclose the use of these reserves to the public. This can provide some flexibility to the bank and help it to avoid a situation where investors lose confidence in the bank and cause a further deterioration of its financial condition.

          However, undisclosed reserves are not widely used as a Tier 2 capital instrument due to their lack of transparency. Investors and regulators may view undisclosed reserves with suspicion as they cannot be easily audited or monitored. As a result, banks are generally encouraged to maintain transparent and easily verifiable reserves as a way to maintain trust and confidence in the financial system.

          4. Revaluation reserves: 
          Revaluation reserves are created when the value of a company's assets is revalued upwards. This is a way for a company to increase its equity without having to issue new shares or retain earnings. Revaluation reserves can be used to absorb losses in the future or to finance future growth opportunities.

          Here is an example of revaluation reserves:

          Let's say ABC Company owns a piece of property that it originally purchased for $1 million. However, the value of the property has increased over time and is now worth $2 million. If ABC Company decides to revalue the property upwards, it can create a revaluation reserve of $1 million.

          This means that ABC Company will now report the value of the property on its balance sheet as $2 million and will also report a revaluation reserve of $1 million. This increases the equity of the company by $1 million without requiring the company to issue new shares or retain earnings.

          In the future, if ABC Company experiences losses, it can use the revaluation reserve to absorb some of these losses. Alternatively, if ABC Company wants to invest in new opportunities, it can use the revaluation reserve to finance these investments.

          Overall, revaluation reserves are a way for companies to increase their equity without diluting the ownership of existing shareholders or relying on retained earnings. However, they are subject to regulatory restrictions and must be created in accordance with accounting standards.

          5. Hybrid securities: 
          Hybrid securities are a type of financial instrument that have both debt and equity characteristics. They can be a useful way for companies to raise capital while still maintaining some flexibility in their financial structure.

          Here is an example of hybrid securities and their features:

          i.Convertible bonds: Convertible bonds are a type of hybrid security that can be converted into equity shares at a predetermined conversion rate. They offer the potential for investors to receive a fixed income stream from the bond and also benefit from any potential upside in the company's stock price if they choose to convert the bond into equity shares.

                    Features of convertible bonds:

                    i.Convertibility: The bond can be converted into equity shares at a predetermined conversion rate.
                    ii.Fixed income: The bond offers a fixed income stream to investors until it is converted or reaches maturity.
                    iii.Callability: The issuer may have the option to call back the bond before it reaches maturity.
                    iv.Credit risk: The investor is still exposed to credit risk as they would be with any other bond.
                    v.Equity participation: The investor has the potential to participate in any potential upside in the company's stock price if they choose to convert the bond into equity shares.
          ii.Preference shares: Preference shares are a type of hybrid security that have priority over common shares in terms of dividend payments and liquidation proceeds. They offer a fixed income stream to investors while still maintaining some equity-like characteristics.

                    Features of preference shares:

                    i.Priority dividend payments: Preference shares have priority over common shares in terms of dividend payments.
                    ii.Fixed dividend: The dividend rate on preference shares is usually fixed, which means that investors can expect a steady income stream.
                    iii.No voting rights: Unlike common shares, preference shares usually do not have voting rights.
                    iv.Callability: The issuer may have the option to call back the preference shares before they reach maturity.
                    v.Equity-like characteristics: Preference shares have some equity-like characteristics, but they are still considered to be a form of debt.
          Overall, hybrid securities offer a way for companies to raise capital while still maintaining some flexibility in their financial structure. They have both debt and equity characteristics, which can make them attractive to investors who are looking for a mix of fixed income and equity-like participation. However, they are subject to regulatory restrictions and can be more complex than traditional debt or equity instruments.
Overall, Tier 2 capital provides additional cushioning to a bank's capital structure and helps to absorb losses in the event of financial distress. However, Tier 2 capital is considered less reliable than Tier 1 capital and is subject to more regulatory restrictions.
    """)

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




