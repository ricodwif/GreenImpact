from pathlib import Path
import streamlit as st
import helper
import settings

st.set_page_config(
    page_title="Deteksi Sampah",
)

st.sidebar.title("Detect Console")

model_path = Path(settings.DETECTION_MODEL)

st.title("Deteksi sampah")
st.write("Dalam rangka mendukung gerakan peduli lingkungan di ITS, website ini dikembangkan sebagai sarana untuk memperkuat peran ITS Waste Bank dalam mengelola sampah dan membangun budaya keberlanjutan.")
st.write("klik (Detect Obejcts) untuk mulai deteksi sampah")
st.markdown(
"""
<style>
    .stRecyclable {
        background-color: rgba(233,192,78,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        margin-top: 0 !important;
        font-size:18px !important;
    }
    .stNonRecyclable {
        background-color: rgba(94,128,173,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        margin-top: 0 !important;
        font-size:18px !important;
    }
    .stHazardous {
        background-color: rgba(194,84,85,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        margin-top: 0 !important;
        font-size:18px !important;
    }

</style>
""",
unsafe_allow_html=True
)

try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)
helper.play_webcam(model)

st.sidebar.markdown("This is a demo of the waste detection model.", unsafe_allow_html=True)
