import sys

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        operator = scheme_eval(first, env)  # Evaluate the operator
        operands = rest.map(lambda operand: scheme_eval(operand, env))  # Evaluate the operands
        return scheme_apply(operator, operands,env)  # Apply the operator to the operands
# You'll have to recursively call scheme_eval in the first two steps. 
# Here are some other functions/methods you should use:

# The map method of Pair returns a new Scheme list 
# constructed by applying a one-argument function to every item in a Scheme list.
# The scheme_apply function applies a Scheme procedure to arguments represented 
# as a Scheme list (a Pair instance or nil).
#Implement the missing part of scheme_eval, which evaluates a call expression. To evaluate a call expression:

#Evaluate the operator (which should evaluate to a Procedure instance).
#Evaluate all of the operands and collect the results (the argument values) in a Scheme list.
#Return the result of calling scheme_apply on this Procedure and these argument values.

def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
       assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):
        # Call the Python function that implements the built-in procedure
        args_= []
        while args is not nil:
            args_.append(args.first)
            args = args.rest
        if procedure.need_env:
            args_.append(env)
        try:
            return procedure.py_func(*args_)
        except TypeError as err:
            raise SchemeError('incorrect number of arguments: {0}'.format(procedure))        
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    return scheme_eval(expressions.first, env)  # replace this with lines of your own code
    # END PROBLEM 6


class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val
