from cats import feline_fixes, autocorrect
import tests.construct_check as test
# Check that the recursion stops when the limit is reached
import trace, io
from contextlib import redirect_stdout
with io.StringIO() as buf, redirect_stdout(buf):
    trace.Trace(trace=True).runfunc(feline_fixes, "someaweqwertyuio",
                                    "awesomeasdfghjkl", 3)
    output = buf.getvalue()
len([line for line in output.split('\n') if 'funcname' in line]) < 10
