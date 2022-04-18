from ortools.sat.python import cp_model


model = cp_model.CpModel()
def BooleanProductSampleSat():
    """Encoding of the product of two Boolean variables.

    p == x * y, which is the same as p <=> x and y
    """
    x = model.NewBoolVar('x')
    y = model.NewBoolVar('y')
    z = model.NewBoolVar('z')


    def _and(*vars, negated=False):
        tmp = model.NewBoolVar('p')
        model.AddBoolOr(
            [v.Not() if not negated else v for v in vars] + [tmp]
        )
        for v in vars:
            model.AddImplication(tmp, v if not negated else v.Not())
        return tmp

    p = _and(x, y, z)

    # Create a solver and solve.
    solver = cp_model.CpSolver()
    solution_printer = cp_model.VarArraySolutionPrinter([x, y, z, p])
    solver.parameters.enumerate_all_solutions = True
    solver.Solve(model, solution_printer)

BooleanProductSampleSat()
