# _temp_core_interface_inspect.py
import inspect
import types
import json
import sys
from core.interfaces import ComponentStoreInterface # Import the specific interface

def extract_class_methods(cls):
    """
    Extracts public methods (excluding those starting with '_') from a class
    using inspect, and returns a dict of method names to their signatures as strings.
    Includes basic error handling for signature extraction.
    """
    method_signatures = {}
    # Iterate through members, checking if they are methods/functions
    for name, obj in inspect.getmembers(cls):
        # Look for functions/methods, exclude private/protected ones
        if inspect.isfunction(obj) and not name.startswith('_'):
            try:
                # Attempt to get the signature
                signature = inspect.signature(obj)
                method_signatures[name] = str(signature)
            except (ValueError, TypeError) as e:
                # Store placeholder for methods without clear signatures
                # print(f"Could not get signature for {cls.__name__}.{name}: {e}", file=sys.stderr)
                method_signatures[name] = "(*args, **kwargs)" # Placeholder
            except Exception as e:
                # Catch any other unexpected errors during inspection
                print(f"Unexpected error inspecting {cls.__name__}.{name}: {e}", file=sys.stderr)
                continue # Skip this member
    return method_signatures

# Apply to ComponentStoreInterface
interface_signatures = extract_class_methods(ComponentStoreInterface)

# Output as JSON to stdout
try:
    print(json.dumps(interface_signatures, indent=2))
except IOError as e:
    if e.errno == 32: # errno.EPIPE
        pass
    else:
        raise 