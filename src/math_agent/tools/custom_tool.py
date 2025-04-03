from crewai.tools import tool

@tool("math_tool")
def math_tool(problem: str) -> str:
    """This tool is used to solve math problems."""
    return eval(problem)
