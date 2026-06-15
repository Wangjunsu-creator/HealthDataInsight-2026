import streamlit as st
import streamlit.components.v1 as components

# 页面基础配置
st.set_page_config(page_title="成果展示系统", layout="wide")

st.title("项目可视化展示平台")
st.divider()

page_url = "https://Wangjunsu-creator.github.io/HealthDataInsight-2026/"

# 调高高度适配多层嵌套网页，滚动开启
components.iframe(
    src=page_url,
    width="100%",
    height=1200,
    scrolling=True
)

st.divider()
st.caption("前端静态展示页面嵌入Streamlit交互式框架")
