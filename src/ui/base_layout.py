import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
                .stApp{
                    background: #5865F2 !important;
                    color: #35348c !important;
                }
                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding: 2rem 3rem !important;
                    margin-left: 1rem !important;
                    border-radius: 5rem !important;
                    max-width: 300px !important;
                }
                .block-container {
                    padding-bottom: 0rem !important;
                }
        </style>
                """
                ,unsafe_allow_html=True)
    
def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp{
                    background-color: #E0E3FF !important;
                    
                }
        </style>
                """
                ,unsafe_allow_html=True)
    

def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


            # /* Hide Top Bar of Streamlit */
            # #MainMenu, footer, header {
            #     visibility: hidden;
            # }
                
            /* space above home screen */
            .block-container {
                padding-top: 1.5rem !important;
            }
                
            h1, h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                margin-bottom: 0rem !important;
            }
            h1{  /* Snap Class */
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
            }
            h2{ /* I am student */
                font-size: 1.8rem !important;
                line-height: 0.9 !important;
                font-weight: 350 !important;
                
            }
            
            h3, 4, p {
                
                font-family: 'Outfit' !important;
            }
            
            /* primary button */
            button{
                background-color: #5865F2 !important;
                border-radius: 1.5rem  !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important; /* hover vli transition slow hove */
            }
            button[kind="secondary"] {
                background-color: #EB459E !important;
            }
            button[kind="tertiary"] {
                background-color: black !important;
            }
            button:hover {
                transform: scale(1.05);
            }
                
        </style>
                """
                ,unsafe_allow_html=True)
    