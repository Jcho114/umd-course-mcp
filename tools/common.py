import httpx
from typing import Dict, Any, List, Optional

DEFAULT_TIMEOUT = 30.0

ApiOutputObject = Optional[Dict[str, Any]]
ApiOutput = Optional[ApiOutputObject | List[ApiOutputObject]]


async def make_http_call(url: str, params: Dict[str, Any] = {}) -> ApiOutput:
    # filter out null params from url
    params = {k: v for k, v in params.items() if v is not None}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url=url,
                params=params,
                timeout=DEFAULT_TIMEOUT,
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}
