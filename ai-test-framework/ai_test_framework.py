import json
import requests
from utils import call_llm, safe_json_loads
from config import BASE_URL


class AITestFramework:
    def __init__(self):
        self.test_cases = []

    def load_spec(self, file_path: str):
        with open(file_path, "r") as f:
            return json.load(f)

    # 1. Generate test cases
    def generate_tests(self, spec):
        prompt = f"""
        Generate 5 positive test cases for this API:

        {json.dumps(spec)}
        """
        response = call_llm(prompt)
        self.test_cases.extend(safe_json_loads(response))

    # 2. Negative test cases
    def generate_negative_tests(self, spec):
        prompt = f"""
        Generate 5 negative test cases for this API:

        {json.dumps(spec)}
        """
        response = call_llm(prompt)
        self.test_cases.extend(safe_json_loads(response))

    # 3. Execute tests
    def run_tests(self, endpoint):
        url = BASE_URL + endpoint
        results = []

        for case in self.test_cases:
            try:
                res = requests.post(url, json=case)
                results.append({
                    "input": case,
                    "status_code": res.status_code,
                    "response": res.text
                })
            except Exception as e:
                results.append({
                    "input": case,
                    "error": str(e)
                })

        return results

    # 4. Analyze failures
    def analyze_failures(self, results):
        failures = []

        for r in results:
            if r.get("status_code") != 200:
                prompt = f"""
                Analyze this API failure and suggest fix:

                {json.dumps(r)}
                """
                analysis = call_llm(prompt)

                failures.append({
                    "failure": r,
                    "analysis": analysis
                })

        return failures

    # 5. Expand tests
    def expand_tests(self, failures):
        for f in failures:
            prompt = f"""
            Generate 3 new edge test cases based on this failure:

            {json.dumps(f)}
            """
            new_tests = safe_json_loads(call_llm(prompt))
            self.test_cases.extend(new_tests)


# ---- RUN ----
if __name__ == "__main__":
    framework = AITestFramework()

    spec = framework.load_spec("openapi_spec.json")

    endpoint = spec["endpoint"]

    print("🔹 Generating tests...")
    framework.generate_tests(spec)

    print("🔹 Generating negative tests...")
    framework.generate_negative_tests(spec)

    print("🔹 Running tests...")
    results = framework.run_tests(endpoint)

    print("🔹 Analyzing failures...")
    failures = framework.analyze_failures(results)

    print("🔹 Expanding tests...")
    framework.expand_tests(failures)

    print("\n✅ FINAL RESULTS")
    print(json.dumps(results, indent=2))

    print("\n🧠 FAILURE ANALYSIS")
    print(json.dumps(failures, indent=2))