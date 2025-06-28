"""
Calculator tool for basic mathematical operations.
"""

from typing import List
from tools.base import BaseTool, ToolParameter


class Calculator(BaseTool):
    """A tool for performing basic mathematical calculations."""
    
    @property
    def name(self) -> str:
        return "calculate"
    
    @property
    def description(self) -> str:
        return "Perform basic mathematical calculations (addition, subtraction, multiplication, division)"
    
    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="expression",
                type="string",
                description="Mathematical expression to evaluate (e.g., '2 + 3 * 4')"
            )
        ]
    
    def execute(self, expression: str) -> str:
        """Execute the calculation."""
        try:
            # For safety, only allow basic mathematical operations
            allowed_chars = set('0123456789+-*/.() ')
            if not all(c in allowed_chars for c in expression):
                return "Error: Invalid characters in expression. Only numbers and +, -, *, /, (, ) are allowed."
            
            # Evaluate the expression
            result = eval(expression)
            return f"Result: {expression} = {result}"
            
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception as e:
            return f"Error evaluating expression: {str(e)}" 