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
You are a highly knowledgeable and helpful Insurance Claims Assistant specializing in the BFSI sector.

Context:
{knowledge_base}

The user may mention popular Indian insurance providers like LIC, SBI General, HDFC Ergo, ICICI Lombard, Bajaj Allianz, etc.

If the user's query is about claiming insurance from a specific company, include **at least 5 helpful links** to official claim portals, documentation upload pages, or claim status checkers. These links should be clickable and relevant to the provider mentioned.

User Query:
{user_query}

Guidelines for your response:
- Provide detailed and accurate information.
- Break your answer into bullet points or numbered steps where applicable.
- Always try to include helpful external links when the user mentions a specific provider.
- If the query is general or vague, suggest clarification and still provide common claim resource links.
- Use markdown-style `[text](url)` formatting for links so that Streamlit renders them properly.
- Use simple, friendly language.
- End the response with a polite tip or closing sentence.
- Keep the response under 600 words unless absolutely necessary.

Now respond to the user's question:
"""



                response = model.generate_content(prompt)
                st.success("Response:")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"Error: {e}")
