from scheme_reader import *
from scheme import *
expr = read_line('(+ 2 2)')
scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors