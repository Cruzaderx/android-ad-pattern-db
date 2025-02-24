#!/usr/bin/env python3
import json
import os
import re
from typing import Dict, List, Any


class VulnerabilityDatabaseValidator:
    def __init__(self, db_root: str):
        self.db_root = db_root
        self.index_file = os.path.join(db_root, "vulnerability_index.json")
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate_all(self) -> bool:
        """Validate entire vulnerability database"""
        try:
            # Validate index file
            if not self.validate_index():
                return False

            # Load index
            with open(self.index_file, "r") as f:
                index = json.load(f)

            # Validate each category file
            for category in index["categories"]:
                if not self.validate_category_file(category):
                    return False

            # Validate cross-references
            if not self.validate_cross_references(index):
                return False

            return len(self.errors) == 0
        except Exception as e:
            self.errors.append(f"Validation failed: {str(e)}")
            return False

    def validate_index(self) -> bool:
        """Validate index file structure and content"""
        try:
            with open(self.index_file, "r") as f:
                index = json.load(f)

            required_fields = ["metadata", "categories", "schema"]
            for field in required_fields:
                if field not in index:
                    self.errors.append(f"Index missing required field: {field}")
                    return False

            # Validate metadata
            metadata_fields = [
                "version",
                "last_updated",
                "total_categories",
                "total_vulnerabilities",
            ]
            for field in metadata_fields:
                if field not in index["metadata"]:
                    self.errors.append(f"Metadata missing required field: {field}")
                    return False

            # Validate categories
            if not isinstance(index["categories"], list):
                self.errors.append("Categories must be a list")
                return False

            for category in index["categories"]:
                if not self.validate_category_entry(category):
                    return False

            return True
        except Exception as e:
            self.errors.append(f"Index validation failed: {str(e)}")
            return False

    def validate_category_entry(self, category: Dict[str, Any]) -> bool:
        """Validate a category entry in the index"""
        required_fields = [
            "name",
            "file",
            "description",
            "vulnerability_count",
            "vulnerability_types",
        ]
        for field in required_fields:
            if field not in category:
                self.errors.append(f"Category missing required field: {field}")
                return False

        # Validate file path
        file_path = os.path.join(self.db_root, category["file"])
        if not os.path.exists(file_path):
            self.errors.append(f"Category file not found: {file_path}")
            return False

        return True

    def validate_category_file(self, category: Dict[str, Any]) -> bool:
        """Validate a category's vulnerability file"""
        try:
            file_path = os.path.join(self.db_root, category["file"])
            with open(file_path, "r") as f:
                vulns = json.load(f)

            # Validate basic structure
            if "metadata" not in vulns or "vulnerabilities" not in vulns:
                self.errors.append(f"Invalid structure in {category['file']}")
                return False

            # Validate each vulnerability
            for vuln in vulns["vulnerabilities"]:
                if not self.validate_vulnerability(vuln, category["name"]):
                    return False

            # Validate count matches
            if len(vulns["vulnerabilities"]) != category["vulnerability_count"]:
                self.warnings.append(
                    f"Vulnerability count mismatch in {category['name']}"
                )

            return True
        except Exception as e:
            self.errors.append(f"Category file validation failed: {str(e)}")
            return False

    def validate_vulnerability(self, vuln: Dict[str, Any], category: str) -> bool:
        """Validate a single vulnerability entry"""
        required_fields = [
            "id",
            "name",
            "description",
            "severity",
            "detection",
            "exploit",
            "affected_components",
            "tags",
        ]
        for field in required_fields:
            if field not in vuln:
                self.errors.append(
                    f"Vulnerability in {category} missing field: {field}"
                )
                return False

        # Validate detection section
        detection_fields = [
            "pattern",
            "method",
            "indicators",
            "accuracy_improvements",
            "confidence_score",
        ]
        for field in detection_fields:
            if field not in vuln["detection"]:
                self.errors.append(f"Detection in {vuln['id']} missing field: {field}")
                return False

        # Validate regex patterns
        for pattern in vuln["detection"]["pattern"]:
            try:
                re.compile(pattern)
            except re.error:
                self.errors.append(f"Invalid regex pattern in {vuln['id']}: {pattern}")
                return False

        return True

    def validate_cross_references(self, index: Dict[str, Any]) -> bool:
        """Validate cross-references and consistency"""
        try:
            # Check for duplicate IDs
            all_ids = set()
            for category in index["categories"]:
                file_path = os.path.join(self.db_root, category["file"])
                with open(file_path, "r") as f:
                    vulns = json.load(f)
                    for vuln in vulns["vulnerabilities"]:
                        if vuln["id"] in all_ids:
                            self.errors.append(
                                f"Duplicate vulnerability ID: {vuln['id']}"
                            )
                            return False
                        all_ids.add(vuln["id"])

            # Validate total counts
            total_vulns = sum(cat["vulnerability_count"] for cat in index["categories"])
            if total_vulns != index["metadata"]["total_vulnerabilities"]:
                self.warnings.append("Total vulnerability count mismatch")

            return True
        except Exception as e:
            self.errors.append(f"Cross-reference validation failed: {str(e)}")
            return False

    def print_results(self):
        """Print validation results"""
        if self.errors:
            print("\nErrors:")
            for error in self.errors:
                print(f"❌ {error}")

        if self.warnings:
            print("\nWarnings:")
            for warning in self.warnings:
                print(f"⚠️ {warning}")

        if not self.errors and not self.warnings:
            print("✅ Validation successful - no issues found")


def main():
    # Get the directory containing this script
    db_root = os.path.dirname(os.path.abspath(__file__))

    validator = VulnerabilityDatabaseValidator(db_root)
    is_valid = validator.validate_all()
    validator.print_results()

    exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
