import streamlit as st

def footer_home():

    st.markdown(f"""
                
        <div style="display:flex; align-items:center; justify-content:center; margin-top:2rem;">
            <p style="font-weight:bold; color:white;">
                Created with ❤️ By Tejwant Kaur
            </p>
        </div>

                """, unsafe_allow_html=True)
    