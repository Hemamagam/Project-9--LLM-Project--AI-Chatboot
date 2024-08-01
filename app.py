import streamlit as st
from langchain_config import summarize_articles, get_news_articles

# Streamlit UI
st.title('Times of India News Chatbot')
st.write('Enter your query to get the latest news articles summarized.')

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Add debugging
st.write("Fetching news articles...")
articles = get_news_articles()
if articles:
    st.write(f"Fetched {len(articles)} articles.")
else:
    st.write("No articles fetched.")

query = st.text_input('Query', key='query')

if st.button('Get News'):
    if articles:
        summaries = summarize_articles(articles)
        if summaries:
            st.session_state.conversation.append({'query': query, 'summaries': summaries})
        else:
            st.write("No summaries generated.")
    else:
        st.write("No articles to summarize.")

for entry in st.session_state.conversation:
    st.write(f"**Query:** {entry['query']}")
    for i, summary in enumerate(entry['summaries'], 1):
        st.write(f"**Summary {i}:** {summary}")