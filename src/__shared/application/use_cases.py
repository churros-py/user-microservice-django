# -*- coding: utf-8 -*-
import abc
from abc import ABC
from typing import Generic, TypeVar

Input = TypeVar("Input")
Output = TypeVar("Output")


class UseCase(Generic[Input, Output], ABC):
    @abc.abstractmethod
    def execute(self, input_param: Input) -> Output:
        raise NotImplementedError()
