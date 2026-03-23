🤖 Test Automation Framework

An AI-driven, multi-layered test automation framework that supports:

API Testing (pytest, Karate)
UI Testing (Playwright)
Security Testing (OWASP ZAP)
Performance Testing (k6)
AI-powered test generation & analysis
📁 Project Structure
test-automation/
│
├── ui-tests/
│   └── playwright/
│
├── api-tests/
│   ├── pytest/
│   └── karate/
│
├── security-tests/
│   └── zap/
│
├── performance-tests/
│   └── k6/
│
├── ai-tests/
│   └── test-generation/
│
├── ci/
│   └── github-actions/
│
├── reports/
│   └── allure/
│
└── .gitignore
🚀 Features
✅ AI-Driven Testing
Generate test cases from API specs
Create negative test scenarios
Analyze failures using LLMs
Self-healing test capabilities
✅ Multi-Type Testing
API – pytest, Karate
UI – Playwright
Security – OWASP ZAP
Performance – k6
✅ Observability & Reporting
Allure Reports
Test artifacts in CI
Metrics-ready for Prometheus & Grafana
✅ CI/CD Ready
GitHub Actions pipeline
Parallel test execution
Quality gates
⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/SowmyaThangarajan/test-automation.git
cd test-automation
2. Install Dependencies
Python
pip install -r requirements.txt
Node.js (UI tests)
cd ui-tests/playwright
npm install
npx playwright install
3. Set Environment Variables
export OPENAI_API_KEY=your_api_key_here
▶️ Running Tests
🔹 API Tests
cd api-tests/pytest
pytest --junitxml=api-report.xml
🔹 UI Tests
cd ui-tests/playwright
npx playwright test
🔹 Security Tests
cd security-tests/zap
# Run ZAP scan script or Docker
🔹 Performance Tests
cd performance-tests/k6
k6 run load-test.js
🔹 AI Tests
cd ai-tests/test-generation
python ai_test_framework.py
📊 Reporting
Generate Allure Report
pytest --alluredir=reports/allure
allure serve reports/allure
🤖 AI Capabilities

This framework uses AI to:

Generate test cases automatically
Detect negative and edge cases
Analyze test failures
Expand test coverage dynamically
Enable self-healing tests
🔄 CI/CD Pipeline

GitHub Actions pipeline includes:

✅ Build stage
✅ Unit tests
✅ API tests
✅ UI tests
✅ Security scans
✅ Performance tests
✅ AI-driven tests
✅ Reporting & quality gates
🔐 Security
API keys stored securely in environment variables
.gitignore prevents sensitive data leakage
No credentials stored in repo
🧠 Observability

Supports:

Test execution metrics
Failure tracking
Flaky test detection
Latency monitoring
Grafana + Prometheus integration ready
📌 Quality Gates

Pipeline fails if:

Any critical test fails
Security vulnerabilities detected
Performance thresholds exceeded
💡 Future Enhancements
Dockerized test environment
Distributed test execution
Advanced AI agents for testing
Slack/Teams notifications
Dashboard for test analytics
🤝 Contributing
Fork the repository
Create a feature branch
Commit changes
Push and create a Pull Request
📄 License

MIT License

⭐ Acknowledgements
OpenAI
Playwright
pytest
OWASP ZAP
k6
Allure Framework
