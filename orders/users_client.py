import httpx
import os

class UsersClient:
    BASE_URL = os.getenv("USERS_SERVICE_URL", "http://localhost:8001")

    async def get_user(self, user_id: str):
        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(f"{self.BASE_URL}/users/{user_id}")
                if r.status_code == 200:
                    return r.json()
                return None
        except Exception:
            return None
