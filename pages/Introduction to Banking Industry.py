import streamlit as st

# Define a list of options
options = ["BASEL-I", "BASEL-II", "BASEL-III", "Tier-1 Capital", "Tier-2 Capital","Nano Lending", "Shadow Banking","For Niladri Only"
          ,"Capital"]

# Add the options to the sidebar
option = st.sidebar.selectbox("Select a Topic", options)

# Display the selected option
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
else:
    st.write("This is BASEL-III")




