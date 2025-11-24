#!/usr/bin/env python3
"""Test the google_search tool via MCP stdio."""

import subprocess
import json
import sys

def test_google_search():
    """Test google_search tool."""
    
    # Start the server
    process = subprocess.Popen(
        ['.venv/bin/python', 'server.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    # Initialize
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
    response = process.stdout.readline()
    print(f"Init response: {response[:100]}...")
    
    # Call google_search
    print("\n--- Calling google_search tool ---")
    search_msg = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "google_search",
            "arguments": {
                "query": "Asus P16 laptop Best Buy",
                "num_results": 5
            }
        }
    }
    
    process.stdin.write(json.dumps(search_msg) + '\n')
    process.stdin.flush()
    
    # Read response(s)
    print("Reading responses...")
    for i in range(10):  # Read up to 10 lines
        try:
            line = process.stdout.readline()
            if not line:
                break
            
            data = json.loads(line)
            
            # Check if this is the final result
            if "result" in data:
                print(f"\n✓ Got final result (id={data.get('id')})")
                result = data["result"]
                
                # Debug: show result structure
                print(f"  Result type: {type(result)}")
                if isinstance(result, dict):
                    print(f"  Result keys: {result.keys()}")
                    print(f"  isError: {result.get('isError')}")
                    
                    # Parse content
                    content = result.get("content", [])
                    if content:
                        print(f"  Content items: {len(content)}")
                        for idx, item in enumerate(content):
                            if item.get("type") == "text":
                                text = item.get("text", "")
                                # Try to parse as JSON
                                try:
                                    search_result = json.loads(text)
                                    print(f"\n  Parsed search result:")
                                    print(f"    Status: {search_result.get('status')}")
                                    print(f"    Method: {search_result.get('method')}")
                                    print(f"    Results count: {len(search_result.get('results', []))}")
                                    
                                    if search_result.get('results'):
                                        print("\n    First 3 results:")
                                        for idx, res in enumerate(search_result['results'][:3], 1):
                                            print(f"      {idx}. {res.get('title', 'N/A')[:60]}")
                                            print(f"         URL: {res.get('url', 'N/A')[:80]}")
                                    else:
                                        print("\n    ⚠ Results array is empty!")
                                        print(f"    Metadata: {search_result.get('metadata', {})}")
                                except json.JSONDecodeError:
                                    print(f"  Raw text (first 500 chars): {text[:500]}")
                    else:
                        print("  ⚠ No content items")
                elif isinstance(result, list):
                    print(f"  Result length: {len(result)}")
                break
            
            # Progress notifications
            elif "method" in data and data["method"] == "notifications/progress":
                progress = data.get("params", {})
                print(f"  Progress: {progress.get('progress', 0)}/{progress.get('total', 100)}")
            
            # Info messages
            elif "method" in data and data["method"] == "notifications/message":
                msg = data.get("params", {})
                print(f"  {msg.get('level', 'INFO')}: {msg.get('data', '')}")
                
        except json.JSONDecodeError as e:
            print(f"  Could not parse line: {line[:100]}")
        except Exception as e:
            print(f"  Error: {e}")
    
    # Cleanup
    process.terminate()
    process.wait(timeout=5)

if __name__ == "__main__":
    test_google_search()
