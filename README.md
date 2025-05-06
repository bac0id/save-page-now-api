# save-page-now-api
 A Python wrapper for Internet Archive Wayback Machine's Save Page Now API.

## Feature

* **Easy to Use:** Provides a simple interface to interact with the Save Page Now API.
* **Customizable SPN Host and Proxy:** Allows specifying a custom SPN host and proxy settings, enabling use with services like Tor.

## Usage

Send a save request to SPN:

```python
from save_page_now_api import SavePageNowApi
api = SavePageNowApi(token="XXX:YYY")
result = api.save("https://example.com")
"""
result:
{
    'url': 'https://example.com',
    'job_id': 'spn2-XXXXXXXXXXXXXX'
}
"""
```

API with Tor:

```python
proxies = {
    "http": "schema://host:port",
    "https": "schema://host:port",
}
tor_api = SavePageNowApi(token="XXX:YYY", host="https://ZZZ.onion", proxies=proxies)
```

## Installation

```bash
pip install save-page-now-api
```

## Test
```bash
python -m unittest
```
