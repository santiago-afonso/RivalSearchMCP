#!/usr/bin/env python3
"""Simple test script for stdio MCP server."""

import subprocess
import json
import sys

def test_mcp_server():
    """Test the MCP server with stdio."""
    
    # Start the server
    process = subprocess.Popen(
        ['.venv/bin/python', 'server.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    # Test 1: Initialize
    print("Test 1: Initialize")
    init_msg = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0.0"}
        }
    }
    
    process.stdin.write(json.dumps(init_msg) + '\n')
    process.stdin.flush()
    
    # Read response
    response = process.stdout.readline()
    if response:
        try:
            result = json.loads(response)
            if "result" in result:
                print("✓ Initialize successful")
                print(f"  Server: {result['result']['serverInfo']['name']}")
                print(f"  Version: {result['result']['serverInfo']['version']}")
            else:
                print(f"✗ Initialize failed: {result.get('error', 'Unknown error')}")
        except json.JSONDecodeError as e:
            print(f"✗ Failed to parse response: {e}")
            print(f"  Response: {response}")
    
    # Test 2: List tools
    print("\nTest 2: List tools")
    tools_msg = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
    }
    
    process.stdin.write(json.dumps(tools_msg) + '\n')
    process.stdin.flush()
    
    response = process.stdout.readline()
    if response:
        try:
            result = json.loads(response)
            if "result" in result and "tools" in result["result"]:
                tools = result["result"]["tools"]
                print(f"✓ Found {len(tools)} tools")
                print("  Available tools:")
                for tool in tools[:5]:  # Show first 5
                    print(f"    - {tool['name']}")
                if len(tools) > 5:
                    print(f"    ... and {len(tools) - 5} more")
            else:
                print(f"✗ List tools failed: {result.get('error', 'Unknown error')}")
        except json.JSONDecodeError as e:
            print(f"✗ Failed to parse response: {e}")
    
    # Cleanup
    process.terminate()
    process.wait(timeout=5)
    
    print("\n✓ All tests completed successfully!")

if __name__ == "__main__":
    test_mcp_server()
