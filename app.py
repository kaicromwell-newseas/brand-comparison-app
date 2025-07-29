import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


st.set_page_config(page_title="Brand Comparison Generator", layout="wide")
st.title("🔍 Brand Comparison Article Generator")

# ---- FILE UPLOAD ----
uploaded_file = st.file_uploader("Upload CSV of Brand Pairs", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("✅ Loaded brand pairs:", df.shape[0], "rows")

    # Show preview
    with st.expander("Preview CSV"):
        st.dataframe(df.head())

    # ---- SCRAPER FUNCTION ----
    def scrape_summary(url):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            html = requests.get(url, headers=headers, timeout=10).text
            soup = BeautifulSoup(html, "html.parser")
            paragraphs = soup.find_all("p")
            text = " ".join(p.text for p in paragraphs[:8])
            return text.strip()
        except:
            return ""

    # ---- PROMPT FUNCTION ----
def generate_comparison(a_name, a_summary, b_name, b_summary):
    prompt = f"""Write a comparison article titled: "{a_name} vs. {b_name}".

Structure it like this:
1. Overview of {a_name}
2. Overview of {b_name}
3. Feature Comparison (bullets)
4. Pricing Differences
5. Pros & Cons
6. Who Each Is Best For
7. Final Verdict (gently favor {a_name})

Use clear, friendly tone. Here's the context:

{a_name} summary:
{a_summary}

{b_name} summary:
{b_summary}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

    # ---- ARTICLE GENERATION LOOP ----
    st.subheader("📝 Generated Articles")

    for index, row in df.iterrows():
        st.markdown(f"### {row['brand_a_name']} vs. {row['brand_b_name']}")

        a_summary = scrape_summary(row['brand_a_url'])
        b_summary = scrape_summary(row['brand_b_url'])

        try:
            article = generate_comparison(row['brand_a_name'], a_summary, row['brand_b_name'], b_summary)
        except Exception as e:
            article = f"⚠️ Error generating article for {row['brand_a_name']} vs {row['brand_b_name']}: {e}"

        st.markdown(article)
        st.markdown("---")

    # ---- PROCESS ALL ROWS ----
    results = []
with st.spinner("Generating articles... this may take a minute."):
    for idx, row in df.iterrows():
        a_summary = scrape_summary(row['brand_a_url'])
        b_summary = scrape_summary(row['brand_b_url'])
        try:
            article = generate_comparison(
                row['brand_a_name'],
                a_summary,
                row['brand_b_name'],
                b_summary
            )
        except Exception as e:
            article = f"⚠️ Error generating article fo {row['brand_a_name']} vs {row['brand_b_name']}: {str(e)}"

        results.append({
            "title": f"{row['brand_a_name']} vs. {row['brand_b_name']}",
            "content": article
        })

# Show results for debugging
st.write("Generated results:", results)


    st.success("✅ Done! Scroll down to see the results.")

    # ---- DISPLAY RESULTS ----
    for res in results:
        with st.expander(res["title"]):
            st.markdown(res["content"])
