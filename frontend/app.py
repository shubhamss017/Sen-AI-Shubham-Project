import streamlit as st
import requests
import pandas as pd

BASE_URL = "http://127.0.0.1:8000/api"

st.set_page_config(
    page_title="AI CRM Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI CRM Agent Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Agent",
        "RAG Search",
        "Thread Viewer",
        "Contact Viewer"
    ]
)

# ====================================================
# AGENT TAB
# ====================================================

with tab1:

    st.header("AI Agent Execution")

    email_id = st.number_input(
        "Email ID",
        min_value=1,
        value=1
    )

    if st.button("Run Agent"):

        with st.spinner("Analyzing Email..."):

            response = requests.post(
                f"{BASE_URL}/agent/execute/{email_id}"
            )

            data = response.json()

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Category",
                data.get("category", "-")
            )

            col2.metric(
                "Sentiment",
                data.get("sentiment", "-")
            )

            col3.metric(
                "Priority",
                data.get("priority", "-")
            )

            col4.metric(
                "Confidence",
                data.get("confidence", "-")
            )

            st.divider()

            st.subheader("Agent Decision")

            st.write(
                "Requires Human Review:",
                data.get("requires_human")
            )

            st.write(
                "Action Type:",
                data.get("action_type")
            )

            st.divider()

            st.subheader("Summary")

            st.info(
                data.get("summary", "")
            )

            st.divider()

            st.subheader("Suggested Reply")

            st.success(
                data.get("suggested_reply", "")
            )

# ====================================================
# RAG TAB
# ====================================================

with tab2:

    st.header("📚 Knowledge Base Search")

    query = st.text_input(
        "Enter Query",
        placeholder="refund"
    )

    if st.button("Search"):

        response = requests.get(
            f"{BASE_URL}/rag/search",
            params={"query": query}
        )

        if response.status_code == 200:

            data = response.json()

            col1, col2 = st.columns(2)

            col1.metric(
                "Source",
                data["source"]
            )

            col2.metric(
                "Distance",
                round(data["distance"], 4)
            )

            st.subheader(
                "Retrieved Policy"
            )

            st.success(
                data["content"]
            )

        else:

            st.error(response.text)

# ====================================================
# THREAD VIEWER
# ====================================================

with tab3:

    st.header("Thread Viewer")

    thread_id = st.text_input(
        "Thread ID"
    )

    if st.button("Load Thread"):

        response = requests.get(
            f"{BASE_URL}/thread/{thread_id}"
        )

        st.json(response.json())

# ====================================================
# CONTACT VIEWER
# ====================================================

with tab4:

    st.header("Contact Viewer")

    contact_id = st.number_input(
        "Contact ID",
        min_value=1,
        value=1,
        key="contact"
    )

    if st.button("Load Contact"):

        response = requests.get(
            f"{BASE_URL}/contact/{contact_id}"
        )

        st.json(response.json())