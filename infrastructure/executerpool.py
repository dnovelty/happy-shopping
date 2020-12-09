
from concurrent import futures
from concurrent.futures.process import ProcessPoolExecutor
from typing import Any, Callable, TypeVar
 


processingPool = ProcessPoolExecutor().submit
_T = TypeVar("_T")

class ProcessingPool(ProcessPoolExecutor):
    def submit(self, fn, *args, **kwargs):
        with self:
          return super().submit(fn, *args, **kwargs)
