import inspect
import types
import ast


def extract_module_functions(module):
    """
    Extracts top-level functions from a module using inspect,
    and returns a dict of function names to their signatures as strings.
    Includes basic error handling for signature extraction.
    """
    function_signatures = {}
    # Iterate through members, checking if they are functions/builtins
    for name, obj in inspect.getmembers(module):
        if isinstance(obj, (types.FunctionType, types.BuiltinFunctionType)):
            try:
                # Attempt to get the signature
                signature = inspect.signature(obj)
                function_signatures[name] = str(signature)
            except (ValueError, TypeError) as e:
                # If signature can't be retrieved (e.g., some C extensions),
                # store a placeholder or skip. Let's store a placeholder.
                # print(f"Could not get signature for {name}: {e}")
                function_signatures[name] = "(*args, **kwargs)" # Placeholder
            except Exception as e:
                # Catch any other unexpected errors during inspection
                print(f"Unexpected error inspecting {name}: {e}")
                continue # Skip this member
    return function_signatures


def extract_module_classes(module):
    """
    Extracts top-level classes from a module using inspect,
    and returns a dict of class names to their signatures as strings.
    """
    class_signatures = {}
    for name, obj in inspect.getmembers(module):
        if isinstance(obj, type):
            try:
                # Attempt to get the signature
                signature = inspect.signature(obj)
                class_signatures[name] = str(signature)
            except (ValueError, TypeError) as e:
                # If signature can't be retrieved (e.g., some C extensions),
                # store a placeholder or skip. Let's store a placeholder.
                # print(f"Could not get signature for {name}: {e}")
                class_signatures[name] = "(*args, **kwargs)" # Placeholder
            except Exception as e:
                print(f"Unexpected error inspecting {name}: {e}")

def extract_

def convert_to_lark_grammar(api_map):
    """
    Convert the API map into a Lark-compatible grammar.
    This is the same (or similar to) the routine we developed earlier.
    """
    grammar_lines = [
        "start: statement+",
        "",
        "statement: " + " | ".join(f"{name}_call" for name in api_map.keys() if name.isidentifier()),
        ""
    ]

    for name in api_map.keys():
        if not name.isidentifier():
            continue
        # For each function, create a simple rule. You can extend this with parameter types later.
        grammar_lines.append(f"{name}_call: \"{name}\" \"(\" [args] \")\"")

    grammar_lines.extend([
        "",
        "args: value (\",\" value)*",
        "value: ESCAPED_STRING | SIGNED_NUMBER | NAME",
        "",
        "%import common.ESCAPED_STRING",
        "%import common.SIGNED_NUMBER",
        "%import common.CNAME -> NAME",
        "%import common.WS",
        "%ignore WS"
    ])

    return "\n".join(grammar_lines)def _extract_module_functions(self, module):
    """
    Extracts top-level functions from a module using inspect,
    and returns a dict of function names to their signatures as strings.
    Includes basic error handling for signature extraction.
    """
    function_signatures = {}
    # Iterate through members, checking if they are functions/builtins
    for name, obj in inspect.getmembers(module):
        if isinstance(obj, (types.FunctionType, types.BuiltinFunctionType)):
            try:
                # Attempt to get the signature
                signature = inspect.signature(obj)
                function_signatures[name] = str(signature)
            except (ValueError, TypeError) as e:
                # If signature can't be retrieved (e.g., some C extensions),
                # store a placeholder or skip. Let's store a placeholder.
                # print(f"Could not get signature for {name}: {e}")
                function_signatures[name] = "(*args, **kwargs)" # Placeholder
            except Exception as e:
                # Catch any other unexpected errors during inspection
                print(f"Unexpected error inspecting {name}: {e}")
                continue # Skip this member
    return function_signatures


def _extract_module_classes(self, module):
    """
    Extracts top-level classes from a module using inspect,
    and returns a dict of class names to their signatures as strings.
    """
    class_signatures = {}
    for name, obj in inspect.getmembers(module):
        if isinstance(obj, type):
            try:
                # Attempt to get the signature
                signature = inspect.signature(obj)
                class_signatures[name] = str(signature)
            except (ValueError, TypeError) as e:
                # If signature can't be retrieved (e.g., some C extensions),
                # store a placeholder or skip. Let's store a placeholder.
                # print(f"Could not get signature for {name}: {e}")
                class_signatures[name] = "(*args, **kwargs)" # Placeholder
            except Exception as e:
                print(f"Unexpected error inspecting {name}: {e}")

def convert_to_lark_grammar(api_map):
    """
    Convert the API map into a Lark-compatible grammar.
    This is the same (or similar to) the routine we developed earlier.
    """
    grammar_lines = [
        "start: statement+",
        "",
        "statement: " + " | ".join(f"{name}_call" for name in api_map.keys() if name.isidentifier()),
        ""
    ]

    for name in api_map.keys():
        if not name.isidentifier():
            continue
        # For each function, create a simple rule. You can extend this with parameter types later.
        grammar_lines.append(f"{name}_call: \"{name}\" \"(\" [args] \")\"")

    grammar_lines.extend([
        "",
        "args: value (\",\" value)*",
        "value: ESCAPED_STRING | SIGNED_NUMBER | NAME",
        "",
        "%import common.ESCAPED_STRING",
        "%import common.SIGNED_NUMBER",
        "%import common.CNAME -> NAME",
        "%import common.WS",
        "%ignore WS"
    ])

    return "\n".join(grammar_lines)