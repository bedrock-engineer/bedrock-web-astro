#!/usr/bin/env python3
"""
Post-process generated pydoc-markdown files to add prev: false and next: false
to the frontmatter for better Starlight navigation.
"""

import os
import re
from pathlib import Path


def update_frontmatter(file_path: Path):
    """Update frontmatter in a markdown file to include prev: false and next: false."""
    content = file_path.read_text(encoding='utf-8')
    
    # Check if file has frontmatter
    if not content.startswith('---'):
        return
    
    # Find the end of frontmatter
    lines = content.split('\n')
    frontmatter_end = -1
    
    for i, line in enumerate(lines[1:], 1):  # Skip first ---
        if line.strip() == '---':
            frontmatter_end = i
            break
    
    if frontmatter_end == -1:
        return
    
    # Check if prev/next already exist
    frontmatter_content = '\n'.join(lines[1:frontmatter_end])
    if 'prev:' in frontmatter_content or 'next:' in frontmatter_content:
        return  # Already has navigation settings
    
    # Insert prev: false and next: false before the closing ---
    lines.insert(frontmatter_end, 'prev: false')
    lines.insert(frontmatter_end + 1, 'next: false')
    
    # Write back to file
    updated_content = '\n'.join(lines)
    file_path.write_text(updated_content, encoding='utf-8')
    print(f"Updated: {file_path}")


def main():
    """Process all markdown files in the reference directory."""
    reference_dir = Path('src/content/docs/reference')
    
    if not reference_dir.exists():
        print(f"Reference directory not found: {reference_dir}")
        return
    
    # Find all .md files recursively
    for md_file in reference_dir.rglob('*.md'):
        update_frontmatter(md_file)
    
    print("Frontmatter update completed!")


if __name__ == '__main__':
    main()