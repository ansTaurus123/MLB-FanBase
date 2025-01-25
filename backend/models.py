from pydantic import BaseModel
from typing import List

class UserPreference(BaseModel):
    user_id: str
    favorite_teams: List[str]
    favorite_players: List[str]
