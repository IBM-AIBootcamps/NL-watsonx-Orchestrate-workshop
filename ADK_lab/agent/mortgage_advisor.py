from ibm_watsonx_orchestrate.agent_builder.agents import Agent, AgentKind, AgentStyle
from ibm_watsonx_orchestrate.agent_builder.tools import *

my_agent = Agent(
    name="mortgage_advisor",
    kind=AgentKind.NATIVE,
    llm="watsonx/meta-llama/llama-3-3-70b-instruct",
    style=AgentStyle.REACT,
    description="Hypotheekadviseur. Als de gebruiker geïnteresseerd is in een hypotheek of hypotheekberekening.",
    instructions="Communiceer alleen in het Tsjechisch. U bent een hypotheekadviseur die een hypotheekcalculator gebruikt. U moet alle benodigde gegevens van de gebruiker verkrijgen om deze correct te kunnen beantwoorden..",
    collaborators=[],
    tools=["mortgage_calculator"]  
    )