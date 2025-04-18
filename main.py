import os

import streamlit as st
from utils import generate_xiaohongshu

st.header('爆款小红书AI写作助手')
with st.sidebar:
    open_api_key = st.text_input('请输入OpenAI密钥(环境变量部署填1)：',type = 'password')
    st.markdown('[获取OpenAI密钥](https://platform.openai.com/api-keys)')
    base_url = st.text_input('请输入镜像网站地址(如有)：')


theme = st.text_input('主题')
submit = st.button('开始写作')

if submit and not open_api_key:
    st.info('请输入你的OpenAI密钥')
    st.stop()

if submit and not theme:
    st.info('请输入生成主题')
    st.stop()

if submit:
    if base_url:
        with st.spinner('AI正努力创作中…'):
            result = generate_xiaohongshu(theme, open_api_key,base_url=base_url)
    if not base_url:
        with st.spinner('AI正努力创作中…'):
            result = generate_xiaohongshu(theme, open_api_key)

    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        for i in range(1,6):
            st.markdown(f'##### 小红书标题{i}')
            st.write(result.titles[i-1])
    with right_column:
        st.markdown(f'##### 小红书正文')
        st.write(result.content)
