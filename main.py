import asyncio
from pathlib import Path
from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI()
server_path = Path(__file__).parent / "servers" / "math_server.py"
stdio_server_params = StdioServerParameters(
    command="python",
    args=[str(server_path)],

)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initilized")

            # tools = await session.list_tools()
            tools = await load_mcp_tools(session)
            print(tools)

            agent = create_agent(llm, tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="what is 2 + 2")]})
            print(result["messages"][-1].content)
if __name__ == "__main__":
    asyncio.run(main())
