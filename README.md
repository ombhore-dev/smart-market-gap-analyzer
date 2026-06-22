# Smart Market Gap Analyzer 📈 — AI-Powered Business Intelligence

> Enter any industry and get a full market gap analysis in seconds — powered by **LLaMA 3 via Groq API** with TAM/SAM/SOM tables, SWOT analysis, competitor weaknesses, and revenue projections.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-F55036?style=for-the-badge&logo=groq&logoColor=white)
![LLaMA](https://img.shields.io/badge/LLaMA_3-0467DF?style=for-the-badge&logo=meta&logoColor=white)

---

## 🔍 What It Does

Smart Market Gap Analyzer is a GenAI business intelligence tool. Enter an industry name, region, and business size — and receive a comprehensive, structured market analysis including gaps, opportunities, competitor weaknesses, and financial projections.

---

## ✨ Features

- 📊 **TAM / SAM / SOM Table** — Total, Serviceable, and Obtainable market size
- 🕳️ **Market Gap Analysis** — 1000-word deep-dive tailored to business size
- 🙋 **Customer Persona** — Target audience profile for the identified gap
- 🏢 **Competitor Weakness Table** — Competitor | Weakness | How to Exploit
- 💰 **Revenue Projection Table** — Year | Est. Users | ARPU | Revenue
- 🔄 **SWOT Analysis** — Strengths, Weaknesses, Opportunities, Threats
- 📈 **Growth Forecast** — Market trajectory and timing recommendations
- ⚙️ **Configurable Depth** — Basic / Moderate / Detailed analysis modes
- 🌍 **Region Filter** — India-specific or global analysis

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| LLM | LLaMA 3 (via Groq API) |
| Frontend | Streamlit |
| Data Display | Pandas |
| Config | python-dotenv |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/smart-market-gap-analyzer.git
cd smart-market-gap-analyzer
```

### 2. Set up environment
```bash
cp .env.example .env
# Add your Groq API key to .env
# Get a free key at: https://console.groq.com
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
smart-market-gap-analyzer/
├── app.py             # Main Streamlit app + prompt engine
├── .env.example       # API key template
├── requirements.txt
└── README.md
```

---

## 💡 Example Use Cases

| Industry | Region | Output Highlights |
|---|---|---|
| Healthcare | India | Telemedicine gaps in Tier 2/3 cities |
| EdTech | Global | Skill-based micro-credential market |
| AgriTech | India | Cold chain logistics opportunity |
| FinTech | India | Rural credit gap for SMEs |

---

## 🔑 Getting a Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to **API Keys** → **Create API Key**
4. Paste it into your `.env` file as `GROQ_API_KEY=your_key_here`

Groq's free tier gives you fast LLaMA 3 inference — no credit card required.
