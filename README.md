# save-page-now-api
 A wrapper for Internet Archive Wayback Machine's Save Page Now API.

## Usage

```python
from save_page_now_api import SavePageNowApi

api = SavePageNowApi(token="XXX:YYY")
result = api.save("https://example.com")

print(result)
"""
{
    'url': 'https://example.com',
    'job_id': 'spn2-XXXXXXXXXXXXXX'
}
"""
```

## Installation

```bash
pip install save-page-now-api
```

## Test
```bash
python -m unittest
```
