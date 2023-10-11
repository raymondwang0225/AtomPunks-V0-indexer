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

# 加载 JSON 数据到 Pandas DataFrame
atompunk_data_list_v0 = pd.read_json("atompunk_data_list_v0.json")

# 使用HTML样式来使表格置中并限制最大宽度
st.markdown(
    f'<div style="display: flex; justify-content: center;"><table style="width: 80%; text-align: center;">{atompunk_data_list_v0.to_html(classes="dataframe", index=False)}</table></div>',
    unsafe_allow_html=True
)
