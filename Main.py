import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Interactive Widgets')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

'Done!!!!'

# for i in range(100):
#   time.sleep(0.1)
#   bar.progress(i)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')

# text = st.text_input('名前を入力してください。')
# satisfactionLevel = st.slider('アプリの満足度は？', 0,100,50)

# 'あなたの名前：', text
# '満足度：', satisfactionLevel
