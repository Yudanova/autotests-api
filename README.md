## API Test Automation (Python, Pytest)

Automated REST API testing framework built with Python and Pytest.

### Tech stack
- Python
- Pytest
- Requests / HTTPX (HTTP clients)
- Pydantic
- JSON Schema
- FastAPI (Swagger UI)
- Allure

### What is covered
- CRUD API tests
- Request / response validation
- JSON schema validation
- Token-based authentication
- Positive & negative scenarios
- Modular test architecture (clients / fixtures / assertions)

### How to run tests
```bash
pytest -v
```

### Local API (for tests)
```bash
uvicorn main:app --reload
```

### Swagger UI
http://localhost:8000/docs

---

### Additional learning modules

This repository also includes small learning experiments:
- gRPC demo (Protocol Buffers, client/server)
- WebSocket example

They are included for learning purposes and are not part of the core API test framework.
