import streamlit as st
import hashlib

# Password hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Initialize session state for user database and login state
if "user_db" not in st.session_state:
    st.session_state["user_db"] = {
        "admin": hash_password("admin123"),  # Predefined admin user
    }
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = None

# Load external CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navigation menu
menu = ["Home", "About", "Dashboards", "Insights and Analysis", "Feedback", "Chatbot"]

# Sidebar Styling and Navigation
def sidebar_navigation():
    
    # Add a styled title and description
    st.sidebar.markdown("## 🌐 Navigation", unsafe_allow_html=True)
    st.sidebar.markdown("Navigate through the GDP Statistics Dashboard to explore insights, analysis, and tools.")
    st.sidebar.markdown("---")
    
    # Define menu with styled radio buttons
    choice = st.sidebar.radio(
        "Choose a section:",
        menu,
        format_func=lambda x: {
            "Home": "🏠 Home",
            "About": "ℹ️ About",
            "Dashboards": "📊 Dashboards",
            "Insights and Analysis": "📈 Insights & Analysis",
            "Feedback": "📝 Feedback",
            "Chatbot": "🤖 Chatbot",
        }.get(x, x),
    )
    # Return the user's choice
    return choice

# Login/Signup Page
if not st.session_state["logged_in"]:
    st.title("Welcome to the GDP Statistics Dashboard")
    st.markdown("Please **Login** or **Sign Up** to access the dashboard.")

    # Radio button for user choice
    option = st.radio("Choose an option:", ["Login", "Sign Up"], horizontal=True)

    # Login Section
    if option == "Login":
        st.subheader("Login")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        login_btn = st.button("Login")

        if login_btn:
            # Check user in session state database
            if username in st.session_state["user_db"] and st.session_state["user_db"][username] == hash_password(password):
                st.session_state["logged_in"] = True
                st.session_state["current_user"] = username
                st.success(f"Welcome back, {username}!")
            else:
                st.error("Invalid username or password.")

    # Sign-Up Section
    elif option == "Sign Up":
        st.subheader("Sign Up")
        new_username = st.text_input("New Username", key="signup_user")
        new_password = st.text_input("New Password", type="password", key="signup_pass")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_pass")
        signup_btn = st.button("Sign Up")

        if signup_btn:
            # Access user database in session state
            if new_username in st.session_state["user_db"]:
                st.error("Username already exists. Please choose a different one.")
            elif new_password != confirm_password:
                st.error("Passwords do not match. Please try again.")
            elif not new_username or not new_password:
                st.error("Username and password cannot be empty.")
            else:
                st.session_state["user_db"][new_username] = hash_password(new_password)
                st.success("Account created successfully! Please log in.")

# Logged-In State
else:
    # Sidebar Navigation
    selected_section = sidebar_navigation()

    # Render selected page content
    if selected_section == "Home":
        st.title("Welcome to the GDP Statistics Dashboard")
        st.image("Home Page.png", use_container_width=True)

        # Title
        st.title("🏠 Welcome to the Economic Dashboard!")

        # Subtitle
        st.subheader("🌏 A Comprehensive View of India's Economic Pulse")

        # Overview Section
        st.markdown("""
        ### 📖 **Homepage Overview**
        The homepage serves as the **gateway** to understanding India's economic health. It's designed to provide:  
        - **High-level insights** into key metrics 📊.  
        - A snapshot of trends driving the economy 🚀.  
        - Easy navigation to deeper analyses through the dashboard features 🧭.  

        ---

        ### 🎯 **Purpose**
        The homepage acts as your **starting point**, offering a quick overview of:  
        - **Economic health** through key statistics.  
        - Insights into **GDP growth** and **employment trends**.  
        - Highlights from **key sectors** like agriculture 🌾, industry 🏭, services 🛠️, and technology 💻.  

        This page sets the tone for exploring the intricate dynamics of India's evolving economy. 🌟  

        ---

        ### 🌟 **Features at a Glance**
        1️⃣ **GDP Growth Rate** 📈:  
        - Displays the **current GDP value** (e.g., ₹250 lakh crore in 2023) with a comparison to the **previous period** (growth rate: +6.5%).  
        - **Color-coded indicators** to show performance trends:  
            - 🟢 Positive Growth  
            - 🔴 Negative Growth  

        2️⃣ **Sector Performance** 🏭💻:  
        - Highlights contributions from key sectors:  
            - 🌾 **Agriculture**: ₹40 lakh crore (16% GDP contribution).  
            - 🏭 **Industry**: ₹60 lakh crore (24% GDP contribution).  
            - 🛠️ **Services**: ₹120 lakh crore (48% GDP contribution).  
            - 💻 **Technology**: ₹30 lakh crore (12% GDP contribution).  
        - Shows the **top-performing sectors** in the current quarter.

        3️⃣ **Trending Metrics** 📊:  
        - A **line graph** visualizing trends over time:  
            - **GDP Growth**: Observe how GDP has evolved over the last 5 years.  
            - **Employment Trends**: Track changes in employment rates across cities.  
        - Compare **city-level trends** for actionable insights.

        ---

        ### 🔑 **Why Explore This Dashboard?**
        This homepage offers a clear and concise introduction, ensuring you:  
        - Stay updated on the **latest economic metrics** 📰.  
        - Understand the **drivers of growth** across India 🚀.  
        - Navigate easily to **deeper data insights** within the dashboard.

        🔎 **Dive deeper** by exploring interactive features in the sidebar!  
        """)


    elif selected_section == "About":
        # Title and Introduction
        st.title("🌏 India's Economic Pulse: GDP & Employment Dashboard")

        st.markdown("""
        Welcome to the **India GDP Dashboard**! 🎉 This interactive platform provides an in-depth exploration of 
        city-wise GDP 📈 and employment statistics 👩‍💼👨‍💻 across India, showcasing the nation's economic landscape in a dynamic and engaging way.
        """)

        # About Section
        st.markdown("""
        ### 🔍 **About the Dashboard**
        This project highlights critical **sector-specific contributions** across **4 key sectors**:  
        1️⃣ **Agriculture** 🌾  
        2️⃣ **Industry** 🏭  
        3️⃣ **Services** 🛠️  
        4️⃣ **Technology** 💻  

        Key **economic indicators** presented include:  
        - 🧠 **Patents per 100K inhabitants** (e.g., Bengaluru: 15, Pune: 10).  
        - 💰 **R&D expenditure** (₹1,200 crore in Hyderabad alone in 2023).  
        - 📉 **Unemployment rates** (Youth unemployment: 18% nationally).  

        The dashboard also focuses on **youth employment trends** and **sectoral distributions**, offering insights into how different industries impact employment opportunities for younger demographics.  

        ---

        ### ✨ **Key Highlights**
        📌 **GDP Growth Trends**: Visualize city-level GDP growth across India, highlighting top performers like:  
        - 🌟 Bengaluru: ₹15.5 lakh crore (2023)  
        - 🌟 Delhi: ₹14.2 lakh crore (2023)  

        📌 **Employment Statistics**:  
        - **Youth unemployment**: 18% nationwide, with urban areas seeing a higher rate (22%).  
        - **Sector-wise employment**: Services dominate in cities like Mumbai, accounting for 65% of employment.  

        📌 **Sector Contributions**:  
        - **Agriculture** 🌾: Major contributor in rural areas (30% GDP in some states).  
        - **Industry** 🏭: Driving manufacturing hubs like Pune and Chennai.  
        - **Services** 🛠️: Largest employment generator (65% GDP contribution in metros).  
        - **Technology** 💻: Bengaluru leads, contributing 10% to the tech sector GDP nationwide.  

        📌 **Economic Indicators**:  
        - 📜 **Patents**: Bengaluru (15/100K), Hyderabad (12/100K).  
        - 💸 **R&D Expenditure**: ₹3,500 crore annually in top cities.  

        ---

        ### 🎯 **Why This Dashboard?**
        The primary goal of this initiative is to empower policymakers, analysts, and stakeholders with **actionable insights**. 🎯 By leveraging this data, decision-makers can:  
        1. **Identify strengths** and **weaknesses**.  
        2. Formulate **strategies** to foster economic growth and development 🚀.  
        3. Pinpoint areas needing **intervention** to improve productivity and sustainability 🌱.  

        ---

        ### 📊 **Dashboard Features**
        Explore various insights through the **interactive options** in the sidebar:  
        - **GDP growth trends** 🌟.  
        - **Employment statistics** 👷‍♂️👩‍💻.  
        - Contributions from key sectors:  
        - Agriculture 🌾  
        - Industry 🏭  
        - Services 🛠️  
        - Technology 💻  
        - Economic indicators, including:  
        - 🧠 **Patents per 100K inhabitants**.  
        - 💰 **R&D expenditures**.  

        Navigate through the data and gain **valuable insights** into India's city-level economic trends. 📈🌏  
        """)



    # Dashboard Page
    # Dashboard Page
    elif selected_section == "Dashboards":
        st.title("Explore Dashboards")
        tab1, tab2, tab3 = st.tabs(["GDP Statistics", "Employment Statistics", "Sector-wise Statistics"])

        with tab1:
            
            st.header("GDP Statistics")
            st.image("GDP Statistics.png", use_container_width=True)
            # Title of the Dashboard

            # Title with effect
            st.markdown("<h1>🌍 GDP Statistics Dashboard</h1>", unsafe_allow_html=True)

            # Introductory description with statistics and emojis
            st.markdown("""
            Welcome to the **GDP Statistics Dashboard**! This interactive tool provides a comprehensive view of India's economic performance, 
            offering valuable insights into key trends and metrics. 📊 Here's what you'll discover:


            ### 📈 GDP Growth Trends 
            - **5.6% annual average growth** over the past decade. 🚀
            - Significant growth spurts in cities like **Bangalore (8.2%)**, **Mumbai (7.5%)**, and **Delhi (7.1%)**.
            - Visualization of **regional disparities** and economic trajectories across India.



            ### 💡 Patents per 100K Inhabitants
            - Cities like **Hyderabad** and **Pune** lead the pack with over **45 patents per 100K residents**. 🧠✨
            - The national average stands at **18 patents per 100K residents**—a sign of growing innovation.



            ### 🔬 R&D Expenditures
            - India’s total R&D spending: **₹2.5 trillion annually**. 💰
            - Metro cities account for **60% of R&D investments**, with **Mumbai (20%)** and **Bangalore (18%)** dominating.



            This dashboard is a vital tool for:
            - 📜 Policymakers: Shape informed strategies to reduce regional economic disparities.
            - 🧑‍🔬 Researchers: Understand innovation hubs and their impact on growth.
            - 🧮 Analysts: Dive deep into economic trends and identify potential opportunities.

            🌟 **Explore the dashboard below and uncover the data behind the numbers!**
            """, unsafe_allow_html=True)




        with tab2:
            st.header("Employment Statistics")
            st.image("Employement Statistics.png", use_container_width=True)
        
            # Title and Introduction
            st.title("📊 Employment Statistics Dashboard")
            st.write("""
            This section provides an in-depth analysis of employment trends, offering insights into the workforce's health and opportunities.
            """)

            # Key Insights
            st.subheader("🔍 Key Insights")

            # Overall Employment Trends
            st.markdown("### 📈 Overall Employment Trends")
            st.markdown("""
            - The **national employment rate** has fluctuated between **45% and 50%** over the last decade.
            - 📅 The **highest employment rate** was recorded in **2018 at 50.3%**, while the lowest was during the **2020 pandemic downturn at 42.6%**.
            """)

            # Youth Unemployment Rates
            st.markdown("### 🧑‍🎓 Youth Unemployment Rates")
            st.markdown("""
            - Youth unemployment (ages **15–24**) currently stands at **24%**, significantly higher than the overall unemployment rate of **7.5%**.
            - 🌆 **Urban areas** show higher youth unemployment rates (**30%**) compared to **rural areas** (**20%**).
            """)

            # Sectoral Employment Distribution
            st.markdown("### 🏢 Sectoral Employment Distribution")
            st.markdown("""
            - 🌾 **Agriculture** employs **42%** of the workforce but contributes only **18% to GDP**, indicating **underemployment**.
            - 🏭 The **industry sector** accounts for **25% of employment**.
            - 💼 The **services sector** employs **33%** of the workforce, contributing a significant **55% to GDP**.
            - 💻 **Technology-driven jobs** in urban areas have seen a growth of **12% year-on-year**, driven by IT and fintech sectors.
            """)

            # Highlight Benefits
            st.markdown("### 🛠️ This dashboard helps in:")
            st.markdown("""
            - ✅ **Understanding labor market dynamics**.
            - ✅ **Identifying trends in youth employment** and the challenges they face.
            - ✅ **Analyzing sectoral workforce distribution** to guide policy decisions aimed at addressing unemployment and workforce imbalances.
            """)

            # Footer
            st.markdown("---")
            st.write("🚀 Empowering insights for a better workforce!")

        with tab3:
            st.header("Sector-wise Statistics")
            st.image("Sector-wise Statstics.png", use_container_width=True)

            # Page Title
            st.header("📊 Sector-wise Statistics Dashboard")
            st.markdown("---")

            # Description Section
            st.markdown("""
            Dive deep into the **economic contributions** of various sectors and uncover their vital roles in shaping **India's GDP**. Here's what each sector brings to the table:

            ### 🌾 **Agriculture Sector**
            - **GDP Contribution**: 🪴 *~17.8%* of India's GDP (2022).
            - **Employment**: 👩‍🌾 Provides livelihood for **58%** of the rural population.
            - **Exports**: 🚜 Drives **$50 billion+** in agricultural exports annually.


            ### 🏭 **Industry Sector**
            - **GDP Contribution**: ⚙️ *~29.6%* of GDP.
            - **Growth**: 📈 **7.3% annual growth** in industrial output.
            - **Investments**: 🏗️ Attracted **$100 billion+** in FDI in manufacturing over the last decade.


            ### 💼 **Services Sector**
            - **GDP Dominance**: 🌐 Contributes a massive **~52.6%** to GDP.
            - **Employment**: 🛎️ Employs **~35%** of the workforce.
            - **IT Sector**: 💻 Accounts for **$230 billion+** in IT exports, solidifying India's tech leadership.


            ### 🚀 **Technology Sector**
            - **Innovation Hub**: 🌟 Hosts **50,000+ startups**, with **100+ unicorns** 🦄 as of 2023.
            - **R&D Spending**: 💡 Over **$80 billion** invested in research and development.
            - **Global Impact**: 📡 India ranks in the **top 10 nations** for AI and robotics innovation.


            ### 🌟 Why This Dashboard?
            This dashboard enables a **holistic understanding** of how these sectors interconnect to drive economic growth. It helps you:
            - Identify **areas for growth** 🚀.
            - Explore **investment opportunities** 💰.
            - Gain insights for **strategic planning** 📋.

            """)


    # Dashboards Page
    elif selected_section == "Insights and Analysis":
        st.title("📊 GDP Insights")
        st.markdown("""
        ## Economic Overview
        Explore the latest economic statistics and trends through detailed visualizations and summary cards.
        """)
        
        # Display Key Statistics as Cards
        st.markdown("### Key Economic Statistics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("GDP Growth Rate", "3.8%", "⬆ 0.5%")
            st.caption("Quarter-over-quarter growth.")
        with col2:
            st.metric("Employment Rate", "95.2%", "⬆ 0.3%")
            st.caption("Percentage of the workforce employed.")
        with col3:
            st.metric("Inflation Rate", "4.1%", "⬇ 0.2%")
            st.caption("Year-over-year price change.")
        
        st.markdown("---")
        
        # Sector Performance
        st.markdown("### Sector Performance")
        st.markdown("""
        Analyze the contributions of various sectors to the GDP. The performance indicators highlight the economic health of major industries.
        """)
        
        # Sector Statistics Table
        st.table({
            "Sector": ["Agriculture", "Manufacturing", "Services", "Technology", "Energy"],
            "Contribution to GDP (%)": [12.3, 25.4, 47.8, 8.6, 5.9],
            "Growth Rate (%)": [2.1, 3.5, 4.8, 6.2, 2.8],
        })
        
        st.markdown("---")
        
        # Trend Analysis
        st.markdown("### GDP Trend Analysis")
        st.line_chart({
            "Year": [2019, 2020, 2021, 2022, 2023],
            "GDP (in Trillions)": [2.3, 2.1, 2.5, 2.7, 3.0],
        })
        
        st.markdown("""
        The above chart shows the steady recovery of the economy after a dip in 2020 due to global challenges.
        """)

        st.markdown("---")
        
        # Insights
        st.markdown("### Insights")
        st.markdown("""
        - The **Services sector** remains the backbone of the economy, contributing nearly 50% of the GDP.
        - **Technology and Energy sectors** are showing significant growth, with technology leading at 6.2%.
        - The **Inflation rate** has seen a decline, indicating stability in consumer prices.
        """)

   # Feedback Page
    elif selected_section == "Feedback":
        st.title("Feedback")
        st.markdown("""
        We value your feedback to improve the GDP Statistics Dashboard.  
        Please let us know your thoughts, suggestions, or any issues you've encountered.
        """)

        # User Details
        name = st.text_input("Your Name", placeholder="Enter your name here")
        email = st.text_input("Your Email (optional)", placeholder="Enter your email for follow-up (optional)")
        
        # Feedback Categories
        st.subheader("Feedback Category")
        category = st.selectbox("What is your feedback related to?", 
                                ["General Feedback", "Data Accuracy", "Dashboard Design", 
                                "Feature Suggestions", "Bugs/Issues", "Other"])

        # Specific Feedback Input
        feedback = st.text_area("Your Feedback", placeholder="Write your feedback here...")
        
        # Satisfaction Rating
        st.subheader("How satisfied are you with the dashboard?")
        satisfaction = st.slider("Rate your experience:", 1, 10, 5, help="1 = Very Unsatisfied, 10 = Extremely Satisfied")
        
        # Additional Input: Features You’d Like to See
        st.subheader("Additional Suggestions")
        suggestions = st.text_area("What new features would you like to see? (Optional)", 
                                    placeholder="E.g., Interactive charts, Downloadable reports, Predictive analysis")

        # Submit Feedback Button
        if st.button("Submit Feedback"):
            if not feedback.strip():
                st.error("Please enter your feedback before submitting.")
            else:
                st.success("Thank you for your feedback!")
                st.markdown(f"""
                **Feedback Summary**:  
                - Name: {name if name else "Not Provided"}  
                - Email: {email if email else "Not Provided"}  
                - Category: {category}  
                - Satisfaction Rating: {satisfaction}/10  
                - Feedback: {feedback}  
                - Additional Suggestions: {suggestions if suggestions else "None"}
                """)
                # Code to save feedback in the backend can go here

    # Chatbot Page  
    elif selected_section == "Chatbot":
        st.title("Chatbot Assistant")
        st.markdown("""
        Welcome to the chatbot assistant!  
        Ask questions about the GDP Statistics Dashboard, features, or insights.  
        """)
        
        if "messages" not in st.session_state:
            st.session_state["messages"] = []

        # Predefined Responses
        predefined_responses = {
            "gdp": "The GDP statistics highlight trends across various cities, focusing on growth rates and sector-wise contributions. Navigate to 'Dashboards' to explore detailed visualizations.",
            "employment": "Employment statistics cover youth unemployment rates, sectoral employment trends, and more. Check the Employment Statistics tab in the dashboard for detailed insights.",
            "features": "Our dashboard provides: \n- GDP growth trends\n- Employment statistics\n- Sector-wise insights\n- Key economic indicators. \nExplore the tabs in the dashboard for more.",
            "issue": "I'm sorry to hear that you're facing an issue. Could you provide more details so we can assist you better?",
            "feedback": "You can submit your feedback in the 'Feedback' section. We appreciate your input to improve the dashboard!",
            "logout": "To log out, use the Logout button in the sidebar.",
        }

        # Function to generate chatbot responses
        def chatbot_response(user_message):
            for keyword, response in predefined_responses.items():
                if keyword in user_message.lower():
                    return response
            return "I'm here to help with any questions about the GDP Statistics Dashboard. Could you provide more details?"

        # Chat Interface
        user_input = st.text_input("You:", placeholder="Type your question here...")
        if user_input:
            # Save user message
            st.session_state["messages"].append({"role": "user", "content": user_input})
            # Generate chatbot response
            bot_response = chatbot_response(user_input)
            st.session_state["messages"].append({"role": "bot", "content": bot_response})

        # Display the chat messages
        for message in st.session_state["messages"]:
            if message["role"] == "user":
                st.chat_message("user").write(message["content"])
            else:
                st.chat_message("assistant").write(message["content"])




    # Logout Button
    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["current_user"] = None
        st.info("You have been logged out. Please log in again.")