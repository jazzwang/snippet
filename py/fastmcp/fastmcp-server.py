import os
import fnmatch
from typing import List
from fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("Local File Search Server")

@mcp.tool
def search_local_files(query: str, root_dir: str = ".") -> List[str]:
    """
    Searches for files matching a given pattern in the specified directory and its subdirectories.

    Args:
        query (str): The filename pattern to search for (e.g., "*.txt", "report.pdf").
        root_dir (str): The root directory to start the search from. Defaults to the current directory.

    Returns:
        List[str]: A list of full paths to the files that match the query.
    """
    matching_files = []
    # Ensure the root_dir is valid
    if not os.path.isdir(root_dir):
        # Using print for warning as ctx.info() is not available outside a tool call context
        print(f"Warning: Directory '{root_dir}' not found or is not a directory. Returning empty list.")
        return []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, query):
            matching_files.append(os.path.join(dirpath, filename))
    return matching_files

if __name__ == "__main__":
    # Run the FastMCP server. By default, it uses the STDIO transport,
    # which is suitable for local command-line interaction.
    mcp.run()
