# Android Ad Pattern Database

A comprehensive, community-driven database of Android advertising SDK patterns for ad detection and removal. This database contains patterns for identifying and handling various ad components across different ad networks and SDKs.

## Overview

This pattern database is designed to:
- Identify ad-related components in Android applications
- Support universal ad detection across different APKs
- Learn and adapt from successful ad removals
- Enable community contributions for pattern updates

## Database Structure

The database (`database.json`) is organized into three main sections:

### 1. Ad SDKs
Contains patterns for major advertising SDKs including:
- Facebook Ads
- Google AdMob
- Unity Ads
- AppLovin
- IronSource
- ByteDance/Pangle
- Yandex Ads
- MoPub
- InMobi
- And more...

Each SDK entry includes:
```json
{
    "identifier": "com.example.ads",
    "components": {
        "activities": ["list of activity classes"],
        "services": ["list of service classes"],
        "providers": ["list of provider classes"],
        "receivers": ["list of receiver classes"],
        "permissions": ["list of permissions"]
    },
    "resources": {
        "layouts": ["ad layout names"],
        "drawables": ["ad drawable resources"],
        "strings": ["ad-related strings"]
    },
    "code_patterns": {
        "initialization": ["SDK init patterns"],
        "loading": ["ad loading patterns"],
        "callbacks": ["callback patterns"]
    }
}
```

### 2. Learned Patterns
Contains dynamically learned patterns from successful ad removals:
```json
{
    "activities": {
        "pattern": "regex pattern",
        "confidence": 0.85,
        "matches": ["discovered matches"]
    }
}
```

### 3. Statistics
Tracks pattern effectiveness and usage:
```json
{
    "total_apks_processed": 1000,
    "successful_removals": 950,
    "pattern_matches": {
        "facebook": 156,
        "admob": 203
    }
}
```

## Usage

### Integration
```python
from db_manager import PatternDatabase, PatternLearner

# Initialize database
pattern_db = PatternDatabase()

# Get patterns for specific SDK
facebook_patterns = pattern_db.get_sdk_patterns("facebook")

# Get all learned patterns
learned_patterns = pattern_db.get_learned_patterns()

# Learn from successful removal
pattern_learner = PatternLearner(pattern_db)
pattern_learner.learn_from_removal(manifest_path, smali_dir, success_rate)
```

### Contributing Patterns

1. Fork the repository
2. Add new patterns or update existing ones
3. Submit a pull request with:
   - Description of new/updated patterns
   - Source APKs used for pattern verification
   - Success rate of pattern matches

## Pattern Quality Guidelines

Patterns should be:
1. Accurate - Minimize false positives
2. Universal - Work across different APK versions
3. Resilient - Handle code obfuscation
4. Documented - Include source and verification info

## Community Updates

The database is continuously updated through:
1. Automated pattern learning
2. Community contributions
3. Regular SDK updates
4. Success rate tracking

## License

This database is provided under the MIT License. See LICENSE file for details.

## Description

The Android Ad Pattern Database is a comprehensive collection of patterns used to identify and handle advertising components in Android applications. It serves as a central repository for the Android modding community, providing reliable patterns for ad detection and removal across various advertising networks and SDKs.

Key Features:
- Extensive coverage of major ad networks
- Machine learning-enhanced pattern detection
- Community-driven updates and improvements
- Success rate tracking and validation
- Universal compatibility across different APKs

This database is maintained by the community and continuously improved through automated pattern learning and user contributions. It aims to provide reliable, up-to-date patterns while maintaining application stability during ad removal operations.
