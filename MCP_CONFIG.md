# RivalSearchMCP Configuration Examples

## For Claude Desktop

Add this to your Claude Desktop MCP settings file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "rivalsearchmcp": {
      "command": "/home/safonso/RivalSearchMCP/.venv/bin/python",
      "args": ["/home/safonso/RivalSearchMCP/server.py"],
      "env": {
        "ENVIRONMENT": "development"
      }
    }
  }
}
```

## For Cursor

Add this to `.cursorrules` or MCP settings:

```json
{
  "mcpServers": {
    "rivalsearchmcp": {
      "command": "/home/safonso/RivalSearchMCP/.venv/bin/python",
      "args": ["/home/safonso/RivalSearchMCP/server.py"]
    }
  }
}
```

## For VS Code with Continue

Add this to `~/.continue/config.json`:

```json
{
  "mcpServers": [
    {
      "name": "rivalsearchmcp",
      "command": "/home/safonso/RivalSearchMCP/.venv/bin/python",
      "args": ["/home/safonso/RivalSearchMCP/server.py"]
    }
  ]
}
```

## Generic MCP Client Configuration

```json
{
  "mcpServers": {
    "rivalsearchmcp": {
      "command": "/home/safonso/RivalSearchMCP/.venv/bin/python",
      "args": ["/home/safonso/RivalSearchMCP/server.py"],
      "transport": {
        "type": "stdio"
      }
    }
  }
}
```

## Available Tools

Once connected, you'll have access to 18 tools including:

### Search & Discovery
- `retrieve_content` - Enhanced content retrieval from URLs
- `stream_content` - Real-time streaming content processing
- `google_search` - Advanced Google search with rich snippets

### Content Analysis
- `traverse_website` - Intelligent website exploration
- `analyze_content` - AI-powered content analysis
- `research_topic` - End-to-end research workflow

### Trends & Analytics
- `search_trends` - Google Trends analysis for keywords
- `compare_keywords` - Comprehensive keyword comparison
- `export_trends` - Export trends data in multiple formats

### And more...

## Testing the Connection

Run the included test script:

```bash
.venv/bin/python test_stdio.py
```

Or test manually with your MCP client by asking:
"Search for 'latest AI news' using the available tools"
