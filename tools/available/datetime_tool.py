"""
DateTime tool for getting current time and date information.
"""

from datetime import datetime, timezone
from typing import List
from tools.base import BaseTool, ToolParameter


class DateTimeTool(BaseTool):
    """A tool for getting current date and time information."""
    
    @property
    def name(self) -> str:
        return "get_datetime"
    
    @property
    def description(self) -> str:
        return "Get current date and time information in various formats"
    
    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="format",
                type="string",
                description="Format for the date/time output",
                enum=["iso", "human", "timestamp", "date_only", "time_only"],
                required=False
            )
        ]
    
    def execute(self, format: str = "human") -> str:
        """Execute the datetime operation."""
        try:
            now = datetime.now(timezone.utc)
            local_now = datetime.now()
            
            if format == "iso":
                return f"Current time (UTC): {now.isoformat()}"
            elif format == "timestamp":
                return f"Current timestamp: {int(now.timestamp())}"
            elif format == "date_only":
                return f"Current date: {local_now.strftime('%Y-%m-%d')}"
            elif format == "time_only":
                return f"Current time: {local_now.strftime('%H:%M:%S')}"
            else:  # human format (default)
                return f"Current date and time: {local_now.strftime('%A, %B %d, %Y at %I:%M:%S %p')}"
                
        except Exception as e:
            return f"Error getting date/time: {str(e)}" 