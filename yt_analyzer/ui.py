import streamlit as st
from yt_analyzer import build_youtube_agent

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout = "centered"
)


st.title("AI Youtube Video Analyzer")

# cache - fast access , temp storage => most frequent accessed
@st.cache_resource # we dont wanna build the yt agent from scratch
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# input box
video_url = st.text_input("Enter youtube URL") # string

button = st.button("Analyze Video")# store as True/False

if video_url and button:
    with st.spinner("Analyzing video...."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)