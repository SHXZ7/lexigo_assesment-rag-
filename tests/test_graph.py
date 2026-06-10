import sys
from pathlib import Path
import json

# Add the app directory to sys.path so we can import modules from it
sys.path.append(str(Path(__file__).parent / "app"))

from graph import graph

if __name__ == "__main__":
    # Test Case 1: Valid question
    print("--- Running Test Case 1: Valid Question ---")
    result1 = graph.invoke({
        "question": "When is the hearing scheduled?"
    })
    print("Output:")
    print(json.dumps(result1, indent=2, default=str))
    print("\n" + "="*50 + "\n")

    # Test Case 2: Bad question
    print("--- Running Test Case 2: Bad Question ---")
    result2 = graph.invoke({
        "question": "Who is the president of India?"
    })
    print("Output:")
    print(json.dumps(result2, indent=2, default=str))
