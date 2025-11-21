import asyncio
from fastmcp import Client

async def main():
    # Connect via in-memory transport to the server script
    # The client can directly interact with the FastMCP instance
    # if it's running as a script with mcp.run() (default STDIO transport)
    async with Client("./fastmcp-server.py") as client:
        print("Connected to FastMCP server.")

        # List available tools to confirm server is working
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        # Call the search_local_files tool
        # Replace 'YOUR_QUERY' with a file pattern (e.g., "*.py", "fastmcp-server.py")
        # Replace 'YOUR_ROOT_DIR' with a directory to search, or keep "." for current directory
        query = "*.py" # Example: search for all Python files
        root_dir = "." # Example: search in the current directory

        print(f"\nCalling tool 'search_local_files' with query='{query}' and root_dir='{root_dir}'...")
        try:
            result = await client.call_tool("search_local_files", {"query": query, "root_dir": root_dir})
            print(f"Tool call result: {result.content}")
        except Exception as e:
            print(f"Error calling tool: {e}")

if __name__ == "__main__":
    asyncio.run(main())
