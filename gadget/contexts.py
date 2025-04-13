import inspect
import types
import ast

from outlines import Template, models, generate
from outlines.samplers import greedy
import lark

# --- Zen of Python --- 
#Purpose: Provide a soft inductive bias for correct Python code.
#Strength: Encourages correct syntax, semantics, and idioms.
#Limitation: Does not prevent hallucinations.
zen_of_python = Template.from_file("prompts/zen_of_python.txt")

# --- API Signatures Grammar --- 
#Purpose: Constrain generation to valid function/method calls.
#Strength: Prevents hallucination of APIs, ensures call signatures match.
#Limitation: Knows nothing of contextual usage, idiomatic sequencing, or logic.

# --- Scripting Grammar --- 
# (Python+Control Structures)
# Purpose: Allow agents to write whole programs—for loops, list comprehensions, if guards, class definitions, etc.
# Strength: Empowers the LLM to compose more than just API calls. This is what lets an agent act as a programmer.
# Limitation: Still doesn’t mean it uses APIs well. It’s just syntactically valid


# --- Software Patterns --- 
# (Idiomatic + Structural)
# Purpose: Encourage the LLM to use high-level structures like Singleton, Factory, Strategy, Event Loop, Observer, etc.
# Strength: Architectural intelligence. This adds a soft inductive bias toward maintainable, idiomatic code—FAIF, PyPat, etc.
# Limitation: Very hard to enforce. Best done via outline+examples or hybrid structural scaffolds, not strict CFGs.


# --- Other References --- 
#  (Code + Docs + Examples in Prompt)
# Purpose: Encourage the LLM to use contextual references to the codebase.
# Strength: Contextual references are a powerful way to guide the LLM to write code that is more likely to be correct and efficient.
# Limitation: Very hard to enforce. Best done via outline+examples or hybrid structural scaffolds, not strict CFGs.


PythonAgentSystemPrompt = Template.from_string("""
## Agent Task

You are writing Python code that performs the following task:

{%for task in tasks%}
- {task}
{%endfor%}

Your outputs shall be constrained by the following structured generations: 
{%for gadget in gadgets%}
- {gadget}
{%endfor%}
                                               

## Available API (constrained by grammar):
{%for api in apis%}
- {api}
{%endfor%}
                                               
## Design Principles

Follow these software patterns:
{%for pattern in patterns%}
- {pattern}
{%endfor%}
                                               
## Reference Example

Example usage of {module_name}:

```python
{example}
```
""")







class GeneratorEnum(Enum):
    """
    An enumeration of the different generators that can be used.
    """
    GADGET = generate.cfg
    SYSTEM = generate.regex
    TYPES = generate.format


