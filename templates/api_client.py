"""
API Client Template

Quick-start template for testing APIs.
Requires: requests (pip install requests)
"""
from typing import Dict, Any, Optional
import json


def api_request(
    url: str,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Make an API request.
    
    Args:
        url: API endpoint URL
        method: HTTP method (GET, POST, PUT, DELETE)
        headers: Request headers
        params: Query parameters
        data: Request body data
        
    Returns:
        API response as dictionary
    """
    try:
        import requests
    except ImportError:
        raise ImportError("requests library required: pip install requests")
    
    if headers is None:
        headers = {"Content-Type": "application/json"}
    
    response = requests.request(
        method=method,
        url=url,
        headers=headers,
        params=params,
        json=data
    )
    
    response.raise_for_status()
    
    return {
        'status_code': response.status_code,
        'headers': dict(response.headers),
        'body': response.json() if response.content else None
    }


def test_api():
    """Example API tests."""
    print("🌐 API Testing")
    print("=" * 40)
    
    # Example: Test a public API
    # Replace with your actual API endpoint
    url = "https://api.github.com/zen"
    
    try:
        print(f"\n📡 GET {url}")
        result = api_request(url)
        print(f"✅ Status: {result['status_code']}")
        print(f"📦 Response: {result['body']}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Add more test cases here
    
    print("\n" + "=" * 40)
    print("✨ Testing complete")


def main():
    """Main execution."""
    test_api()


if __name__ == "__main__":
    main()
