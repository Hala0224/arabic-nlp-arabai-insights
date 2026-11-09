# ArabAI Insights — Arabic NLP Pipeline

Final project for the **Natural Language Processing** course at Al Hussein Technical University (HTU), 2026.

An end-to-end Arabic NLP pipeline built on the **AAFAQ** dataset (5,009 Arabic question–answer pairs across 17 categories), covering preprocessing, question answering, text classification and machine translation, plus a small web interface.

## Notebooks

| # | Notebook | What it does |
|---|----------|--------------|
| 1 | [Preprocessing](notebooks/1_Preprocessing.ipynb) | Arabic text cleaning: tashkeel & tatweel removal, NLTK stop-words, Alef normalisation, ISRI stemming. Produces `data/AAFAQ_Preprocessed.csv`. |
| 2 | [Question Answering](notebooks/2_QuestionAnswering.ipynb) | Compares TF-IDF, Word2Vec and AraBERT embeddings with RNN, LSTM, GRU and BiGRU models; a retrieval-based QA system; and generative models (AraGPT2, mT5, Qwen). |
| 3 | [Classification](notebooks/3_Classification.ipynb) | TF-IDF n-gram features with Naive Bayes, Linear SVM, Logistic Regression and Random Forest, plus BERT fine-tuning. Best: **LinearSVC – 73.5 % accuracy**. |
| 4 | [Machine Translation](notebooks/4_MachineTranslation.ipynb) | Arabic → English translation through the OpenRouter API (GPT-3.5-turbo) with category-aware prompts. |

## Web interface

[`app/NLP_Interface.py`](app/NLP_Interface.py) is a Streamlit app for asking questions in Arabic.

```bash
pip install streamlit requests
streamlit run app/NLP_Interface.py
```

Notebook 4 and the app call the OpenRouter API. Replace `YOUR_OPENROUTER_API_KEY` with your own key before running — never commit a real key.

## Presentation

[NLP-Presentation.pdf](NLP-Presentation.pdf) — project overview slides.

## Tech

Python · PyTorch · Hugging Face Transformers (AraBERT, AraGPT2, mT5, Qwen) · scikit-learn · NLTK · imbalanced-learn · Streamlit

---
**Author:** Hala Nazzal
