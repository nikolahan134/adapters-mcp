# adapters-mcp

A learning project for building MCP (Model Context Protocol) servers and connecting them to LangChain agents via [`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters).

## Overview

This repo demonstrates:

- **MCP servers** built with [FastMCP](https://github.com/jlowin/fastmcp)
- **LangChain integration** using `load_mcp_tools` and `create_agent`
- Two example servers: a math server (stdio) and a weather server (SSE)

