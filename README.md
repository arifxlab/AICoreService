# AI Core Service

A production-ready AI backend service built with **FastAPI** that provides a unified interface for Large Language Models (LLMs) through a gateway architecture. The service supports tool execution, structured outputs, input/output guardrails, metrics, and provider abstraction, making it suitable for building scalable AI-powered applications.

---

## Features

- AI Gateway architecture
- OpenRouter provider integration
- Provider abstraction layer
- Tool calling framework
- Calculator tool
- Date & Time tool
- Structured JSON outputs
- Input validation guardrails
- Output validation guardrails
- Request logging with Structlog
- Metrics collection
- Health monitoring endpoint
- Exception handling
- FastAPI automatic API documentation
- Modular architecture
- Fully asynchronous implementation

---

## Tech Stack

- Python 3.11
- FastAPI
- Pydantic v2
- HTTPX
- OpenRouter
- Structlog
- Uvicorn

Development Tools

- Ruff
- Black
- MyPy
- Pytest

---

## Project Structure

```
app/
├── ai/
│   ├── gateway/
│   ├── providers/
│   ├── guardrails/
│   ├── schemas/
│   ├── services/
│   └── tools/
├── api/
│   └── v1/
├── core/
└── main.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ai-core-service.git
cd ai-core-service
```

Create a virtual environment

```bash
uv venv
```

Activate the environment

Windows

```powershell
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file.

Example:

```env
APP_NAME=AI Core Service
APP_VERSION=1.0.0
DEBUG=True
ENVIRONMENT=development

OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=google/gemma-3-27b-it
OPENROUTER_TEMPERATURE=0
OPENROUTER_MAX_TOKENS=300
```

---

## Running the Application

```bash
uv run uvicorn app.main:app --reload
```

The application will be available at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

OpenAPI Specification

```
http://127.0.0.1:8000/openapi.json
```

---

## API Endpoints

### Root

```
GET /
```

Returns service information.

---

### Health

```
GET /health
```

Returns application health status.

---

### Metrics

```
GET /metrics
```

Returns runtime metrics including:

- Total requests
- Successful requests
- Failed requests
- Tool calls
- Provider calls
- Average provider latency

---

### Chat

```
POST /api/v1/chat
```

Example request

```json
{
  "system_prompt": "",
  "user_prompt": "Explain FastAPI",
  "model": "google/gemma-3-27b-it",
  "temperature": 0,
  "max_tokens": 300
}
```

---

## Built-in Tools

### Calculator

```
calc: 25 * 14
```

Example response

```
350
```

---

### Date & Time

```
What is the current time?
```

Returns the current system date and time.

---

## Structured Output

The service supports structured JSON generation.

Example

```
summarize: FastAPI is a modern Python framework...
```

Response

```json
{
  "summary": "...",
  "keywords": [
    "...",
    "..."
  ]
}
```

---

## Architecture

```
Client
   │
   ▼
FastAPI API
   │
   ▼
AI Service
   │
   ├──────────────► Guardrails
   │
   ├──────────────► Tool Registry
   │                     │
   │                     ├── Calculator
   │                     └── DateTime
   │
   ▼
Gateway
   │
   ▼
OpenRouter Provider
   │
   ▼
Large Language Model
```

---

## Development

Format code

```bash
black .
```

Lint

```bash
ruff check .
```

Type checking

```bash
mypy .
```

Run tests

```bash
pytest
```

---

## Future Improvements

- Streaming responses
- Multi-provider routing
- Conversation memory
- Authentication
- Rate limiting
- Redis caching
- Database persistence
- Additional AI tools
- OpenTelemetry tracing
- Docker deployment

---

## Author

**Arif Khan**

Backend AI Engineer

---

## License

This project is released under the MIT License.