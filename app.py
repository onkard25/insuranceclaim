import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load Gemini API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini Flash model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Sample Knowledge Base (Mini FAQ for Priming the Model)
knowledge_base = """
BFSI Insurance Claims FAQ Knowledge Base:

1. **How to file an insurance claim?**
- Fill out the online claim form.
- Upload necessary documents like ID proof, claim form, medical reports, etc.
- Wait for claim approval within the standard timeline.

2. **What documents are required for claim filing?**
- ID Proof (Aadhar / PAN)
- Filled Claim Form
- Medical Reports (for health claims)
- FIR Copy (for accident claims)
- Policy Number Details

3. **Claim Processing Time?**
- Health Insurance: 7 to 10 working days.
- Vehicle Insurance: 5 to 7 working days.

4. **How to track claim status?**
- Visit the insurer's claim status portal.
- Enter your policy number and registered mobile number.

Respond politely. Keep your answers under 300 words. If unsure, suggest contacting the Claims Department.
"""

# Streamlit UI setup
st.set_page_config(page_title="Enhanced Insurance Claim Assistant", layout="centered")

st.title("📄 Enhanced Insurance Claim Assistant ")
st.write("Ask your Insurance Claim-related queries below:")

# User input
user_query = st.text_area("Enter your claim-related query here:")

if st.button("Get Assistance"):
    if user_query.strip() == "":
        st.warning("Please enter your query.")
    else:
        with st.spinner("Fetching response from Gemini Flash..."):
            try:
                # Enhanced Prompt
                prompt = f"""
You are a professional Insurance Claims Assistant for the BFSI sector.

Reference Knowledge Base:
{knowledge_base}

Now, answer the following customer query clearly, politely, and concisely:

User Query:
{user_query}

Guidelines:
- Stick to factual information.
- Structure the response (use bullets or numbered lists if needed).
- If the query is out of scope or unclear, respond with: "For this specific query, please contact the Insurance Claims Department."
"""

                response = model.generate_content(prompt)
                st.success("Response:")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"Error: {e}")
