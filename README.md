# SAST FP Reducer

AI-assisted false positive triage for Static Application Security Testing (SAST).

---

## Overview

SAST tools such as Semgrep generate a large number of security findings. While these tools are effective at detecting potential vulnerabilities, they frequently produce findings that require manual investigation before developers can determine whether they are actually exploitable.

This project performs an automated first-pass triage of Semgrep findings by combining:

- Static analysis metadata
- Source code context
- Large Language Models
- Multi-model consensus

The objective is to reduce the amount of manual effort required during Application Security reviews while preserving human validation for security-critical decisions.

---

## Problem Statement

Traditional SAST workflows have several limitations:

- High false positive rates
- Time-consuming manual investigation
- Lack of exploitability analysis
- Limited contextual understanding

Security engineers often spend more time triaging findings than fixing vulnerabilities.

This project attempts to automate the initial reasoning process performed by an Application Security engineer.

---

## Features

- Parse Semgrep JSON reports
- Normalize findings into Python data models
- Extract vulnerable code context
- Generate structured prompts
- Analyze findings using multiple LLM providers
- Combine AI responses using a consensus engine
- Validate AI output
- Produce terminal reports
- Export structured JSON reports

---

## Architecture

```
                  Semgrep Report
                        │
                        ▼
                 JSON Parser
                        │
                        ▼
              Context Extraction
                        │
                        ▼
               Prompt Generation
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
  OpenRouter Provider             Groq Provider
        │                               │
        └───────────────┬───────────────┘
                        ▼
                 Consensus Engine
                        │
                        ▼
                AnalysisResult
                        │
          ┌─────────────┴──────────────┐
          ▼                            ▼
     Terminal Report             JSON Report
```

---

## Workflow

### 1. Parse Findings

Semgrep findings are loaded and converted into strongly typed Python objects.

---

### 2. Extract Context

The vulnerable lines and surrounding source code are extracted from the scanned project.

Providing surrounding code significantly improves the quality of AI reasoning compared to analyzing isolated lines.

---

### 3. Prompt Generation

Each finding is converted into a structured security prompt containing:

- Rule identifier
- Severity
- CWE metadata
- OWASP metadata
- Vulnerable code
- Surrounding source code

---

### 4. AI Analysis

The same finding is analyzed independently by multiple LLM providers.

Current providers:

- OpenRouter
- Groq

Each provider returns structured JSON.

Example:

```json
{
    "classification": "TRUE_POSITIVE",
    "confidence": 95,
    "vulnerability": "Command Injection",
    "reasoning": "...",
    "developer_action": "..."
}
```

---

### 5. Consensus

The responses are compared and merged into a single AnalysisResult.

This avoids relying on a single model and provides more consistent classifications.

---

### 6. Reporting

Results are presented through:

- Rich terminal output
- JSON export

Each finding includes:

- Classification
- Confidence
- Vulnerability type
- Source
- Sink
- Exploitability
- Recommended remediation

---

## Project Structure

```
src/
│
├── ai/
│   ├── openrouter_client.py
│   ├── groq_client.py
│   ├── consensus.py
│   └── manager.py
│
├── analyzer.py
├── parser.py
├── context.py
├── prompts.py
├── reporter.py
├── reducer.py
├── models.py
└── utils.py

tests/

examples/

reports/
```

---

## Example

```bash
python -m src.reducer \
    --scan examples/vulnerable_app \
    --report examples/semgrep_output.json \
    --output reports/report.json
```

---

## Example Output

```
Finding #1

Rule
python.flask.security.injection.subprocess-injection

Classification
TRUE_POSITIVE

Confidence
95%

Vulnerability
Command Injection

Source
request.args.get("host")

Sink
subprocess.check_output(...)

Recommended Fix

Replace shell=True.
Validate user input.
```

---

## Design Decisions

### Why multiple AI providers?

Different models often produce different security reasoning.

Using multiple providers allows findings to be evaluated independently before producing a single result.

---

### Why extract source code context?

Security findings frequently depend on surrounding code rather than the flagged line alone.

Providing additional context improves reasoning quality and reduces incorrect classifications.

---

### Why require structured JSON?

Natural language is difficult to validate programmatically.

Structured JSON enables:

- Validation
- Automation
- Report generation
- CI/CD integration

---

## Current Limitations

- Supports Semgrep reports only
- Does not perform interprocedural data-flow analysis
- Does not perform symbolic execution
- AI-generated analysis still requires human verification

---

## Future Work

- Support additional SAST tools
- SARIF export
- GitHub Actions integration
- Finding deduplication
- HTML reporting

---

## Technologies

- Python
- Semgrep
- OpenRouter API
- Groq API
- Rich
- OpenAI SDK

---

## License

MIT
