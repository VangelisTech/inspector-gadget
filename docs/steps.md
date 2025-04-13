step 1: attach code introspection tool to the llm 
if llm uses tool, it enables them to traverse the api stack through inspect or AST as it chooses. 
It enables the llm to collect context iteratively building an AST of the codebase. 
Finally the llm is asked to generate code and for the pieces of code in the generated response pull the api calls and grammars for those things and put it into a prompt to validate and generate against it. 


So given a task, with library dependencies X, IF Agent wants to inspect (which is recommendable in the agent system prompt or by the user, the inpect and AST modules help generate grammars and regex. The workflow is managed by choices at different steps. 