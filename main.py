import streamlit as st
from typing import List
from dataclasses import dataclass
from itertools import product
import json;
from PIL import Image
import requests
import pandas as pd
import numpy as np
import csv
import plost
import matplotlib.pyplot as plt
import altair as alt


st.set_page_config(layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("AtomPunks V0 Indexer")


atompunk_data_list_v0 =pd.read_json("atompunk_data_list_v0.json")


#row size 35 px
st.dataframe(df)
