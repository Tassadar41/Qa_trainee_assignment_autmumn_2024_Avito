from pydantic import BaseModel, field_validator
from datetime import datetime
from uuid import UUID

class Statistics(BaseModel):
    contacts: int
    likes: int
    viewCount: int

class Post(BaseModel):
    createdAt: datetime
    id: UUID
    name: str
    price: int
    sellerId: int
    statistics: Statistics

    # Валидатор для обработки неправильного формата даты
    @field_validator('createdAt', mode='before')
    def fix_datetime(cls, value):
        # Удаление лишнего дублированного часового пояса
        if isinstance(value, str):
            value = value.split(" +")[0]  # Убираем лишнюю информацию о часовом поясе
        return datetime.fromisoformat(value)


