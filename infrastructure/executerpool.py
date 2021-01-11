
from concurrent import futures
from concurrent.futures.process import ProcessPoolExecutor 
from concurrent.futures import ThreadPoolExecutor

 




class ProcessingPool(ProcessPoolExecutor):
    def submit(self, fn, *args, **kwargs):
        with self:
          return super().submit(fn, *args, **kwargs)

processingPool = ProcessingPool()


class ThreadingPool(ThreadPoolExecutor):
    def submit(self, fn, *args, **kwargs):
        with self:
          return super().submit(fn, *args, **kwargs)

threadingPool = ThreadingPool(max_workers=20)