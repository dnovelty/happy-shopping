import threading


def largeFibonnaciNumber():
    """
    Represent a long running blocking function by calculating
    the TARGETth Fibonnaci number
    """
    TARGET = 10000

    first = 0
    second = 1
    print('【订单线程[%s]】55555===================================================================='
          % threading.currentThread().ident)
    for i in range(TARGET - 1):
        new = first + second
        first = second
        second = new

    return second


from twisted.internet import threads, reactor


def fibonacciCallback(result):
    """
    Callback which manages the largeFibonnaciNumber result by
    printing it out
    """
    print('【订单线程[%s]】44444===================================================================='
          % threading.currentThread().ident)
    print("largeFibonnaciNumber result =", result)
    # make sure the reactor stops after the callback chain finishes,
    # just so that this example terminates
    reactor.stop()


def run():
    """
    Run a series of operations, deferring the largeFibonnaciNumber
    operation to a thread and performing some other operations after
    adding the callback
    """
    print('【订单线程[%s]】11111===================================================================='
          % threading.currentThread().ident)
    # get our Deferred which will be called with the largeFibonnaciNumber result
    d = threads.deferToThread(largeFibonnaciNumber)
    print('【订单线程[%s]】22222===================================================================='
          % threading.currentThread().ident)
    # add our callback to print it out
    d.addCallback(fibonacciCallback)
    print('【订单线程[%s]】33333===================================================================='
          % threading.currentThread().ident)
    print("1st line after the addition of the callback")
    print("2nd line after the addition of the callback")


if __name__ == '__main__':
    run()
    reactor.run()
