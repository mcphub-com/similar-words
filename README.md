# Similar Words MCP Server

## Overview

The Similar Words MCP Server is a tool designed to assist users in finding words that are similar to the ones they provide as input. This can be particularly useful for generating new keywords, adding tags, or exploring related concepts. The service is versatile, allowing you to enter multiple words to uncover related themes or categories. For instance, entering "apple pear" may yield results related to fruits, while "apple microsoft" could return terms associated with tech companies.

## Features

- **Word Similarity Search**: The core functionality of this tool is to identify and return words that are similar to the input words. This can be an asset for various applications, such as content creation, SEO optimization, and brainstorming sessions.
  
- **Multi-Word Input**: Users can input multiple words to receive nuanced results. The service can recognize complex queries where context is essential to determining similarity.

## Tool Usage

### `/moar` Endpoint

- **Description**: This endpoint is the primary function of the server, designed to return similar words based on the provided input.
  
- **Parameters**:
  - `query` (String): The main parameter for this endpoint. Words should be separated by spaces, and some words can be joined using an ASCII dash (`-`), such as in "new-york".

The Similar Words MCP Server is a powerful tool for those looking to expand their vocabulary, discover new associations, or simply explore the linguistic landscape. Whether you're a writer, marketer, or developer, this service can provide valuable insights and inspiration.