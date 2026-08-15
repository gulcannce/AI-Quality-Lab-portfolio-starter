                         AI QUALITY LAB
                               |
             +-----------------+-----------------+
             |                 |                 |
         API TESTING       LLM TESTING      AGENT TESTING
             |                 |                 |
          Postman          Prompt Tests       Tool Routing
             |                 |                 |
        Python/pytest     Evaluation Engine      Agent QA
             |                 |                 |
             +-----------------+-----------------+
                               |
                       QUALITY ENGINE
                               |
          +--------------------+--------------------+
          |                    |                    |
      Accuracy            Groundedness       Hallucination
          |                    |                    |
          +--------------------+--------------------+
                               |
                       REGRESSION GATES
                               |
                        GitHub Actions


        Technology Stack
Python 3.12
pytest
requests
Postman
GitHub Actions
python-dotenv
OpenAI SDK
REST APIs


Testing Coverage
API Testing
GET / POST / PUT / DELETE
Positive testing
Negative testing
Invalid input testing
Status code validation
Response body validation
CRUD testing
Parameterized test scenarios
Environment-based configuration
Collection regression testing
API Automation
Reusable ApiClient
pytest fixtures
Parameterized tests
Environment configuration
Automated regression execution
LLM Testing
LLM provider abstraction
Fake LLM testing
LLM response validation
Prompt quality testing
Response quality scoring
AI Quality Evaluation

The framework evaluates:

Accuracy
Relevance
Completeness
Groundedness
Hallucination risk

The evaluator itself is also tested to detect false positives and false negatives.

Hallucination Testing

The framework includes tests that identify factual inconsistencies such as:
Expected:
The capital of Turkey is Ankara.

Incorrect:
The capital of Turkey is Istanbul.

RAG Testing

RAG responses are evaluated across:

Context relevance
Faithfulness
Answer correctness
AI Agent Testing

Agent behavior is tested for:

Tool selection
Tool arguments
Unknown intents
Incorrect routing prevention
AI Regression Testing

The framework compares:
Baseline Quality Score
          ↓
Current Quality Score
          ↓
Regression Gate
          ↓
PASS / FAIL


Example:
Baseline: 0.91
Current:  0.74

Regression detected ❌

CI/CD

GitHub Actions automatically runs the regression suite on:

Push
Pull Request

Pipeline:
Git Push
   ↓
GitHub Actions
   ↓
Python 3.12
   ↓
Install Dependencies
   ↓
pytest
   ↓
PASS / FAIL


External LLM integration tests are intentionally isolated from the default regression suite because they depend on:

External API availability
Network connectivity
API credits

Project Structure

AI-Quality-Lab/
│
├── .github/
│   └── workflows/
│       └── qa-regression.yml
│
├── docs/
│   ├── test-strategy.md
│   ├── QUALITY_REPORT.md
│   └── test-cases/
│
├── postman/
│   └── AI-Quality-Lab-API-Testing.postman_collection.json
│
├── src/
│   ├── agent/
│   ├── api/
│   ├── llm/
│   ├── llm_eval/
│   ├── rag/
│   └── regression/
│
├── tests/
│   ├── test_api.py
│   ├── test_llm_client.py
│   ├── test_llm_eval.py
│   ├── test_prompt_quality.py
│   ├── test_hallucination.py
│   ├── test_rag.py
│   ├── test_agent.py
│   └── test_regression.py
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .env.example

Current Test Strategy

The framework separates deterministic tests from external integration tests.

Deterministic tests

These run by default:

pytest -q

They cover:

API testing
LLM evaluation
Prompt testing
Hallucination testing
RAG testing
Agent testing
Regression testing
LLM Integration Tests

Real external LLM tests are isolated:

RUN_LLM_INTEGRATION=1 pytest -v -m integration

This prevents external API availability or credit limits from breaking the normal CI regression suite.

Engineering Principles

The project follows these principles:

1- Test behavior, not only status codes.
2- Separate API communication from test logic.
3- Use reusable automation components.
4- Keep external integrations isolated.
5- Treat AI evaluators as testable software.
6- Use regression gates to prevent AI quality degradation.
7- Prefer deterministic tests for CI reliability.

Key Learning Outcome

This project demonstrates the transition from traditional QA:
API Testing
    ↓
Test Automation
    ↓
CI/CD

to AI Quality Engineering:
LLM Testing
    ↓
Prompt Evaluation
    ↓
Hallucination Testing
    ↓
RAG Testing
    ↓
AI Agent Testing
    ↓
AI Regression Testing

Portfolio Outcome

The project is designed as a practical QA portfolio demonstrating:

API Testing + Automation + AI Quality Engineering

rather than a collection of isolated tutorials.

Author

Gülcan Çelik

QA Engineer | Test Automation | AI Quality Engineering

