### 💬 Streamlit LLM App with LangChain and Ollama

This Streamlit app is a simple LLM-powered chatbot built using **LangChain**, **Ollama**, and **Streamlit**. It allows users to ask questions via a web interface and get fast, natural language responses powered by a local LLM model (like `llama3` via Ollama).

#### 🔧 Features:

* Uses **LangChain's `Ollama` integration** to run local LLMs (e.g., LLaMA 3).
* Chain includes:

  * System and user prompt template
  * Local LLM inference via Ollama
  * Output parsing
* Minimal Streamlit UI for live chat interaction.
* Supports `.env` configuration for LangChain environment settings.

#### 🧠 Tech Stack:

* [LangChain](https://www.langchain.com/)
* [Ollama](https://ollama.com/)
* [Streamlit](https://streamlit.io/)
* Python + `.env` for secrets

#### 🚀 How to Run:

Make sure you have Ollama running locally and a model (e.g., `llama3`) pulled.

```bash
ollama pull llama3
streamlit run app.py
```

---

### ✅ Example GitHub Commit Message:

```
Add Streamlit LLM chatbot using LangChain and Ollama
```


