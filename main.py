import pyshorteners
import barcode
from barcode.writer import SVGWriter
from streamlit.components.v1 import html
import streamlit as st


st.write("Enter the long URL below:")
long_url = st.text_input("Long URL:")
if st.button("Shorten"):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    st.write("Shortened URL:", short_url)
    # Generate barcode SVG
    code128 = barcode.Code128(short_url, writer=SVGWriter())
    svg = code128.render()
    
    # Display barcode SVG in Streamlit app
    html_object = f"<div>{svg}</div>"
    html(html_object, width=500, height=100)