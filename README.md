# Android Vulnerability Database

A comprehensive database of Android application vulnerabilities organized by categories, designed for security scanning and analysis.

## Structure

The database is organized into category-specific JSON files:

```
android-ad-pattern-db/
├── vulnerability_index.json           # Index of all categories and schema
└── vulnerabilities/
    ├── webview/                      # WebView security issues
    ├── component/                    # Component exposure vulnerabilities
    ├── bluetooth/                    # BLE/Bluetooth vulnerabilities
    ├── nfc/                         # NFC-related vulnerabilities
    ├── storage/                     # Data storage vulnerabilities
    ├── anti_detection/              # Root/Emulator detection bypass
    └── runtime/                     # Runtime manipulation issues
```

## Vulnerability Schema

Each vulnerability entry follows this structure:

```json
{
    "id": "CATEGORY-XXX",
    "name": "Vulnerability Name",
    "description": "Detailed description",
    "severity": {
        "level": "Critical/High/Medium/Low",
        "impact": "Impact description",
        "exploitability": "Easy/Medium/Hard"
    },
    "detection": {
        "pattern": ["regex patterns"],
        "method": "static/dynamic",
        "indicators": ["what to look for"],
        "accuracy_improvements": {
            "required_conditions": ["conditions"],
            "exclusion_patterns": ["patterns"],
            "validation_steps": ["steps"],
            "context_requirements": ["requirements"]
        },
        "confidence_score": {
            "static_analysis": 0-100,
            "dynamic_analysis": 0-100,
            "manual_review": 0-100
        }
    },
    "exploit": {
        "difficulty": "Easy/Medium/Hard",
        "steps": ["exploitation steps"],
        "requirements": ["needed tools/access"],
        "verification": {
            "test_cases": ["test cases"],
            "expected_results": ["results"]
        }
    },
    "affected_components": ["components"],
    "tags": ["relevant", "tags"]
}
```

## Categories

1. **WebView Security**
   - Insecure WebView configurations
   - JavaScript interface vulnerabilities

2. **Component Security**
   - Exported component issues
   - Content provider vulnerabilities

3. **Bluetooth Security**
   - BLE authentication issues
   - MITM vulnerabilities

4. **NFC Security**
   - Tag cloning vulnerabilities
   - Relay attack issues

5. **Storage Security**
   - File permission issues
   - External storage vulnerabilities

6. **Anti-Detection Security**
   - Root detection bypass
   - Emulator detection evasion

7. **Runtime Security**
   - Dynamic code loading issues
   - Reflection abuse

## Detection Patterns

Each vulnerability includes regex patterns designed for static code analysis:

- **Pattern Types**:
  - Code patterns (Java/Kotlin)
  - XML patterns (AndroidManifest.xml)
  - Resource patterns (strings.xml, layout files)

- **Accuracy Improvements**:
  - Required conditions for vulnerability
  - Exclusion patterns to reduce false positives
  - Validation steps for confirmation
  - Context requirements

## Usage for Vulnerability Scanner

1. Parse the vulnerability_index.json to get all categories
2. For each category:
   - Load the corresponding JSON file
   - Extract detection patterns
   - Apply patterns to target code
   - Use accuracy improvements to filter results
   - Score findings based on confidence levels

## False Positive Reduction

The database includes multiple layers of validation:

1. **Required Conditions**: Must be present for vulnerability
2. **Exclusion Patterns**: Indicate secure implementations
3. **Validation Steps**: Additional checks to confirm
4. **Context Requirements**: Application context needed
5. **Confidence Scoring**: Multi-dimensional scoring system

## Confidence Scoring

Each vulnerability includes confidence scores for:

- **Static Analysis**: Pattern-based detection
- **Dynamic Analysis**: Runtime verification
- **Manual Review**: Human analysis required

Scores range from 0-100, indicating detection reliability.
