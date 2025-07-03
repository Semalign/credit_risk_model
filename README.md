# 💳 CrediTrust Risk Intelligence Chatbot

An AI-powered internal tool designed to help CrediTrust Financial teams explore customer complaint data and credit risk insights across product lines like Credit Cards, Personal Loans, BNPL, Savings Accounts, and Money Transfers.

---

## 📌 Project Overview

CrediTrust receives thousands of monthly complaints from over 500,000 users across East Africa. This project builds a **Retrieval-Augmented Generation (RAG)** system to help product managers, compliance teams, and support agents explore complaint patterns in real time using natural language queries.

---

## ✅ Tasks Breakdown

### ✅ Task 1: Credit Scoring Business Understanding

This section outlines foundational credit risk concepts and modeling trade-offs, guided by Basel II and industry practice.

#### 1. Basel II and the Need for Interpretability

Basel II emphasizes the importance of internal risk models that are **transparent, auditable, and explainable**. Interpretable models like Logistic Regression with WoE are often preferred due to their alignment with regulatory requirements.

Black-box models (e.g., XGBoost) may be more accurate but face **barriers to acceptance** if they cannot provide intuitive justifications for predictions.

#### 2. Why We Need a Proxy Variable

In many datasets, we lack an explicit “default” label. A **proxy variable** (like 90-day nonpayment) must be constructed to define credit risk. This introduces the **risk of misalignment** between the proxy and true default behavior, which could lead to misleading predictions or flawed policy decisions.

To mitigate this, we must:
- Document how the proxy is created
- Validate its correlation with actual risk events
- Disclose limitations in model governance

#### 3. Trade-offs: Simple vs. Complex Models

| Model Type                  | Pros                                           | Cons                                    |
|----------------------------|------------------------------------------------|-----------------------------------------|
| Logistic Regression + WoE  | Interpretable, easy to explain and monitor     | May underperform on complex interactions |
| Gradient Boosting (e.g., XGBoost) | Highly accurate, good for non-linear patterns | Less interpretable, harder to govern     |

**In regulated financial contexts, interpretability usually takes precedence.**

> 📘 *References:*
> - [World Bank Credit Scoring Guide](https://thedocs.worldbank.org/en/doc/935891585869698451-0130022020/original/CREDITSCORINGAPPROACHESGUIDELINESFINALWEB.pdf)
> - [Basel II Primer](https://www3.stat.sinica.edu.tw/statistica/oldpdf/A28n535.pdf)
> - [HKMA Alternative Scoring](https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/alternative_credit_scoring.pdf)

---

## 🔍 Task 2: Embedding and Vector Indexing

- Cleaned complaint narratives were split into overlapping text chunks using LangChain's `RecursiveCharacterTextSplitter` (chunk size = 300, overlap = 50).
- Used `all-MiniLM-L6-v2` from SentenceTransformers to create semantic embeddings.
- Chunks and metadata were stored in a FAISS index for fast vector search.

📁 Output saved to:
