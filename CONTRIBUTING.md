# Contributing to Android Ad Pattern Database

Thank you for your interest in contributing to the Android Ad Pattern Database! This guide will help you understand how to contribute effectively.

## Types of Contributions

### 1. New Ad SDK Patterns
- Complete SDK information including activities, services, providers
- Initialization and loading patterns
- Resource patterns (layouts, drawables, strings)
- Verification data showing pattern effectiveness

### 2. Pattern Updates
- Improvements to existing patterns
- Additional components for known SDKs
- Updated initialization or loading patterns
- Bug fixes for existing patterns

### 3. Pattern Verification
- Success rate data
- APK compatibility information
- False positive/negative reports
- Performance impact data

## Contribution Process

1. Fork the Repository
   ```bash
   git clone https://github.com/[your-username]/android-ad-pattern-db
   cd android-ad-pattern-db
   ```

2. Create a Branch
   ```bash
   git checkout -b pattern-update/[sdk-name]
   ```

3. Make Changes
   - Update database.json
   - Include verification data
   - Update documentation if needed

4. Test Your Changes
   - Verify pattern accuracy
   - Test with multiple APKs
   - Check for false positives

5. Submit Pull Request
   - Detailed description of changes
   - List of tested APKs
   - Success rate data
   - Any known limitations

## Pattern Quality Requirements

### 1. Accuracy
- Minimum 90% success rate
- Less than 1% false positive rate
- Tested on at least 5 different APKs

### 2. Documentation
- Clear pattern descriptions
- Usage examples
- Source APK information
- Known limitations

### 3. Performance
- Efficient regex patterns
- Minimal resource usage
- Quick matching speed

### 4. Compatibility
- Works with obfuscated code
- Handles different SDK versions
- Compatible with various Android versions

## Pattern Format

### SDK Pattern
```json
{
    "identifier": "com.example.ads",
    "components": {
        "activities": [
            "com.example.ads.AdActivity",
            "com.example.ads.InterstitialActivity"
        ],
        "services": [
            "com.example.ads.AdService"
        ],
        "providers": [
            "com.example.ads.AdProvider"
        ],
        "permissions": [
            "com.example.ads.permission.ADS"
        ]
    },
    "code_patterns": {
        "initialization": [
            "initialize\\(.*\\)",
            "init.*Ads\\(.*\\)"
        ],
        "loading": [
            "loadAd\\(\\)",
            "showAd\\(\\)"
        ]
    },
    "verification": {
        "tested_apks": [
            "com.example.app1 v1.0",
            "com.example.app2 v2.1"
        ],
        "success_rate": 0.95,
        "false_positive_rate": 0.01
    }
}
```

### Learned Pattern
```json
{
    "pattern": ".*[Aa]d[s]?Activity$",
    "confidence": 0.85,
    "matches": [
        "com.example.CustomAdActivity",
        "com.example.InterstitialAdsActivity"
    ],
    "verification": {
        "discovered_in": "com.example.app v1.0",
        "confirmed_matches": 15
    }
}
```

## Best Practices

1. Pattern Design
   - Use precise patterns over broad matches
   - Include context in pattern descriptions
   - Document edge cases and limitations

2. Testing
   - Test with various APK sizes
   - Verify with obfuscated code
   - Check performance impact

3. Documentation
   - Clear pattern descriptions
   - Example matches
   - Known limitations
   - Version compatibility

4. Maintenance
   - Regular pattern updates
   - Deprecation notices
   - Version tracking
   - Success rate monitoring

## Review Process

1. Initial Review
   - Pattern format check
   - Documentation completeness
   - Basic validation

2. Technical Review
   - Pattern effectiveness
   - Performance impact
   - Code quality
   - Test coverage

3. Final Verification
   - Community testing
   - Success rate confirmation
   - Merge approval

## Questions?

If you have questions about contributing, please:
1. Check existing issues
2. Review pull request history
3. Create a new issue for discussion

Thank you for helping improve the Android Ad Pattern Database!
