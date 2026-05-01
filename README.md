# Gemma 4 Beginner Tutor (Local-First Streamlit App)

A beginner-friendly AI tutor app built with **Streamlit + Ollama + Gemma 4**.

This project is designed for hackathon/demo use and focuses on:

- Local-first AI usage
- Simple setup for beginners
- Clear impact narrative (works in low-connectivity settings)
- Safe fallback messages when Ollama/model is not ready

---

## Screenshot gallery

### Home screen

![Home screen](assets/screenshots/app-home.png)

### Live interaction view

![Live interaction](assets/screenshots/app-chat-processing.png)

---

## Kaggle judges section 

### 1) Problem statement

Many students in low-connectivity environments do not have stable access to
online tutoring tools. This limits personalized support and self-paced
learning.

### 2) Proposed solution

**Gemma 4 Beginner Tutor** is a local-first educational assistant that runs on
device through Ollama. It gives beginner-friendly explanations, examples, and
practice prompts without requiring cloud API keys.

### 3) Why Gemma 4

- Strong local inference capability for practical offline usage
- Good quality responses for beginner education prompts
- Easy integration with local app workflows through Ollama runtime

### 4) Real-world impact

- Supports students where internet is unstable or expensive
- Preserves privacy through local processing
- Reduces setup complexity for schools and small learning centers

### 5) Technical architecture

- **Frontend/UI:** Streamlit web app
- **Inference layer:** Ollama HTTP API on `127.0.0.1:11434`
- **Model:** `gemma4:latest`
- **App behavior:**
  - Maintains chat history in Streamlit session state
  - Provides clear setup fallback when Ollama is unavailable
  - Allows chat export for revision and teacher review

### 6) Functional status

- Working local app with browser-accessible UI
- Model status detection implemented
- Chat flow and export flow implemented
- Beginner-safe error handling implemented

### 7) Demo checklist for judges

- Show app launch in under 30 seconds
- Ask one real educational question
- Show response quality and beginner formatting
- Highlight local-first privacy and connectivity benefits
- Export chat history to prove practical classroom utility

### 8) Suggested evaluation plan

- **Latency:** first response time vs subsequent response time
- **Usability:** time for a new user to ask first question
- **Learning quality:** short rubric (clarity, correctness, actionability)
- **Reliability:** behavior when Ollama is down or model is missing

### 9) What is included in this repository

- Complete runnable source code
- Setup and troubleshooting documentation
- Launch script for Windows
- Real application screenshots for verification

---

## What this app does

- Runs a chat-style tutor UI in your browser
- Uses `gemma4` model through Ollama API (`http://127.0.0.1:11434`)
- Stores conversation in Streamlit session
- Lets user clear chat
- Lets user download chat history as a text file
- Shows setup guidance directly in UI when Ollama is unavailable

---

## Tech stack

- Python 3.14+
- Streamlit
- Ollama
- Gemma 4 model (`gemma4:latest`)

---

## Project structure

```text
gemma_app/
├── assets/
│   └── screenshots/
│       ├── app-home.png
│       └── app-chat-processing.png
├── app.py
├── requirements.txt
├── RUN_ME.ps1
├── .gitignore
├── LICENSE
└── README.md
```

---

## Prerequisites

1. **Python installed**
   - Verify:
     ```powershell
     python --version
     ```

2. **Ollama installed**
   - Verify:
     ```powershell
     ollama --version
     ```

3. **Gemma model downloaded**
   - Pull model:
     ```powershell
     ollama pull gemma4
     ```
   - Check model list:
     ```powershell
     ollama list
     ```

> Note: `gemma4` download is large (~9.6 GB), so first-time setup may take a while.

---

## Installation

From project folder:

```powershell
cd "C:\Users\DELL PRECision 7550\gemma_app"
python -m pip install -r requirements.txt
```

---

## Run the app

### Option A (recommended)

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\DELL PRECision 7550\gemma_app\RUN_ME.ps1"
```

### Option B (manual)

```powershell
cd "C:\Users\DELL PRECision 7550\gemma_app"
python -m streamlit run app.py
```

Then open:

- [http://localhost:8501](http://localhost:8501)

---

## How to use

1. Open the app in browser
2. Keep model name as `gemma4` (or change if your Ollama tag differs)
3. Ask short study questions (for faster responses)
4. Use **Clear Chat** to reset
5. Use **Download Chat** to export conversation

---

## Troubleshooting

### 1) Browser shows `ERR_CONNECTION_REFUSED`

This means Streamlit is not running yet.

Run:

```powershell
cd "C:\Users\DELL PRECision 7550\gemma_app"
python -m streamlit run app.py
```

### 2) App says Ollama is not ready

Start Ollama service and ensure model exists:

```powershell
ollama serve
ollama list
```

If `gemma4` is missing:

```powershell
ollama pull gemma4
```

### 3) `streamlit` command not found

Use module style:

```powershell
python -m streamlit run app.py
```

### 4) First response is very slow

Normal behavior: first response loads model into memory.
Next responses are faster.

### 5) Port 8501 already in use

Use another port:

```powershell
python -m streamlit run app.py --server.port 8502
```

---

## Hackathon submission notes

This app supports a strong beginner impact story:

- **Problem**: limited internet and access to educational support
- **Solution**: local-first tutoring assistant
- **Why Gemma 4**: capable local model with meaningful offline utility
- **Demo value**: real working application, not just slides

For a stronger submission, add:

- Sample lesson plans
- Multilingual prompts
- Performance metrics (latency and quality examples)
- A short user test with classmates/teachers

---

## Security and privacy notes

- Prompts are sent to local Ollama endpoint (`127.0.0.1`) by default
- No cloud API key is required in current version
- Chat is stored in session state while app is open
- Exported chat file is local to user machine

---

## Future improvements

- Add voice input/output
- Add language selector
- Add education-grade prompt templates
- Add PDF/image study material support
- Add local usage analytics dashboard

---

## License

This project is licensed under the MIT License. See `LICENSE`.
