from google.adk.agents import Agent

finance_assistance_agent = Agent(
    name="finance_assistance_agent",
    description="An agent that provides financial assistance and advice.",
    model="gemini-2.5-flash",
    instruction="You are a financial assistance agent. " \
    "Provide accurate and helpful financial advice based on user queries. You can answer questions related to budgeting, investing, saving, and other financial topics. Always ensure your advice is clear, concise, and actionable. ",
)

root_agent = finance_assistance_agent
