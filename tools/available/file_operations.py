"""
File operations tool for reading and listing files.
"""

import os
from pathlib import Path
from typing import List
from tools.base import BaseTool, ToolParameter


class FileOperations(BaseTool):
    """A tool for basic file operations like reading and listing files."""
    
    @property
    def name(self) -> str:
        return "file_operations"
    
    @property
    def description(self) -> str:
        return "Perform file operations like reading file contents or listing directory contents"
    
    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="operation",
                type="string",
                description="Operation to perform",
                enum=["read_file", "list_directory"]
            ),
            ToolParameter(
                name="path",
                type="string",
                description="File or directory path"
            )
        ]
    
    def execute(self, operation: str, path: str) -> str:
        """Execute the file operation."""
        try:
            path_obj = Path(path)
            
            if operation == "read_file":
                if not path_obj.exists():
                    return f"Error: File '{path}' does not exist"
                
                if not path_obj.is_file():
                    return f"Error: '{path}' is not a file"
                
                try:
                    with open(path_obj, 'r', encoding='utf-8') as f:
                        content = f.read()
                    return f"Contents of '{path}':\n\n{content}"
                except UnicodeDecodeError:
                    return f"Error: Cannot read '{path}' as text file (binary file?)"
                
            elif operation == "list_directory":
                if not path_obj.exists():
                    return f"Error: Directory '{path}' does not exist"
                
                if not path_obj.is_dir():
                    return f"Error: '{path}' is not a directory"
                
                items = []
                for item in sorted(path_obj.iterdir()):
                    item_type = "📁" if item.is_dir() else "📄"
                    items.append(f"{item_type} {item.name}")
                
                return f"Contents of directory '{path}':\n\n" + "\n".join(items)
            
            else:
                return f"Error: Unknown operation '{operation}'"
                
        except PermissionError:
            return f"Error: Permission denied accessing '{path}'"
        except Exception as e:
            return f"Error: {str(e)}" 