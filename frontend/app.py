import streamlit as st
import requests
from pathlib import Path

ASSETS_PATH = Path(__file__).absolute().parents[1] / "assets"

def layout():

    st.markdown("# Chatube")
    st.markdown("Ask a question regarding data engineering")
    text_input = st.text_input(label="Ask a questions, see if you get an answer =)")

    if st.button("Send") and text_input.strip() != "":
        response = requests.post(
            "http://127.0.0.1:8000/rag/query",
            json={"prompt": text_input}
        )

        if response.status_code != 200:
            st.error(f"Backend error: {response.status_code}")
            st.text(response.text)
            return

        try:
            data = response.json()
        except ValueError:
            st.error("Response is not valid JSON")
            st.text(response.text)
            return

      # Output section
        st.divider()

        with st.container():
            st.markdown("### Question")
            st.info(text_input)

            st.markdown("### Answer")
            st.success(data.get("answer", "No answer returned"))

            filepath = data.get("filepath")
            if filepath:
                st.markdown("### Source")
                st.code(filepath, language="text")



if __name__ == "__main__":
    layout()
