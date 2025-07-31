# 🧠 Investment Elicitation Profiling Assistant

This project is an **AI-powered conversational assistant** that guides users step-by-step (elicitation) to build their **investment profile** through a friendly dialogue. It uses **LangChain**, **OpenAI**, **FastAPI**, and **WebSocket** for a real-time interactive experience.

---

## 🚀 Features

- Conversational investment profiling via WebSocket
- Guided 4-step elicitation:
  1. **Purpose** – Why you're investing
  2. **Timeline** – How long you plan to invest
  3. **Risk Tolerance** – How much risk you can handle
  4. **Investment Entry** – How and how much you plan to invest
- Structured and validated input via Pydantic
- Real-time messaging powered by LangChain + OpenAI
- WebSocket support for frontend integration

---

## 📦 Tech Stack

- **Python**
- **FastAPI** – REST + WebSocket API
- **LangChain** – agent logic and prompt orchestration
- **OpenAI GPT** – language understanding and generation
- **Pydantic** – validation and type safety
- **Loguru** – logging
- **dotenv** – environment management
- **FastMCP** – multi-step conversational pipeline manager

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/investment-assistant.git
cd investment-assistant
```

## 2. Install Dependencies

```bash
uv sync
```

## 3. Add .env File
Create a .env file with your OpenAI API key:
```
OPENAI_API_KEY=your-openai-api-key
```

## 4. Run the servers
```
uv run python client.py
uv run python mcp_server.py
```
