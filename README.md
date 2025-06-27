# Insurance Claim Assistant GenAI Agent (Streamlit Version)

## About
This is an Insurance Claim Assistant agent for the BFSI sector built using Python and Streamlit.  
It uses OpenAI's GPT model to answer user queries about insurance claims.

## Features
- Simple Streamlit Web UI
- OpenAI GPT-based responses
- Focused on claim filing, document requirements, status, and more

## Local Setup Instructions

### 1. Clone / Download the project
```
git clone [repo link or download ZIP]
cd insurance_claim_agent_streamlit
```

### 2. Install required packages
```
pip install -r requirements.txt
```

### 3. Add your OpenAI API key
- Create a `.env` file with this content:

```
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
```

### 4. Run the app
```
streamlit run app.py
```

### 5. Open your browser
Go to:  
```
http://localhost:8501
```

## Hosting (After Local Testing)
- Streamlit Cloud
- Render.com
- Railway.app

## License
MIT