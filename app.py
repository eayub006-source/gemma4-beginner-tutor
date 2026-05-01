import json
import urllib.error
import urllib.request

import streamlit as st

st.set_page_config(page_title="Gemma 4 Beginner Tutor", page_icon="🎓")

OLLAMA_BASE = "http://127.0.0.1:11434"
OLLAMA_CHAT_URL = f"{OLLAMA_BASE}/api/chat"
DEFAULT_MODEL = "gemma4"


def ollama_installed_and_running() -> tuple[bool, str]:
    try:
        with urllib.request.urlopen(
            f"{OLLAMA_BASE}/api/tags", timeout=3
        ) as response:
            if response.status == 200:
                return True, ""
            return False, f"Ollama returned status {response.status}"
    except urllib.error.URLError:
        return False, "Cannot connect to Ollama on port 11434."
    except (TimeoutError, OSError, ValueError) as exc:
        return False, str(exc)


def ask_model(messages: list[dict[str, str]], selected_model: str) -> str:
    payload = {
        "model": selected_model,
        "messages": messages,
        "stream": False,
    }
    request = urllib.request.Request(
        OLLAMA_CHAT_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=180) as response:
        body = response.read().decode("utf-8")
        data = json.loads(body)
        return data["message"]["content"]


st.title("🎓 Gemma 4 Beginner Tutor")
st.caption("Local-first learning helper for your hackathon demo")

st.info(
    "Tip: Keep this app open and ask short questions for faster replies. "
    "Example: 'Teach me loops in Python with one easy example.'"
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly tutor for beginners. "
                "Use simple words, short examples, and numbered steps. "
                "End with one practice question."
            ),
        }
    ]

model_name = st.text_input("Model name", value=DEFAULT_MODEL)

ok, reason = ollama_installed_and_running()
if not ok:
    st.error("Ollama is not ready yet.")
    st.code(
        "1) Install Ollama\n"
        "2) Run: ollama pull gemma4\n"
        "3) Run: ollama serve"
    )
    st.caption(f"Details: {reason}")
else:
    st.success("Ollama is running.")

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask your study question...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if not ok:
                reply = (
                    "I cannot reach Ollama yet. "
                    "Please finish the 3 setup steps shown above."
                )
            else:
                try:
                    reply = ask_model(st.session_state.messages, model_name.strip())
                except (
                    TimeoutError,
                    urllib.error.URLError,
                    urllib.error.HTTPError,
                    json.JSONDecodeError,
                    KeyError,
                ) as exc:
                    reply = (
                        "I could not get a reply from the model. "
                        "Check model name and make sure it is downloaded.\n\n"
                        f"Error: {exc}"
                    )
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

col1, col2 = st.columns(2)
with col1:
    if st.button("Clear Chat"):
        st.session_state.messages = [st.session_state.messages[0]]
        st.rerun()

with col2:
    history = "\n\n".join(
        f"{m['role'].upper()}: {m['content']}"
        for m in st.session_state.messages
        if m["role"] != "system"
    )
    st.download_button(
        "Download Chat",
        data=history if history else "No messages yet.",
        file_name="chat_history.txt",
        mime="text/plain",
    )
