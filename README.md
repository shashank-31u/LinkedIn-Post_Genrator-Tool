💼 LinkedIn Post Generator

A GenAI-powered tool to analyze a LinkedIn influencer's past posts and help them generate future content in the same writing style.

---

## 🚀 Overview

The **LinkedIn Post Generator** enables influencers like Mohan to:

- Upload their past LinkedIn posts
- Extract key characteristics such as **topic**, **language**, and **length**
- Select desired content setting
- Automatically generate a new post that matches their **style and tone**

---

## 🧠 How It Works

### Stage 1: Analyze Past Posts

- Extracts features like:
  - **Topics** (e.g., AI, leadership, marketing)
  - **Language** (English, Hindi, etc.)
  - **Post Length** (short, medium, Long)

### Stage 2: Generate New Post

- Uses selected features (topic, preferred language, length)
- Applies **few-shot learning** with similar previous posts to guide the LLM
- Generates a new, stylistically consistent post

---

## 🏗️ Architecture

```text
1. Input: Past LinkedIn posts
     ↓
2. Feature Extraction: Topic, Length, Language
     ↓
3. User Selection: Choose topic, language, length
     ↓
4. Few-shot prompt generation using similar past posts
     ↓
5. Post Generation using LLM
