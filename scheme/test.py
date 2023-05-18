from scheme import *
env = create_global_frame()
twos = Pair(2, Pair(2, nil))
plus = BuiltinProcedure(scheme_add) # + procedure
scheme_apply(plus, twos, env)