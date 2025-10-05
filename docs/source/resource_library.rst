Resource Library Integration
============================

Garak Resource Library Metadata
--------------------------------

The Garak project includes metadata files for integration with external resource 
libraries and platforms, such as the Aurelius Federal Platform.

Metadata Files
~~~~~~~~~~~~~~

Two metadata files are provided in the root directory of the repository:

* ``resource_library_metadata.json`` - JSON format metadata
* ``resource_library_metadata.yaml`` - YAML format metadata

These files contain comprehensive information about the Garak project including:

* Project identification and versioning
* Repository and documentation links
* Capabilities and features
* Deployment requirements
* Integration points
* Compliance information
* Contact and support details

Metadata Schema
~~~~~~~~~~~~~~~

The metadata follows a standardized schema for resource library registration:

Project Information
^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

   name: garak
   fullName: Garak - LLM Vulnerability Scanner
   version: 0.13.1.pre1
   description: Generative AI Red-teaming & Assessment Kit
   type: security_tool
   category: ai_security

Repository Information
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

   repository:
     type: git
     url: https://github.com/AureliustechandTalentSolutions/garak
     upstream: https://github.com/NVIDIA/garak

Capabilities
^^^^^^^^^^^^

The metadata includes a comprehensive list of Garak's security testing capabilities:

* Hallucination detection
* Data leakage detection
* Prompt injection testing
* Misinformation detection
* Toxicity generation testing
* Jailbreak testing
* Security vulnerability scanning

Platform Integration
~~~~~~~~~~~~~~~~~~~~

For Aurelius Federal Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The metadata is specifically structured for integration with the Aurelius Federal 
Platform's Resource Library. The platform integration section includes:

.. code-block:: yaml

   platform:
     name: Aurelius Federal Platform
     category: Resource Library
     addedDate: "2025-01-01"
     status: active

Using the Metadata
~~~~~~~~~~~~~~~~~~

Registering with a Resource Library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To register Garak with a resource library platform:

1. Locate the appropriate metadata file (JSON or YAML) in the repository root
2. Submit the metadata file to the resource library registration system
3. Follow the platform-specific registration process

Updating Metadata
^^^^^^^^^^^^^^^^^

When updating the Garak project version or capabilities:

1. Update both metadata files to maintain consistency
2. Ensure the version field matches the version in ``pyproject.toml``
3. Update the platform integration dates as appropriate

Validation
~~~~~~~~~~

The metadata files can be validated using standard JSON and YAML validators:

.. code-block:: bash

   # Validate JSON
   python -m json.tool resource_library_metadata.json > /dev/null

   # Validate YAML (requires PyYAML)
   python -c "import yaml; yaml.safe_load(open('resource_library_metadata.yaml'))"

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* `Garak Homepage <https://garak.ai>`_
* `Garak Documentation <https://docs.garak.ai>`_
* `GitHub Repository <https://github.com/NVIDIA/garak>`_
* `Discord Community <https://discord.gg/uVch4puUCs>`_
