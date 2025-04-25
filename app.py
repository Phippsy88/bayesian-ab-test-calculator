
import streamlit as st
import numpy as np

st.set_page_config(page_title="Bayesian A/B Test Calculator", layout="centered")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call it at the top of your app
local_css("styles.css")

st.title("📊 Vervaunt's Bayesian A/B Test Calculator")

st.markdown("Use Bayesian inference to evaluate the probability that one variant is better than the other based on your test data.")

st.header("Input Data")

with st.form("ab_form"):
    col1, col2 = st.columns(2)
    with col1:
        a_conversions = st.number_input("Conversions (A)", min_value=0, value=50)
        a_total = st.number_input("Total Visitors (A)", min_value=1, value=100)
    with col2:
        b_conversions = st.number_input("Conversions (B)", min_value=0, value=60)
        b_total = st.number_input("Total Visitors (B)", min_value=1, value=100)

    submitted = st.form_submit_button("Calculate")

if submitted:
    samples = 100000
    a_samples = np.random.beta(a_conversions + 1, a_total - a_conversions + 1, samples)
    b_samples = np.random.beta(b_conversions + 1, b_total - b_conversions + 1, samples)

    prob_b_better = np.mean(b_samples > a_samples)
    uplift = (np.mean(b_samples) - np.mean(a_samples)) / np.mean(a_samples) * 100

    st.header("Results")
    st.metric("Probability B is better than A", f"{prob_b_better*100:.2f}%")
    st.metric("Expected Uplift", f"{uplift:.2f}%")
