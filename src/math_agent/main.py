#!/usr/bin/env python
import warnings

from math_agent.crew import MathAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'problem': 'What is the sum of 3 and 5?',
    }
    
    try:
        MathAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

