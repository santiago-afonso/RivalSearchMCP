# RivalSearchMCP - Quick Start Guide

## ✅ Setup Complete!

The RivalSearchMCP server is now configured and working with stdio transport.

## What Was Done

1. ✅ Installed all required dependencies
2. ✅ Configured FastMCP for stdio transport
3. ✅ Fixed middleware/route registration for stdio mode
4. ✅ Verified server functionality with test script

## How to Use

### Start the Server

The server runs automatically when invoked by an MCP client. To test manually:

```bash
.venv/bin/python server.py
```

### Run Tests

```bash
.venv/bin/python test_stdio.py
```

### Configure Your MCP Client

Use the absolute paths for your system. Update the paths in the examples below:

**For Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "rivalsearchmcp": {
      "command": "/path/to/RivalSearchMCP/.venv/bin/python",
      "args": ["/path/to/RivalSearchMCP/server.py"]
    }
  }
}
```

**For other MCP clients**, see `MCP_CONFIG.md` for more examples.

## Available Tools (18 total)

### Search & Discovery
- `retrieve_content` - Fetch and extract content from URLs
- `stream_content` - Stream content processing
- `google_search` - Advanced Google search

### Content Analysis  
- `traverse_website` - Explore website structure
- `analyze_content` - AI-powered content analysis
- `research_topic` - Comprehensive research

### Trends & Analytics
- `search_trends` - Google Trends analysis
- `compare_keywords` - Keyword comparison
- `export_trends` - Export trend data

### And 9 more tools for LLMs.txt generation, research workflows, etc.

## Test the Connection

Ask your AI assistant:
> "Use the google_search tool to search for 'latest AI news'"

## Key Changes Made

1. **server.py**: 
   - Middleware registration now conditional (production/HTTP only)
   - Custom routes registration now conditional (production/HTTP only)
   - Stdio mode runs without middleware to avoid context issues

2. **middleware.py**:
   - Fixed context access in RateLimitingMiddleware
   - Added safety checks for fastmcp_context

## Environment Variables

- `ENVIRONMENT=development` (default) - Runs with stdio
- `ENVIRONMENT=production` - Runs with HTTP on port 8000

## Troubleshooting

If the server doesn't start:
1. Ensure virtual environment is activated: `source .venv/bin/activate`
2. Reinstall dependencies: `.venv/bin/pip install -r requirements.txt`
3. Check Python version: `python3 --version` (requires 3.8+)

## Next Steps

1. Configure your MCP client with the paths above
2. Restart your AI assistant
3. Test by asking it to search or research a topic
4. Check logs in the terminal if issues occur

## Documentation

- Full installation guide: `docs/getting-started/installation.md`
- Configuration examples: `MCP_CONFIG.md`
- Test script: `test_stdio.py`

---

**Status**: ✅ Ready to use with stdio transport!
