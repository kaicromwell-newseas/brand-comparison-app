import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from prompts import (
    SYSTEM_PROMPT, 
    get_introduction_prompt
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Brand Comparison Introduction Generator", layout="wide")
st.title("🔍 Brand Comparison Introduction Generator")

# ---- FILE UPLOAD ----
uploaded_file = st.file_uploader("Upload CSV of Brand Pairs", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("✅ Loaded brand pairs:", df.shape[0], "rows")

    # Show preview
    with st.expander("Preview CSV"):
        st.dataframe(df.head())

    # ---- PROMPT CUSTOMIZATION ----
    st.subheader("🎛️ Customize Introduction")
    
    temperature = st.slider("Creativity Level", 0.1, 1.0, 0.1, 0.1,
                          help="Lower = more consistent and predictable, Higher = more creative but less reliable")

    # ---- WRITE BUTTON ----
    st.subheader("🚀 Generate Articles")
    
    # ---- SCRAPER FUNCTION ----
    def scrape_summary(url):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            html = requests.get(url, headers=headers, timeout=10).text
            soup = BeautifulSoup(html, "html.parser")
            paragraphs = soup.find_all("p")
            text = " ".join(p.text for p in paragraphs[:8])
            return text.strip()
        except Exception as e:
            return f"Error scraping {url}: {e}"

    # ---- INTRODUCTION GENERATION FUNCTION ----
    def generate_introduction(a_name, a_summary, b_name, b_summary):
        """Generate only the introduction paragraph for a brand comparison article"""
        
        try:
            introduction_response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": get_introduction_prompt(a_name, a_summary, b_name, b_summary)}
                ],
                temperature=temperature,
                max_tokens=400
            )
            
            introduction = introduction_response.choices[0].message.content
            return introduction

        except Exception as e:
            raise e



    if st.button("Write Introductions", type="primary", use_container_width=True):
        # ---- GENERATE INTRODUCTIONS ----
        st.subheader("Generating introductions...")

        results = []

        for i, (_, row) in enumerate(df.iterrows()):
            try:
                # Get column names dynamically
                columns = list(row.index)
                if len(columns) >= 4:
                    brand_a_name = row[columns[0]]
                    brand_a_url = row[columns[1]]
                    brand_b_name = row[columns[2]]
                    brand_b_url = row[columns[3]]
                else:
                    st.error(f"⚠️ Row {i + 1} doesn't have enough columns. Expected at least 4 columns.")
                    continue
                
                st.write(f"🔄 Processing row {i + 1}: {brand_a_name} vs. {brand_b_name}")
                a_summary = scrape_summary(brand_a_url)
                b_summary = scrape_summary(brand_b_url)

                article = generate_introduction(
                    brand_a_name,
                    a_summary,
                    brand_b_name,
                    b_summary
                )

                results.append({
                    "a_name": brand_a_name,
                    "b_name": brand_b_name,
                    "article": article
                })
            except Exception as e:
                st.error(f"⚠️ Error generating article for row {i + 1}: {e}")
                article = f"⚠️ Error generating article for row {i + 1}"
                results.append({
                    "a_name": f"Brand A (Row {i + 1})",
                    "b_name": f"Brand B (Row {i + 1})",
                    "article": article
                })

        # ---- SHOW RESULTS ----
        st.success("✅ Done! Scroll down to see the introductions.")
        for res in results:
            st.markdown(f"## {res['a_name']} vs. {res['b_name']}")
            st.markdown(res['article'])
            st.markdown("---")
