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

# 静态完成百分比（例如：80%）
completion_percentage = 80

# 使用st.bar_chart显示静态条形图
st.bar_chart(completion_percentage / 100)
# 加载 JSON 数据到 Pandas DataFrame
atompunk_data_list_v0 = pd.read_json("atompunk_data_list_v0.json")

# 在 Streamlit 中显示 DataFrame
st.dataframe(atompunk_data_list_v0,height=630,use_container_width =True)
# 使用HTML样式来使表格置中
