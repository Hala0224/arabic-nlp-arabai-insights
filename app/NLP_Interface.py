import streamlit as st
import requests

# API Configuration (same as lab)
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "YOUR_OPENROUTER_API_KEY"
MODEL   = "openai/gpt-3.5-turbo"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def call_api(system_prompt, user_message):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message}
        ],
        "max_tokens": 500,
        "temperature": 0.3
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    if "choices" in result:
        return result["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: {result}"

def answer_question(q):
    return call_api("You are an Arabic-language QA assistant. Answer clearly in Arabic.", q)

def classify_question(q):
    return call_api("Classify this Arabic question into one of: Religion, Science, History, Health, Sports, Technology, Culture, Other. Reply with ONLY the category name in English.", q)

def translate_text(text, category):
    return call_api(f"You are a professional Arabic to English translator specializing in {category}. Translate accurately.", text)


st.set_page_config(page_title="Arabic NLP Interface", layout="centered")

st.markdown("""
<style>
.block-container { max-width: 600px; padding-top: 2rem; }
.box {
    border: 2px solid #888;
    border-radius: 8px;
    padding: 10px 14px;
    min-height: 48px;
    background: white;
    font-size: 1rem;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## Arabic NLP Interface")
st.markdown("---")

# Q
st.markdown("**Q**")
question = st.text_input("Question", placeholder="Enter your Arabic question here...", key="q")

# store results in session state so they persist across button clicks
if "answer" not in st.session_state:
    st.session_state.answer = ""
if "category" not in st.session_state:
    st.session_state.category = ""
if "translation" not in st.session_state:
    st.session_state.translation = ""

# Answer button
_, ans_btn_col = st.columns([5, 1])
with ans_btn_col:
    ans_clicked = st.button("Answer")

if ans_clicked:
    if not question.strip():
        st.warning("Please enter an Arabic question.")
    else:
        with st.spinner("Answering in Arabic..."):
            st.session_state.answer   = answer_question(question)
            st.session_state.category = classify_question(question)
        st.session_state.translation = ""  # clear old translation

# A
st.markdown("**A**")
st.markdown(f'<div class="box">{st.session_state.answer if st.session_state.answer else "&nbsp;"}</div>', unsafe_allow_html=True)

# Catg
st.markdown("**Catg**")
st.markdown(f'<div class="box" style="{"color:#2e7d32;font-weight:bold;" if st.session_state.category else ""}">{st.session_state.category if st.session_state.category else "&nbsp;"}</div>', unsafe_allow_html=True)

st.markdown("---")

# Eng button
_, eng_btn_col = st.columns([5, 1])
with eng_btn_col:
    eng_clicked = st.button("Eng")

if eng_clicked:
    if not st.session_state.answer:
        st.warning("Click Answer first to get the Arabic answer.")
    else:
        with st.spinner("Translating to English..."):
            combined = f"Question: {question}\nAnswer: {st.session_state.answer}"
            st.session_state.translation = translate_text(combined, st.session_state.category)

# Translation output
if st.session_state.translation:
    st.markdown(f'<div class="box" style="border-color:#1f77b4;">{st.session_state.translation}</div>', unsafe_allow_html=True)
