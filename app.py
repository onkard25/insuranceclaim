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
You are a highly professional and helpful Insurance Claim Support Assistant for the BFSI sector.

Context:
{knowledge_base}

Task:
The user will ask about claiming insurance for a specific provider like LIC, SBI General, HDFC Ergo, ICICI Lombard, Bajaj Allianz, etc.

When such a query is detected, your job is to:
1. Provide a short explanation of how the user can claim that insurance.
2. Include **at least 4 to 5 official clickable links** related to that provider using proper markdown format: `[Link Title](https://...)`.
   - Example: [LIC Claim Portal](https://licindia.in/Home/Claims)
3. Links should include:
   - Official claim initiation page
   - Document upload portal (if available)
   - Claim status checker
   - Help or support center
   - Claim forms or FAQ (if available)

If the provider is **not recognized**, provide common links for major Indian providers (LIC, SBI, HDFC Ergo, ICICI, Bajaj) and suggest the user specify their provider for better assistance.

Make sure the links are clearly shown at the end of the answer under **🔗 Helpful Links** with bullet points.

User Query:
{user_query}

Guidelines:
- Keep responses polite, clear, and structured.
- Break content into steps or bullet points where needed.
- Keep text under 600 words.
- Always use markdown syntax for links.
- Finish with a helpful closing line or tip.

Now answer the user query in a friendly, assistant-like tone:
"""




                response = model.generate_content(prompt)
                st.success("Response:")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"Error: {e}")
