import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/wordgrabbag/api/similar-words'

mcp = FastMCP('similar-words')

@mcp.tool()
def moar(query: Annotated[str, Field(description="this is the query parameter. words are separated by space ' ', and some words can be joined by an ascii dash -, e.g. new-york")]) -> dict: 
    '''the endpoint.'''
    url = 'https://similarwords.p.rapidapi.com/moar'
    headers = {'x-rapidapi-host': 'similarwords.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
