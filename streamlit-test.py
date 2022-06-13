import streamlit as st
import pandas as pd
import numpy as np

INFERENCE_URL = "http://127.0.0.1:8080/api/v1/model/infer"

def main():
    st.title("This is the header")
    
    uploader = st.file_uploader("Upload Images",type=["png","jpg","jpeg"])

    if uploader is not None:
        pass

if __name__ == "__main__":
    main()