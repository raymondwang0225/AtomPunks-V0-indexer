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



# 添加一张图片
image = Image.open("MaIZeKFo_400x400.jpg")
image = image.resize((50, 50))

st.image(image, use_column_width=False, width=50)
st.title("AtomPunks V0 Indexer")

   

    
    
# 加载 JSON 数据到 Pandas DataFrame
atompunk_data_list_v0 = pd.read_json("atompunk_data_list_v0.json")

data_df = pd.DataFrame(
    {
        "mint": [len(atompunk_data_list_v0)]
    }
)

st.data_editor(
    data_df,
    column_config={
        "mint": st.column_config.ProgressColumn(
            "mint volume",
            help="mint volume compliant with hex standard",
            format = "%f",
            min_value=0,
            max_value=10000,
        ),
    },
    use_container_width =True,
    hide_index=True,
)


# 在 Streamlit 中显示 DataFrame
st.dataframe(atompunk_data_list_v0,height=630,use_container_width =True)
# 使用HTML样式来使表格置中
