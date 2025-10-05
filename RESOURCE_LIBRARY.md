# Resource Library Integration

This repository includes metadata files for integration with the **Aurelius Federal Platform Resource Library**.

## Metadata Files

Two metadata files are provided in the repository root:

- `resource_library_metadata.json` - JSON format metadata
- `resource_library_metadata.yaml` - YAML format metadata

## What's Included

The metadata files contain comprehensive information about the Garak project:

### Project Information
- Name and version
- Description and purpose
- License and compliance information

### Capabilities
- Hallucination detection
- Data leakage detection  
- Prompt injection testing
- Misinformation detection
- Toxicity generation testing
- Jailbreak testing
- Security vulnerability scanning

### Integration Details
- Supported APIs (OpenAI, Hugging Face, Replicate, REST)
- Input/output formats
- Deployment requirements
- Usage instructions

### Platform Information
- Platform name: Aurelius Federal Platform
- Category: Resource Library
- Status: Active

## Using the Metadata

### For Platform Administrators

To register Garak in your resource library:

1. Use either the JSON or YAML metadata file
2. Submit to your resource library registration system
3. Follow your platform's registration workflow

### For Developers

To update the metadata:

1. Edit both `resource_library_metadata.json` and `resource_library_metadata.yaml`
2. Ensure version matches `pyproject.toml`
3. Maintain consistency between JSON and YAML files
4. Run tests to validate: `pytest tests/test_resource_library.py`

## Validation

The metadata files are automatically validated by the test suite:

```bash
# Run all resource library tests
pytest tests/test_resource_library.py -v

# Validate JSON manually
python -m json.tool resource_library_metadata.json

# Validate YAML manually  
python -c "import yaml; yaml.safe_load(open('resource_library_metadata.yaml'))"
```

## Documentation

For more detailed information, see the [Resource Library Integration](docs/source/resource_library.rst) documentation.

## Contact

For questions about resource library integration:

- GitHub Issues: https://github.com/NVIDIA/garak/issues
- Discord: https://discord.gg/uVch4puUCs
- Email: docs@garak.ai
