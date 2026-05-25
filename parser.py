"""
AST Parser for extracting functions, classes, and methods from code.
Supports Python, JavaScript, TypeScript initially.
"""
import tree_sitter
from tree_sitter import Language, Parser
from pathlib import Path
from typing import List, Dict


class CodeParser:
    def __init__(self):
        # TODO: Build tree-sitter languages
        # For now, placeholder
        self.python_parser = None
        self.js_parser = None
        
    def extract_symbols(self, code: str, language: str) -> List[Dict]:
        """
        Extract functions, classes, methods from code.
        Returns list of symbols with:
        - name: symbol name
        - type: 'function' | 'class' | 'method'
        - code: full code snippet
        - line: line number
        - docstring: if available
        """
        # TODO: Implement tree-sitter parsing
        # For MVP PoC, simple regex fallback
        return self._simple_extract(code, language)
    
    def _simple_extract(self, code: str, language: str) -> List[Dict]:
        """Simple regex-based extraction for PoC"""
        import re
        symbols = []
        
        if language == "python":
            # Find function definitions
            func_pattern = r'^def\s+(\w+)\s*\([^)]*\):'
            for match in re.finditer(func_pattern, code, re.MULTILINE):
                symbols.append({
                    'name': match.group(1),
                    'type': 'function',
                    'language': 'python',
                    'line': code[:match.start()].count('\n') + 1
                })
            
            # Find class definitions
            class_pattern = r'^class\s+(\w+)'
            for match in re.finditer(class_pattern, code, re.MULTILINE):
                symbols.append({
                    'name': match.group(1),
                    'type': 'class',
                    'language': 'python',
                    'line': code[:match.start()].count('\n') + 1
                })
        
        return symbols
