import streamlit as st
import pandas as pd
import gspread
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
from streamlit_option_menu import option_menu
from PIL import Image
import toml

cred1_file = toml.load("secrets.toml")


cred1 = {
    "type": cred1_file['gsheets_3']['type'],
    "project_id": cred1_file['gsheets_3']['project_id'],
    "private_key_id": cred1_file['gsheets_3']['private_key_id'],
    "private_key": cred1_file['gsheets_3']['private_key'],
    "client_email": cred1_file['gsheets_3']['client_email'],
    "client_id": cred1_file['gsheets_3']['client_id'],
    "auth_uri": cred1_file['gsheets_3']['auth_uri'],
    "token_uri": cred1_file['gsheets_3']['token_uri'],
    "auth_provider_x509_cert_url": cred1_file['gsheets_3']['auth_provider_x509_cert_url'],
    "client_x509_cert_url": cred1_file['gsheets_3']['client_x509_cert_url'],
    "universe_domain": cred1_file['gsheets_3']['universe_domain'],
}

cred2 = {
    "type": cred1_file['gsheets_4']['type'],
    "project_id": cred1_file['gsheets_4']['project_id'],
    "private_key_id": cred1_file['gsheets_4']['private_key_id'],
    "private_key": cred1_file['gsheets_4']['private_key'],
    "client_email": cred1_file['gsheets_4']['client_email'],
    "client_id": cred1_file['gsheets_4']['client_id'],
    "auth_uri": cred1_file['gsheets_4']['auth_uri'],
    "token_uri": cred1_file['gsheets_4']['token_uri'],
    "auth_provider_x509_cert_url": cred1_file['gsheets_4']['auth_provider_x509_cert_url'],
    "client_x509_cert_url": cred1_file['gsheets_4']['client_x509_cert_url'],
    "universe_domain": cred1_file['gsheets_4']['universe_domain'],
}


cred3 = {
    "type": cred1_file['gsheets_1']['type'],
    "project_id": cred1_file['gsheets_1']['project_id'],
    "private_key_id": cred1_file['gsheets_1']['private_key_id'],
    "private_key": cred1_file['gsheets_1']['private_key'],
    "client_email": cred1_file['gsheets_1']['client_email'],
    "client_id": cred1_file['gsheets_1']['client_id'],
    "auth_uri": cred1_file['gsheets_1']['auth_uri'],
    "token_uri": cred1_file['gsheets_1']['token_uri'],
    "auth_provider_x509_cert_url": cred1_file['gsheets_1']['auth_provider_x509_cert_url'],
    "client_x509_cert_url": cred1_file['gsheets_1']['client_x509_cert_url'],
    "universe_domain": cred1_file['gsheets_1']['universe_domain'],
}

cred4 = {
    "type": cred1_file['gsheets_2']['type'],
    "project_id": cred1_file['gsheets_2']['project_id'],
    "private_key_id": cred1_file['gsheets_2']['private_key_id'],
    "private_key": cred1_file['gsheets_2']['private_key'],
    "client_email": cred1_file['gsheets_2']['client_email'],
    "client_id": cred1_file['gsheets_2']['client_id'],
    "auth_uri": cred1_file['gsheets_2']['auth_uri'],
    "token_uri": cred1_file['gsheets_2']['token_uri'],
    "auth_provider_x509_cert_url": cred1_file['gsheets_2']['auth_provider_x509_cert_url'],
    "client_x509_cert_url": cred1_file['gsheets_2']['client_x509_cert_url'],
    "universe_domain": cred1_file['gsheets_2']['universe_domain'],
}

st.set_page_config(layout="wide")

# this is for styling
st.markdown(f"""
    <style>
        /* Main background color */
        .main {{
            background-color: #b3cf99;
        }}

        /* Text styling for markdown, text inputs, and number inputs */
        .stMarkdown, .stTextInput, .stNumberInput {{
            color: #2d5128;
            font-family: 'Helvetica', 'Arial', sans-serif;
        }}

        /* Heading styling */
        h1, h2, h3, h4, h5, h6 {{
            color: #262730;
            font-family: 'Helvetica', 'Arial', sans-serif;
        }}

        /* Button styling */
        .stButton button {{
            background-color: #2d5128;
            color: white;
            border-color: #2d5128;
            font-family: 'Helvetica', 'Arial', sans-serif;
        }}

        /* Secondary container background color */
        .secondary-container {{
            background-color: #e0e0ef;
        }}

        /* Custom text size */
        .custom-text {{
            font-size: 24px;
            font-family: 'Helvetica', 'Arial', sans-serif;
        }}

        /* Specific styling for class 'css-1d391kg' */
        .css-1d391kg, .css-1d391kg * {{
            background-color: #2d5128 !important;
            font-family: 'Helvetica', 'Arial', sans-serif;
        }}

        /* Optional additional styling for overall text and layout consistency */
        body {{
            font-family: 'Helvetica', 'Arial', sans-serif;
            color: #2d5128;
        }}
        .sidebar .sidebar-content {{
            background-color: #e0e0ef;
            color: #2d5128;
            font-family: 'Helvetica', 'Arial', sans-serif;
        }}
    </style>
""", unsafe_allow_html=True)


# sidebar
img = Image.open("public/images/sentinel-logo-removebg-preview.jfif")
st.sidebar.image(
    img ,
    width= 280,
    channels= "RGB"
)
# write here what your webpage is about
st.sidebar.info("""
Streamlines inventory tracking, pallet positioning, and stock management.
""")

with st.sidebar:
    page = option_menu(
        menu_title="DATA ENTRY FORMS",
        options=["RECEIVE FORM", "RELEASE FORM", "RECEIVE PALLET POSITION", "RELEASE PALLET POSITION"],
        icons=["caret-right-fill", "caret-right-fill", "caret-right-fill", "caret-right-fill"],
        menu_icon="menu-button-wide-fill",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#c2d5aa"},
            "icon": {"color": "#5c7650", "font-size": "13px"}, 
            "nav-link": {
                "font-size": "13px",
                "text-align": "left",
                "margin": "1px",
                "--hover-color": "#e1dace",
            },
            "nav-link-selected": {"background-color": "#bbc9c0"},
            "menu-title": {"font-size": "18px", "font-weight": "bold"},
        },
    )
    
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# if we click receive form
if page == "RECEIVE FORM":
    # Display Title and Description with center alignment and design
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 24px; font-weight: bold; color: #333; margin-top: 20px;">WAREHOUSE MANAGEMENT PORTAL</h2>
        <h4 style="text-align: center; font-size: 18px; font-weight: normal; color: #666;">RECEIVED STOCK DATA ENTRY</h4>
        """, 
        unsafe_allow_html=True
    )
    url = "1w_4eJdKW5l5WeSk5F4yAKARFxUhZVbx9j3_ujeS_BZ0"

    products = ["Armchair", "Trolley", "Pallets"]
    color = ["orange", "black", "green"]

    with st.form(key="received_form"):
        production_id_text = st.text_input("Production ID* (Enter a number)", placeholder="e.g., 000-0-00000")
        product_type = st.selectbox("Product Received*", options=products, index=None)
        color_type = st.selectbox("Color*", options=color, index=None)
        quantity = st.number_input("Quantity*", value=0, step=1, format="%d")
        onboarding_date = st.date_input(label="Date")

        st.markdown("**required*")

        submit_button = st.form_submit_button(label="Submit Details")

        if submit_button:
            if not product_type or not color_type or not quantity or not onboarding_date:
                st.warning("Ensure all mandatory fields are filled.")
                st.stop()
            else:
                received_data = pd.DataFrame(
                    [
                        {
                            "PRODUCTION CODE": production_id_text,
                            "DATE": onboarding_date.strftime("%m-%d-%Y"),
                            "PRODUCT": product_type,
                            "COLOR": color_type,
                            "ITEM CODE": None,
                            "QUANTITY": quantity,
                            "STATUS": "RECEIVED"
                            
                        }
                    ]
                )    
                # Create an empty DataFrame with the same columns for headers
                headers = ["PRODUCTION CODE", "DATE", "PRODUCT", "COLOR", "ITEM CODE", "QUANTITY", "STATUS"]
                display_data = pd.DataFrame(columns=headers)

                # Concatenate headers with the new data
                final_display_df = pd.concat([display_data, received_data], ignore_index=True)
        
                # Show only the header and new data in the DataFrame
                st.dataframe(final_display_df)
                st.success("Received Details successfully submitted!")

                # Use gspread to update the Google Sheets
                creds = ServiceAccountCredentials.from_json_keyfile_dict(cred3, scope)
                client = gspread.authorize(creds)
                sheet = client.open_by_url(f"https://docs.google.com/spreadsheets/d/{url}").sheet1

                # Convert the new data to a list of lists
                new_row = received_data.values.tolist()[0]

                # Append the new row to the sheet
                sheet.append_row(new_row)

if page == "RELEASE FORM":
    # Display Title and Description with center alignment and design
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 24px; font-weight: bold; color: #333; margin-top: 20px;">WAREHOUSE MANAGEMENT PORTAL</h2>
        <h4 style="text-align: center; font-size: 18px; font-weight: normal; color: #666;">RELEASED STOCK DATA ENTRY</h4>
        """, 
        unsafe_allow_html=True
    )
    url = "18qFvLbwSkQg3f-A87sLsLq6h7R3nWam0ZAjRPu5rujc"

    products = ["Armchair", "Trolley", "Pallets"]
    color = ["orange", "black", "green"]

    with st.form(key="released_form"):
        production_id_text = st.text_input("Production ID* (Enter a number)", placeholder="e.g., 000-0-00000")
        product_type = st.selectbox("Product Released*", options=products, index=None)
        color_type = st.selectbox("Color*", options=color, index=None)
        quantity = st.number_input("Quantity*", value=0, step=1, format="%d")
        onboarding_date = st.date_input(label="Date")

        st.markdown("**required*")

        submit_button = st.form_submit_button(label="Submit Details")

        if submit_button:
            if not product_type or not color_type or not quantity or not onboarding_date:
                st.warning("Ensure all mandatory fields are filled.")
                st.stop()
            else:
                received_data = pd.DataFrame(
                    [
                        {
                            "PRODUCTION CODE": production_id_text,
                            "DATE": onboarding_date.strftime("%m-%d-%Y"),
                            "PRODUCT": product_type,
                            "COLOR": color_type,
                            "ITEM CODE": None,
                            "QUANTITY": quantity,
                            "STATUS": "RELEASED"
                            
                        }
                    ]
                )    
                # Create an empty DataFrame with the same columns for headers
                headers = ["PRODUCTION CODE", "DATE", "PRODUCT", "COLOR", "ITEM CODE", "QUANTITY", "STATUS"]
                display_data = pd.DataFrame(columns=headers)

                # Concatenate headers with the new data
                final_display_df = pd.concat([display_data, received_data], ignore_index=True)
        
                # Show only the header and new data in the DataFrame
                st.dataframe(final_display_df)
                st.success("Received Details successfully submitted!")

                # Use gspread to update the Google Sheets
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                creds = ServiceAccountCredentials.from_json_keyfile_name(cred4, scope)
                client = gspread.authorize(creds)
                sheet = client.open_by_url(f"https://docs.google.com/spreadsheets/d/{url}").sheet1

                # Convert the new data to a list of lists
                new_row = received_data.values.tolist()[0]

                # Append the new row to the sheet
                sheet.append_row(new_row)

if page == "RECEIVE PALLET POSITION":
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 24px; font-weight: bold; color: #333; margin-top: 20px;">WAREHOUSE MANAGEMENT PORTAL</h2>
        <h4 style="text-align: center; font-size: 18px; font-weight: normal; color: #666;">PALLET RECEIVE DATA ENTRY</h4>
        """, 
        unsafe_allow_html=True
    )
    url= "1c9wqNXrRX5xrYcJlphQeAQNbbX5vZj9czWbNtnGxf7I"

    # Set up the credentials and client
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(cred1, scope)
    client = gspread.authorize(creds)

    # Open the Google Sheets document by URL and select the 'LOCATOR' sheet
    sheet = client.open_by_url(f"https://docs.google.com/spreadsheets/d/{url}/edit?gid=25345550#gid=25345550")
    worksheet = sheet.worksheet("PALLET RECEIVE")

    data = worksheet.get('A:I')

    existing_data = pd.DataFrame(data[3:], columns=data[2])

    products = ["Armchair", "Trolley", "Pallets"]
    color = ["orange", "black", "green"]

    with st.form(key="received_form"):
        production_id_text = st.text_input("Production ID* (Enter a number)", placeholder="e.g., 000-0-00000")
        product_type = st.selectbox("Product Received*", options=products, index=None)
        color_type = st.selectbox("Color*", options=color, index=None)
        quantity = st.number_input("Quantity*", value=0, step=1, format="%d")
        onboarding_date = st.date_input(label="Date")
        pallet_position = st.text_input("Position No.*", placeholder="e.g., P001")

        st.markdown("**required*")

        submit_button = st.form_submit_button(label="Submit Details")

        if submit_button:
            if not product_type or not color_type or not quantity or not onboarding_date:
                st.warning("Ensure all mandatory fields are filled.")
                st.stop()
            else:
                received_data = pd.DataFrame(
                    [
                        {
                            "PRODUCTION CODE": production_id_text,
                            "DATE": onboarding_date.strftime("%m-%d-%Y"),
                            "PRODUCT": product_type,
                            "COLOR": color_type,
                            "ITEM CODE": None,
                            "QUANTITY": quantity,
                            "POSITION NO.": pallet_position,
                            "STATUS": "RECEIVED"
                            
                        }
                    ]
                )    
                # Create an empty DataFrame with the same columns for headers
                headers = ["PRODUCTION CODE", "DATE", "PRODUCT", "COLOR", "ITEM CODE", "QUANTITY", "STATUS"]
                display_data = pd.DataFrame(columns=headers)

                # Concatenate headers with the new data
                final_display_df = pd.concat([display_data, received_data], ignore_index=True)
        
                # Show only the header and new data in the DataFrame
                st.dataframe(final_display_df)
                st.success("Received Details successfully submitted!")

                # Use gspread to update the Google Sheets
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                creds = ServiceAccountCredentials.from_json_keyfile_dict(cred1, scope)
                client = gspread.authorize(creds)
                sheet = client.open_by_url(f"https://docs.google.com/spreadsheets/d/{url}").sheet1

                # Convert the new data to a list of lists
                new_row = received_data.values.tolist()[0]

                # Append the new row to the sheet
                sheet.append_row(new_row)

if page == "RELEASE PALLET POSITION":
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 24px; font-weight: bold; color: #333; margin-top: 20px;">WAREHOUSE MANAGEMENT PORTAL</h2>
        <h4 style="text-align: center; font-size: 18px; font-weight: normal; color: #666;">PALLET RELEASE DATA ENTRY</h4>
        """, 
        unsafe_allow_html=True
    )
    
    url= "1c9wqNXrRX5xrYcJlphQeAQNbbX5vZj9czWbNtnGxf7I"

    # Set up the credentials and client
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(cred1, scope)
    client = gspread.authorize(creds)

    # Open the Google Sheets document by URL and select the 'LOCATOR' sheet
    sheet = client.open_by_url(f"https://docs.google.com/spreadsheets/d/{url}/edit?gid=25345550#gid=25345550")
    worksheet = sheet.worksheet("PALLET RELEASE")
    
    

    data = worksheet.get('A:I')
    existing_data = pd.DataFrame(data[3:], columns=data[2])

    products = ["Armchair", "Trolley", "Pallets"]
    colors = ["orange", "black", "green"]

    with st.form(key="received_form"):
        production_id_text = st.text_input("Production ID* (Enter a number)", placeholder="e.g., 000-0-00000")
        product_type = st.selectbox("Product Released*", options=products, index=None)
        color_type = st.selectbox("Color*", options=colors, index=None)
        quantity = st.number_input("Quantity*", value=0, step=1, format="%d")
        onboarding_date = st.date_input(label="Date")
        pallet_position = st.text_input("Position No.*", placeholder="e.g., P001")

        st.markdown("**required*")

        submit_button = st.form_submit_button(label="Submit Details")

        if submit_button:
            if not production_id_text or not product_type or not color_type or not quantity or not onboarding_date or not pallet_position:
                st.warning("Ensure all mandatory fields are filled.")
                st.stop()
            else:
                received_data = pd.DataFrame(
                    [
                        {
                            "PRODUCTION CODE": production_id_text,
                            "DATE": onboarding_date.strftime("%m-%d-%Y"),
                            "PRODUCT": product_type,
                            "COLOR": color_type,
                            "ITEM CODE": None,
                            "QUANTITY": quantity,
                            "POSITION NO.": pallet_position,
                            "STATUS": "RELEASED"
                        }
                    ]
                )
                # Create an empty DataFrame with the same columns for headers
                headers = ["PRODUCTION CODE", "DATE", "PRODUCT", "COLOR", "ITEM CODE", "QUANTITY", "STATUS"]
                display_data = pd.DataFrame(columns=headers)

                # Concatenate headers with the new data
                final_display_df = pd.concat([display_data, received_data], ignore_index=True)
        
                # Show only the header and new data in the DataFrame
                st.dataframe(final_display_df)
                st.success("Received Details successfully submitted!")

                # Use gspread to update the Google Sheets
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                creds = ServiceAccountCredentials.from_json_keyfile_dict(cred2, scope)
                client = gspread.authorize(creds)
                sheet = client.open_by_url(f"https://docs.google.com/spreadsheets/d/{url}").sheet1

                # Convert the new data to a list of lists
                new_row = received_data.values.tolist()[0]

                # Append the new row to the sheet
                sheet.append_row(new_row)


    