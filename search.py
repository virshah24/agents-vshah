import json
import os
from typing import Annotated
from semantic_kernel.functions import kernel_function
from tavily import TavilyClient

class SearchPlugin:
    
    @kernel_function(description="Searches the internet for information.")
    async def search(self, query: Annotated[str, "The input text"])  -> Annotated[json, "Returns the results from the internet search."]:
        print("Performing search...")
        print(f"Query: {query}")
        # Perform a search using the Serper API
        tavily_client = TavilyClient(api_key=os.environ.get('TAVILY_API_KEY', ''))
        response = tavily_client.search(query)
        return response