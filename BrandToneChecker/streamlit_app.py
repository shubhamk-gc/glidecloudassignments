import streamlit as st
import requests

API = "http://localhost:8000"

st.title("Brand Tone Checker")

st.subheader("Create Brand")
tone = st.text_input("Tone keywords (comma separated)")
samples = st.text_area("Sample brand texts (one per line)")

if st.button("Create Brand"):
    if tone.strip() == "" or samples.strip() == "":
        st.warning("Please enter tone keywords and sample texts")
    else:
        try:
            r = requests.post(f"{API}/brands", json={
                "tone_keywords": tone.split(","),
                "samples": samples.split("\n")
            })
            r.raise_for_status()
            st.session_state["brand_id"] = r.json()["brand_id"]
            st.success("Brand created! Brand ID stored in session")
        except Exception as e:
            st.error(f"Error creating brand: {e}")

st.subheader("Check Content")
text = st.text_area("Marketing content")

if st.button("Check Tone"):
    if "brand_id" not in st.session_state:
        st.warning("Please create a brand first!")
    elif text.strip() == "":
        st.warning("Please enter content to check")
    else:
        try:
            r = requests.post(f"{API}/check-tone", json={
                "brand_id": st.session_state["brand_id"],
                "text": text
            })
            r.raise_for_status()
            st.json(r.json())
        except Exception as e:
            st.error(f"Error checking tone: {e}")
