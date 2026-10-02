#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

def check_file_exists(filepath):
    if not os.path.exists(filepath):
        print(f"Error: Missing required file {filepath}")
        return False
    return True

def check_markdown_links(filepath):
    """Simple check for working relative local markdown links."""
    if not str(filepath).endswith(".md"):
        return True
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match markdown links: [text](link)
    # Ignore http/https
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    links = link_pattern.findall(content)
    
    success = True
    base_dir = os.path.dirname(filepath)
    
    for text, link in links:
        if link.startswith('http') or link.startswith('#') or link.startswith('mailto:'):
            continue
            
        target_path = os.path.normpath(os.path.join(base_dir, link))
        if not os.path.exists(target_path):
            print(f"Error in {filepath}: Broken link to {link} (resolved to {target_path})")
            success = False
            
    return success

def check_frontmatter(filepath, required_fields):
    """Check if markdown file has yaml frontmatter and required fields."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if not content.startswith('---'):
        print(f"Error in {filepath}: Missing frontmatter metadata.")
        return False
        
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"Error in {filepath}: Malformed frontmatter metadata.")
        return False
        
    frontmatter = parts[1]
    success = True
    for field in required_fields:
        if not re.search(rf'^{field}:', frontmatter, re.MULTILINE):
            print(f"Error in {filepath}: Missing required metadata field '{field}'")
            success = False
            
    return success

def main():
    repo_root = Path(__file__).parent.parent
    os.chdir(repo_root)
    
    success = True
    
    # 1. Check required scaffold files
    required_files = [
        "README.md", "ROADMAP.md", "CONTRIBUTING.md", "CHANGELOG.md",
        ".gitignore", ".editorconfig",
        "programmes/README.md", "programmes/ral/README.md",
        "projects/README.md", "projects/improvement-verification/README.md",
        "writing/README.md", "reading/README.md", "docs/conventions.md"
    ]
    
    print("Checking required files...")
    for f in required_files:
        if not check_file_exists(f):
            success = False
            
    # 2. Check all markdown links
    print("Checking markdown links...")
    for root, dirs, files in os.walk('.'):
        if '.github' in root or 'templates' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                if not check_markdown_links(os.path.join(root, file)):
                    success = False
                    
    # 3. Check metadata on specific content types
    print("Checking metadata...")
    # Programmes
    for root, dirs, files in os.walk('programmes'):
        if 'templates' in root: continue
        for file in files:
            if file == 'README.md' and root != 'programmes' and 'sources' not in root:
                # specific programme readme
                if not check_frontmatter(os.path.join(root, file), ['id', 'title', 'status', 'created']):
                    success = False
                    
    # Projects
    for root, dirs, files in os.walk('projects'):
        if 'templates' in root: continue
        for file in files:
            if file == 'README.md' and root != 'projects' and len(Path(root).parts) == 2:
                # specific project readme
                if not check_frontmatter(os.path.join(root, file), ['id', 'title', 'status', 'programme', 'created']):
                    success = False

    if success:
        print("All checks passed!")
        sys.exit(0)
    else:
        print("Some checks failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
