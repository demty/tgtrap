from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class ApplicationUser:
    user_id: int
    _id: int
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ApplicationUser":
        return cls(
            _id=data.get("_id"),
            user_id=data.get("id"),
            username=data.get("username"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
        )

    @classmethod
    def from_mongo_dict(cls, data: Dict[str, Any]):
        entity = cls.from_dict(data)
        entity.user_id = data.get('user_id')
        return entity
