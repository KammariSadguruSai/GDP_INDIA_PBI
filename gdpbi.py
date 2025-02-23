import streamlit as st
import pandas as pd
import bcrypt
import os

# File to store user credentials
USER_DATA_FILE = "users.csv"

# Initialize user data file
if not os.path.exists(USER_DATA_FILE):
    df = pd.DataFrame(columns=["username", "password", "dob"])
    df.to_csv(USER_DATA_FILE, index=False)

# Hashing functions
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

# Authentication Functions
def create_account(username, password, dob):
    df = pd.read_csv(USER_DATA_FILE)
    if username in df["username"].values:
        return "Username already exists!"
    hashed_password = hash_password(password)
    new_user = pd.DataFrame([[username, hashed_password, dob]], columns=["username", "password", "dob"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(USER_DATA_FILE, index=False)
    return "Account created successfully!"

def authenticate(username, password):
    df = pd.read_csv(USER_DATA_FILE)
    user = df[df["username"] == username]
    if not user.empty and verify_password(password, user.iloc[0]["password"]):
        return True
    return False

def reset_pin(username, dob, new_password):
    df = pd.read_csv(USER_DATA_FILE)
    user_idx = df.index[df["username"] == username].tolist()
    if user_idx and df.loc[user_idx[0], "dob"] == dob:
        df.loc[user_idx[0], "password"] = hash_password(new_password)
        df.to_csv(USER_DATA_FILE, index=False)
        return "PIN reset successful!"
    return "Incorrect username or date of birth."

# Session Management
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None

# UI: Authentication Pages
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

def signup_page():
    st.title("Create Account")
    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")
    dob = st.text_input("Date of Birth (YYYY-MM-DD)")
    if st.button("Sign Up"):
        msg = create_account(username, password, dob)
        st.success(msg) if "successfully" in msg else st.error(msg)

def reset_page():
    st.title("Reset PIN")
    username = st.text_input("Username")
    dob = st.text_input("Date of Birth (YYYY-MM-DD)")
    new_password = st.text_input("New Password", type="password")
    if st.button("Reset PIN"):
        msg = reset_pin(username, dob, new_password)
        st.success(msg) if "successful" in msg else st.error(msg)

# UI: App Pages
def home_page():
    st.title("Welcome to India Insights")
    st.subheader("📊 India's GDP Overview")
    st.write(
        "India is the world's fifth-largest economy by nominal GDP. The country has seen rapid growth over the past few decades due to its large workforce, booming IT sector, and diverse industries."
    )
    st.subheader("🎨 Indian Art & Culture")
    st.write(
        "India has a rich history of art and culture, ranging from ancient cave paintings in Ajanta to modern Bollywood cinema. The fusion of traditional and contemporary art makes India's cultural landscape unique."
    )

def about_page():
    st.title("About")
    st.write("This web application provides insights into India's economy and culture. Built using Streamlit.")

def dashboard_page():
    st.title("GDP Dashboard")
    st.write("Below is the embedded Power BI dashboard for India's GDP.")
    st.markdown(
        '<iframe title="GDP_DASH" width="1140" height="541.25" '
        'src="https://app.powerbi.com/reportEmbed?reportId=8fa265a1-ef46-4d83-83d8-49383004f7c6&autoAuth=true&ctid=b45e253c-d9f0-4c81-b778-8d3197741240" '
        'frameborder="0" allowFullScreen="true"></iframe>', 
        unsafe_allow_html=True
    )

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.success("Logged out successfully!")
    st.experimental_rerun()

# Sidebar Navigation
def app():
    st.sidebar.title("Navigation")
    menu = ["Home", "About", "Dashboard", "Logout"]
    choice = st.sidebar.radio("Go to", menu)

    if choice == "Home":
        home_page()
    elif choice == "About":
        about_page()
    elif choice == "Dashboard":
        dashboard_page()
    elif choice == "Logout":
        logout()

# Authentication Handling
if not st.session_state.logged_in:
    st.sidebar.title("Auth")
    auth_menu = ["Login", "Sign Up", "Reset PIN"]
    auth_choice = st.sidebar.radio("Choose", auth_menu)

    if auth_choice == "Login":
        login_page()
    elif auth_choice == "Sign Up":
        signup_page()
    elif auth_choice == "Reset PIN":
        reset_page()
else:
    app()
