from ibm_watsonx_orchestrate.agent_builder.agents import Agent, AgentKind, AgentStyle
from ibm_watsonx_orchestrate.agent_builder.tools import *

main_agent = Agent(
    name="main_agent",
    title="Main agent",
    nickname="main_agent",
    kind=AgentKind.NATIVE,
    llm="watsonx/meta-llama/llama-3-3-70b-instruct",
    style=AgentStyle.REACT,
    description="Hoofdagent. Beheert de oplossing van het probleem en reageert op de gebruiker.",
    instructions="Communiceer alleen in het Nederlands. Beantwoord alle vragen van gebruikers. Als je het antwoord niet weet, gebruik dan een van je tools.",
    collaborators=["mortgage_advisor"],
    tools=["wiki_search"],
)
