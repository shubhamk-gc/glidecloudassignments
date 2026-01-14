import streamlit as st
import requests

API = "http://localhost:8000"

st.title("Brand Tone Checker")

# ----------------------------------
# Load brands
# ----------------------------------
def load_brands():
    try:
        r = requests.get(f"{API}/brands")
        return r.json()
    except:
        return []

brands = load_brands()

# ----------------------------------
# Sidebar – Brand selection
# ----------------------------------
st.sidebar.subheader("Select Brand")

selected_brand = st.sidebar.selectbox(
    "Choose a brand",
    [""] + brands
)

st.sidebar.markdown("---")

# ----------------------------------
# Create Brand
# ----------------------------------
st.sidebar.subheader("Create New Brand")

brand_name = st.sidebar.text_input("Brand name")
tone = st.sidebar.text_input("Tone keywords (comma separated)")
samples = st.sidebar.text_area("Sample brand texts (one per line)")

if st.sidebar.button("Create Brand"):
    if not brand_name or not tone or not samples:
        st.sidebar.warning("Fill all fields")
    else:
        try:
            r = requests.post(f"{API}/brands", json={
                "brand_name": brand_name,
                "tone_keywords": [x.strip() for x in tone.split(",")],
                "samples": [x.strip() for x in samples.split("\n") if x.strip()]
            })
            r.raise_for_status()
            st.sidebar.success("Brand created!")
            st.rerun()
        except Exception as e:
            st.sidebar.error(f"Error: {e}")

# ----------------------------------
# Tone Checking
# ----------------------------------
st.subheader("Check Content Tone")

if not selected_brand:
    st.info("Select a brand from the sidebar")
else:
    st.write(f"Using brand: **{selected_brand}**")

    text = st.text_area("Marketing content")

    if st.button("Check Tone"):
        if not text.strip():
            st.warning("Please enter content")
        else:
            try:
                r = requests.post(f"{API}/check-tone", json={
                    "brand_name": selected_brand,
                    "text": text
                })
                r.raise_for_status()
                result = r.json()

                st.subheader("Results")
                st.metric("Tone Match Score", round(result["score"], 3))
                st.write("**Brand Tone:**", result["tone"])
                st.write("**LLM Review:**")
                st.text(result["llm_result"])
            except Exception as e:
                st.error(f"Error checking tone: {e}")
