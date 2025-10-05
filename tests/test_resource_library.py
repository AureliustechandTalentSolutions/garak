# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import yaml
from pathlib import Path

import pytest

import garak


def test_resource_library_json_exists():
    """Test that the resource library JSON metadata file exists"""
    metadata_file = Path(__file__).parent.parent / "resource_library_metadata.json"
    assert metadata_file.exists(), "resource_library_metadata.json should exist"


def test_resource_library_yaml_exists():
    """Test that the resource library YAML metadata file exists"""
    metadata_file = Path(__file__).parent.parent / "resource_library_metadata.yaml"
    assert metadata_file.exists(), "resource_library_metadata.yaml should exist"


def test_resource_library_json_valid():
    """Test that the resource library JSON metadata file is valid JSON"""
    metadata_file = Path(__file__).parent.parent / "resource_library_metadata.json"
    with open(metadata_file, "r") as f:
        metadata = json.load(f)
    
    assert isinstance(metadata, dict), "Metadata should be a dictionary"
    assert "name" in metadata, "Metadata should have a 'name' field"
    assert metadata["name"] == "garak", "Name should be 'garak'"


def test_resource_library_yaml_valid():
    """Test that the resource library YAML metadata file is valid YAML"""
    metadata_file = Path(__file__).parent.parent / "resource_library_metadata.yaml"
    with open(metadata_file, "r") as f:
        metadata = yaml.safe_load(f)
    
    assert isinstance(metadata, dict), "Metadata should be a dictionary"
    assert "name" in metadata, "Metadata should have a 'name' field"
    assert metadata["name"] == "garak", "Name should be 'garak'"


def test_resource_library_json_required_fields():
    """Test that the JSON metadata has all required fields"""
    metadata_file = Path(__file__).parent.parent / "resource_library_metadata.json"
    with open(metadata_file, "r") as f:
        metadata = json.load(f)
    
    required_fields = [
        "name",
        "version",
        "description",
        "type",
        "category",
        "repository",
        "license",
        "capabilities",
        "platform"
    ]
    
    for field in required_fields:
        assert field in metadata, f"Metadata should have a '{field}' field"


def test_resource_library_yaml_required_fields():
    """Test that the YAML metadata has all required fields"""
    metadata_file = Path(__file__).parent.parent / "resource_library_metadata.yaml"
    with open(metadata_file, "r") as f:
        metadata = yaml.safe_load(f)
    
    required_fields = [
        "name",
        "version",
        "description",
        "type",
        "category",
        "repository",
        "license",
        "capabilities",
        "platform"
    ]
    
    for field in required_fields:
        assert field in metadata, f"Metadata should have a '{field}' field"


def test_resource_library_version_matches():
    """Test that the version in metadata matches the garak version"""
    metadata_file = Path(__file__).parent.parent / "resource_library_metadata.json"
    with open(metadata_file, "r") as f:
        metadata = json.load(f)
    
    assert metadata["version"] == garak.__version__, \
        f"Metadata version should match garak version {garak.__version__}"


def test_resource_library_platform_info():
    """Test that the platform information is present and correct"""
    metadata_file = Path(__file__).parent.parent / "resource_library_metadata.json"
    with open(metadata_file, "r") as f:
        metadata = json.load(f)
    
    assert "platform" in metadata, "Metadata should have platform information"
    platform = metadata["platform"]
    
    assert "name" in platform, "Platform should have a name"
    assert platform["name"] == "Aurelius Federal Platform", \
        "Platform name should be 'Aurelius Federal Platform'"
    
    assert "category" in platform, "Platform should have a category"
    assert platform["category"] == "Resource Library", \
        "Platform category should be 'Resource Library'"
    
    assert "status" in platform, "Platform should have a status"


def test_resource_library_json_yaml_consistency():
    """Test that JSON and YAML metadata files have consistent content"""
    json_file = Path(__file__).parent.parent / "resource_library_metadata.json"
    yaml_file = Path(__file__).parent.parent / "resource_library_metadata.yaml"
    
    with open(json_file, "r") as f:
        json_metadata = json.load(f)
    
    with open(yaml_file, "r") as f:
        yaml_metadata = yaml.safe_load(f)
    
    # Check key fields match
    key_fields = ["name", "version", "description", "type", "category", "license"]
    
    for field in key_fields:
        assert json_metadata[field] == yaml_metadata[field], \
            f"Field '{field}' should match in both JSON and YAML files"
