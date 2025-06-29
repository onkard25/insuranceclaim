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
                # Enhanced Prompt for More Detailed Assistance
                prompt = f"""
You are a professional and helpful Insurance Claim Assistant specializing in the BFSI sector.

Context:
{knowledge_base}

Task:
When the user asks a question related to insurance claims, do the following:
1. Understand the intent and provide a **clear, elaborative explanation** related to their query. For example, explain steps to file a claim, required documents, or processing time.
2. If the user mentions a specific insurance provider (e.g., LIC, SBI General, HDFC Ergo, ICICI Lombard, Bajaj Allianz), then **add only the official website link** for that company.
   - Use markdown format: [Visit LIC Website](https://licindia.in)

If no known provider is detected, give a general response and recommend the user to mention the company name for specific links.

User Query:
{user_query}

Guidelines:
- Explain the answer in a structured and easy-to-follow way.
- Use bullet points or numbered lists if needed.
- Always include the provider’s **official website link** if identified.
- Keep the response polite and minimum 600 words.
- End with a friendly summary or suggestion if needed.

Now respond to the user query in a helpful and conversational tone:
"""




                response = model.generate_content(prompt)
                st.success("Response:")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"Error: {e}")
