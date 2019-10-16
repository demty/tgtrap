from dataclasses import asdict
from typing import Any, Dict, Optional

import motor.motor_asyncio
from pymongo.collection import Collection


from tgtrap.entities import ApplicationUser


class Trap:
    states = []
    init_state = None

    def __init__(self, mongo_cs: str, mongo_db: str):
        self.users_collection: Collection = motor.motor_asyncio.AsyncIOMotorClient(mongo_cs)[mongo_db]['users']

    async def create_user(self, user_data: Dict[str, Any]) -> ApplicationUser:
        user = ApplicationUser.from_dict(user_data)
        user_data = asdict(user)
        user_data.pop('_id', None)
        res = await self.users_collection.insert_one(user_data)
        user._id = str(res.inserted_id)
        return user

    async def get_user(self, user_id: int) -> Optional[ApplicationUser]:
        found_user = await self.users_collection.find_one({'user_id': user_id})
        if not found_user:
            return None
        return ApplicationUser.from_mongo_dict(found_user)

    async def process_message(self, message: Dict[str, Any]):
        user = await self.get_user(message['from']['id'])
        if not user:
            user = await self.create_user(message['from'])
        pass

    async def process_inline(self):
        pass
