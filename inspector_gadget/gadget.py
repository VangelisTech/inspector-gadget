import inspect
import types
import ast
from enum import Enum 

from outlines import Template, models, generate
from outlines.samplers import greedy

import lark


class Gadget:
    """
    An Agent Tool that enables an agent to leverage underlying classes 
    and methods of a provided library or module. Enables Asynchronous traversal
    and introspection of third party libraries enabling the agent to adopt the 
    entire API as a suite of tools.
    """
    def __init__(self, module, name, api_map, grammar):
        self.module = module            # the actual Python module
        self.name = module.__name__     # name of the module (e.g., "networkx")
        self.api_map = api_map          # dictionary mapping function names to signatures
        self.grammar = grammar          # the Lark grammar (as a string) derived from the API map

    def get_tool_description(self):
        """
        Returns a descriptive prompt block for the gadget.
        Includes the module name, a summary of its API, and the grammar.
        """
        description = f"Module: {self.name}\n"
        description += "API Functions:\n"
        for func, sig in self.api_map.items():
            description += f"  - {func}{sig}\n"
        description += "\nGrammar (constrained syntax):\n"
        description += self.grammar
        return description

    def as_declarative_tool(self):
        """
        Returns a string that can be inserted into a larger system prompt,
        declaring the gadget as an available tool.
        """
        return f"Tool({self.name}): " + self.get_tool_description()

    


class GadgetFactory:
    """
    Stacks together layers for:
        Grammar-constrained generation for correctness
        Outlines/templates for idiomatic structures
        Reference code in context for usage fidelity
        Optional: Runtime validation agents to test or simulate output

    Given a task, extract necessary context from the dependency and construct a 
    composite prompt with constrained generation. 

    1. Inspect the dependency to extract API context
    2. Inspect the dependency to extract AST context
    3. Identify relevant methods and classes to include in the prompt.
    4. Identify relevant design patterns to include in the prompt.
    5. Identify relevant examples to include in the prompt.
    4. Identify 
    3. Construct a composite prompt with constrained generation
    4. Generate code
    5. Validate the code
    6. Return the code
    """
    def __init__(self, dependency: Module, model: models.Model, sampler: outlines.samplers.Sampler = greedy):
        self.dependency = dependency
        self.sampler = sampler
        self.model = model

        
    def __call__(self, task: str):
        """
        Given a task, extract necessary context from the dependency and construct a 
        composite prompt with constrained generation interface. 

        Returns the gadget.
        """

        # Given Task, identify relevant contexts 


    def provision_context_choices(self):
        """
        Provision the context choices for the gadget.
        """
        generate.choice(model, choices, sampler = self.sampler) 

    def _build_gadget(self, ):
        """
        Builds the gadget.
        """
        generate.cfg(gadget, grammar) 
    
    def _build_gadget_system_prompt(self):
        """
        Builds the gadget system prompt.
        """
        return 

    def _inpect_module(self):
        """
        Extracts the API context from the dependency.
        """
        
        grammar 
        return APILevelGrammar = Template.from_string(grammar)

    def _ast_module(self):
        """
        Extracts the AST context from the dependency.
        """
        return ast.parse(self.dependency)
    
    def _get_relevant_api_context(self, dependency: Module):
        """
        Gets the relevant API context for the dependency.
        """
        # Inspect and AST the dependency and construct an enum of the relevant API calls.
        relevant_inspect_context = self._inspect_module(dependency)
        generate.choice(model, choices, sampler = self.sampler)
        
    
    def _generate_api_grammar(self, dependency: Module):
        """
        Generates the API grammar for the dependency.
        """
        return 
    
    def _get_relevant_scripting_grammar(self, dependency: Module):
        """
        Generates the scripting grammar for the dependency.
        """
        return 



class GadgetFactory:
    @staticmethod
    def build_gadget(module):
        """
        Inspects the given module, extracts API information, generates grammar,
        and returns a Gadget instance.
        """
        api_map = {}
        for name, obj in inspect.getmembers(module):
            if isinstance(obj, (types.FunctionType, types.BuiltinFunctionType)):
                try:
                    api_map[name] = str(inspect.signature(obj))
                except (ValueError, TypeError):
                    continue

        # Generate grammar from the API map.
        grammar = convert_to_lark_grammar(api_map)
        return Gadget(module, module.__name__, api_map, grammar)

# Example: Build a Gadget for networkx
gadget_networkx = GadgetFactory.build_gadget(nx)
print(gadget_networkx.get_tool_description())
