# -*- coding: utf-8 -*-
from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field

from __shared.domain.entities import Entity


@dataclass(kw_only=True, frozen=True, slots=True)
class User(Entity):

    name: str
    birth_date: datetime
    updated_at: Optional[datetime]
    created_at: Optional[datetime] = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.created_at:
            self._set("created_at", datetime.now())
