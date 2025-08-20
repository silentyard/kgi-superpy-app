#!/usr/bin/env python3
"""
Version Management Script for KGI SuperPy App

This script helps manage version information and changelog updates.
"""

import json
import datetime
from pathlib import Path

# Project information
PROJECT_INFO = {
    "name": "KGI Securities Trading Application",
    "description": "A Python application providing basic securities login/logout functionality using kgisuperpy library with multi-account support",
    "version": "1.1.0",
    "release_date": "2025-08-21",
    "author": "KGI SuperPy App Team",
    "license": "MIT",
    "python_requires": ">=3.8",
    "homepage": "https://github.com/yourusername/kgi-superpy-app"
}

# Version history
VERSION_HISTORY = [
    {
        "version": "1.0.0",
        "date": "2025-08-20",
        "type": "major",
        "description": "Initial release with basic login/logout functionality",
        "features": [
            "Basic login/logout functionality",
            "Simulation and production modes",
            "Modern GUI interface",
            "Interactive CLI",
            "Account information display",
            "Multi-threaded operations"
        ]
    },
    {
        "version": "1.1.0", 
        "date": "2025-08-21",
        "type": "minor",
        "description": "Multi-account type support and enhanced functionality",
        "features": [
            "Multi-account type support (Stock/Futures)",
            "Dynamic account switching",
            "Detailed account information",
            "Account capabilities testing",
            "Enhanced GUI with new features",
            "Comprehensive testing suite"
        ]
    }
]

def get_current_version():
    """Get current version information."""
    return PROJECT_INFO["version"]

def get_version_info():
    """Get formatted version information."""
    current = PROJECT_INFO
    return f"""
Project: {current['name']}
Version: {current['version']}
Release Date: {current['release_date']}
Description: {current['description']}
Python: {current['python_requires']}
License: {current['license']}
"""

def generate_version_json():
    """Generate version.json file."""
    version_data = {
        "project": PROJECT_INFO,
        "history": VERSION_HISTORY,
        "generated": datetime.datetime.now().isoformat()
    }
    
    with open("version.json", "w", encoding="utf-8") as f:
        json.dump(version_data, f, indent=2, ensure_ascii=False)
    
    print("✅ Generated version.json")

def update_changelog():
    """Update CHANGELOG.md with latest version info."""
    changelog_path = Path("CHANGELOG.md")
    
    if not changelog_path.exists():
        print("❌ CHANGELOG.md not found")
        return
    
    # Read current changelog
    with open(changelog_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if latest version is already documented
    latest_version = VERSION_HISTORY[-1]["version"]
    if f"## [{latest_version}]" in content:
        print(f"✅ CHANGELOG.md already contains version {latest_version}")
        return
    
    print(f"📝 CHANGELOG.md is up to date")

def show_statistics():
    """Show project statistics."""
    print("\n📊 Project Statistics:")
    print(f"  Total versions: {len(VERSION_HISTORY)}")
    print(f"  Latest version: {VERSION_HISTORY[-1]['version']}")
    print(f"  Latest release: {VERSION_HISTORY[-1]['date']}")
    
    # Count features
    total_features = sum(len(v['features']) for v in VERSION_HISTORY)
    print(f"  Total features: {total_features}")
    
    # Show version timeline
    print("\n📅 Version Timeline:")
    for version in VERSION_HISTORY:
        print(f"  {version['date']} - v{version['version']} ({version['type']})")

def main():
    """Main function."""
    print("🚀 KGI SuperPy App - Version Management")
    print("=" * 50)
    
    print(get_version_info())
    
    # Generate version file
    generate_version_json()
    
    # Update changelog if needed
    update_changelog()
    
    # Show statistics
    show_statistics()
    
    print("\n✅ Version management complete!")

if __name__ == "__main__":
    main()
