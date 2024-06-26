import aiohttp
from typing import Optional
from realmeye.scraper import fetch_player_page, fetch_guild_page, fetch_status_effects_page
from realmeye.parser import parse_player_data, parse_guild_data, parse_status_effects
from realmeye.models import Player, Guild, StatusEffect
from realmeye.constants import ScraperError, ParserError
import logging

async def get_player_data(username: str, session: Optional[aiohttp.ClientSession] = None) -> Optional[Player]:
    """Returns a Player object if found, otherwise returns None."""
    try:
        async with session or aiohttp.ClientSession() as session:
            html_data = await fetch_player_page(username, session)
            player = parse_player_data(html_data)
            return player
    except (ScraperError, ParserError) as e:
        logging.error(f"Error fetching player data: {e}")
        return None

async def get_guild_data(guild_name: str, session: Optional[aiohttp.ClientSession] = None) -> Optional[Guild]:
    """Returns a Guild object if found, otherwise returns None."""
    try:
        async with session or aiohttp.ClientSession() as session:
            html_data = await fetch_guild_page(guild_name, session)
            guild = parse_guild_data(html_data)
            return guild
    except (ScraperError, ParserError) as e:
        logging.error(f"Error fetching guild data: {e}")
        return None
    
async def get_status_effects(status_effect_name: str, session: Optional[aiohttp.ClientSession] = None) -> Optional[StatusEffect]:
    """Returns a StatusEffect object if found, otherwise returns None."""
    try: 
        async with session or aiohttp.ClientSession() as session:
            html_data = await fetch_status_effects_page(session)
            status_effect = parse_status_effects(html_data)
            return status_effect
    except (ScraperError, ParserError) as e:
        logging.error(f"Error fetching status effect data: {e}")
        return None
