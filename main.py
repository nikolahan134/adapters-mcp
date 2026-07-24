import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=["D:/langchain course/adapters-mcpservers/math_server.py"],

)

async def main():
    print("Hello from adapters-mcp!")


if __name__ == "__main__":
    asyncio.run(main())
