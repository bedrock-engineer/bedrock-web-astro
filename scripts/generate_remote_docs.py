#!/usr/bin/env python3
"""Generate API documentation from published bedrock-ge package using pdoc."""

import subprocess
import sys
import tempfile
from pathlib import Path

def generate_docs_with_pdoc():
    """Install bedrock-ge in a temp venv and generate docs with pdoc."""
    
    # Create a temporary virtual environment
    with tempfile.TemporaryDirectory() as temp_dir:
        venv_path = Path(temp_dir) / "venv"
        
        print("Creating temporary virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
        
        # Get the python executable in the venv
        if sys.platform == "win32":
            python_exe = venv_path / "Scripts" / "python.exe"
            pip_exe = venv_path / "Scripts" / "pip.exe"
        else:
            python_exe = venv_path / "bin" / "python"
            pip_exe = venv_path / "bin" / "pip"
        
        print("Installing bedrock-ge and pdoc...")
        subprocess.run([str(pip_exe), "install", "bedrock-ge", "pdoc"], check=True)
        
        print("Generating documentation...")
        # Run pdoc to generate markdown
        result = subprocess.run(
            [str(python_exe), "-m", "pdoc", "bedrock_ge", "--output-format", "repr"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Create output directory
        output_dir = Path("src/content/docs/reference")
        output_dir.mkdir(exist_ok=True, parents=True)
        
        # Create index file with module info
        index_content = f"""---
title: bedrock-ge API Reference  
description: Complete API reference for the bedrock-ge Python library
---

# bedrock-ge API Reference

This is the complete API reference for the `bedrock-ge` Python library, generated from the published package.

## Module Structure

{result.stdout}
"""
        
        (output_dir / "api-reference.md").write_text(index_content)
        print(f"Generated API documentation at {output_dir / 'api-reference.md'}")
        
        # Also try to generate detailed docs
        try:
            detailed_result = subprocess.run(
                [str(python_exe), "-c", """
import bedrock_ge
import inspect
import sys

def document_module(module, prefix=""):
    content = []
    
    # Module docstring
    if module.__doc__:
        content.append(f"## {prefix}{module.__name__}")
        content.append(module.__doc__.strip())
        content.append("")
    
    # Get all public members
    members = [(name, obj) for name, obj in inspect.getmembers(module) 
               if not name.startswith('_')]
    
    # Document classes
    classes = [(name, obj) for name, obj in members if inspect.isclass(obj)]
    if classes:
        content.append("### Classes")
        content.append("")
        for name, cls in classes:
            content.append(f"#### {name}")
            if cls.__doc__:
                content.append(cls.__doc__.strip())
            content.append("")
    
    # Document functions
    functions = [(name, obj) for name, obj in members if inspect.isfunction(obj)]
    if functions:
        content.append("### Functions")
        content.append("")
        for name, func in functions:
            content.append(f"#### {name}")
            if func.__doc__:
                content.append(func.__doc__.strip())
            try:
                sig = inspect.signature(func)
                content.append(f"```python")
                content.append(f"{name}{sig}")
                content.append(f"```")
            except:
                pass
            content.append("")
    
    return "\\n".join(content)

# Document main module
print(document_module(bedrock_ge))

# Try to document gi submodule
try:
    import bedrock_ge.gi
    print("\\n" + document_module(bedrock_ge.gi, "gi."))
except ImportError:
    pass
"""],
                capture_output=True,
                text=True
            )
            
            if detailed_result.returncode == 0 and detailed_result.stdout.strip():
                detailed_content = f"""---
title: bedrock-ge Detailed API
description: Detailed API documentation for bedrock-ge
---

# bedrock-ge Detailed API

{detailed_result.stdout}
"""
                (output_dir / "detailed-api.md").write_text(detailed_content)
                print(f"Generated detailed API documentation at {output_dir / 'detailed-api.md'}")
                
        except subprocess.CalledProcessError:
            print("Could not generate detailed documentation")

if __name__ == "__main__":
    generate_docs_with_pdoc()