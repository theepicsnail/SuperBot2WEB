from Hook import *
@requires("bar")
@prefers("foobar")
class SamplePlugin:
    @bindFunction():
    def foo(self):pass
