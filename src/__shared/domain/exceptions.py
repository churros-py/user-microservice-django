# -*- coding: utf-8 -*-
class InvalidObjectIdException(Exception):
    def __init__(
        self, error="ID must be a valid ObjectId"
    ) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(error)


class ValidationException(Exception):
    pass


class NotFoundException(Exception):
    pass
