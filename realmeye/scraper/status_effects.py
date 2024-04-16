import aiohttp
from urllib.parse import urljoin, quote
from realmeye.constants import routes, HTTPResponseError

async def fetch_status_effects_page(session: aiohttp.ClientSession) -> str:
    """Asynchronously retrieves the target guild's RealmEye page."""
    url = urljoin(routes.base_wiki_url, "status-effects")

    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            raise HTTPResponseError(f"Error: Received a non-200 response code ({response.status}).")