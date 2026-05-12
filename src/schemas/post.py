from datetime import UTC, datetime

from pydantic import BaseModel


class PostIn(BaseModel):
    title : str
    content : str
    published_at: datetime | None = None
    date : datetime = datetime.now(UTC)
    published : bool = False