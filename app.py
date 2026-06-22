import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
import pandas as pd
import re

# Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="📈 AI Market Gap Analyzer", layout="wide")

# Stylish HTML headers
st.markdown("""
    <style>
        .main-title { text-align: center; color: #0288D1; font-size: 42px; font-weight: bold; margin-bottom: 10px; }
        .sub-title { text-align: center; font-size: 18px; color: #455A64; margin-bottom: 30px; }
        .section-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin-top: 20px; }
        .insights-output { background-color: #E1F5FE; padding: 20px; border-left: 5px solid #0288D1; border-radius: 8px; font-family: 'Arial', sans-serif; }
    </style>
    <h1 class='main-title'>📈 smart Market Gap Analyzer</h1>
    <p class='sub-title'>Uncover opportunities and insights tailored to your industry!</p>
""", unsafe_allow_html=True)

# Sidebar inputs
st.sidebar.markdown("<h3 style='color:#0288D1'>⚙️ Analysis Settings</h3>", unsafe_allow_html=True)
industry = st.sidebar.text_input("Industry Name", "e.g., Healthcare")
region = st.sidebar.text_input("Region (Optional)", "e.g., India")
business_size = st.sidebar.selectbox("Business Size Focus", ["Small (Startups/SMEs)", "Medium (Regional Players)", "Large (Enterprises)"])
analysis_depth = st.sidebar.select_slider("Analysis Depth", options=["Basic", "Moderate", "Detailed"], value="Detailed")
analyze_button = st.sidebar.button("Analyze Market")

# Prompt generator
def generate_market_analysis(industry, region, business_size, depth):
    region_text = f" in {region}" if region else " globally"
    depth_map = {
        "Basic": "short and concise",
        "Moderate": "balanced with key details and some market statistics",
        "Detailed": "extensive with tabular data, detailed market structure, SWOT analysis, customer personas, TAM/SAM/SOM, competitor analysis, and numerical insights"
    }

    prompt = f"""
    You are a professional market analyst. Perform a detailed market gap analysis for the '{industry}' industry{region_text} for {business_size.lower()} businesses.

    Include:
    1. Market Overview
    2. TAM/SAM/SOM Table:
       | Metric | Value | Description |
    3. Market Gap should be explain in 1000 words according to {business_size }
    4. Suggested Product/Service
    5. Customer Persona
    6. Competitor Weakness Table:
       | Competitor | Weakness | How We Can Exploit |
    7. Revenue Projection Table:
       | Year | Est. Users | ARPU | Revenue |
    8. SWOT Analysis
    9. Growth Forecast

    Use markdown formatting for all tables.
    Format all monetary values with $ or ₹ based on region.
    Depth: {depth_map[depth]}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=16000,
            temperature=0.4
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"⚠️ API Error: {str(e)}")
        return None

# Extract table from markdown
def extract_table(markdown_text, keyword):
    pattern = rf"{keyword}.*?\n(\|.*?\|(?:\n\|.*?\|)+)"
    match = re.search(pattern, markdown_text, re.DOTALL | re.IGNORECASE)
    if not match:
        return None

    table_md = match.group(1)
    lines = [line.strip() for line in table_md.strip().split("\n") if line.strip().startswith("|")]
    if len(lines) < 2:
        return None

    headers = [h.strip() for h in lines[0].split("|")[1:-1]]
    rows = []
    for row_line in lines[2:]:  # Skip header and separator
        row = [cell.strip() for cell in row_line.split("|")[1:-1]]
        if len(row) == len(headers):
            rows.append(row)

    df = pd.DataFrame(rows, columns=headers)
    return df

# Extract section block (like SWOT, Persona etc.)
def extract_section(markdown_text, section_title):
    pattern = rf"{section_title}\s*[:\-]?\s*(.*?)(?=\n\n|\Z)"
    match = re.search(pattern, markdown_text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else None

# Main app logic
if analyze_button:
    if industry:
        analysis = generate_market_analysis(industry, region, business_size, analysis_depth)
        if analysis:
            st.markdown(f"<div class='section-box'><div class='insights-output'>", unsafe_allow_html=True)
            st.markdown(analysis, unsafe_allow_html=True)
            st.markdown("</div></div>", unsafe_allow_html=True)

           

# Footer
st.sidebar.markdown("<p style='text-align:center; color:gray;'>🔮 Powered by Groq</p>", unsafe_allow_html=True)
