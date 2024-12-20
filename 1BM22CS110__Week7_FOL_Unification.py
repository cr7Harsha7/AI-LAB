def unify(expr1, expr2):
    def is_variable(x):
        return isinstance(x, str) and x.islower()

    def occurs_check(var, expr):
        """Check if a variable occurs in the expression."""
        if var == expr:
            return True
        elif isinstance(expr, list):
            return any(occurs_check(var, sub_expr) for sub_expr in expr)
        return False

    def unify_internal(e1, e2, subst):
        """Recursive unification with a substitution set."""
        if e1 == e2:  # Case 1: Identical
            return subst
        elif is_variable(e1):  # Case 2: e1 is a variable
            if occurs_check(e1, e2):
                return None  # Occurs check failure
            subst[e1] = e2
            return {k: substitute(v, subst) for k, v in subst.items()}
        elif is_variable(e2):  # Case 3: e2 is a variable
            if occurs_check(e2, e1):
                return None  # Occurs check failure
            subst[e2] = e1
            return {k: substitute(v, subst) for k, v in subst.items()}
        elif isinstance(e1, list) and isinstance(e2, list):  # Case 4: Compound expressions
            if len(e1) != len(e2):
                return None
            for el1, el2 in zip(e1, e2):
                subst = unify_internal(el1, el2, subst)
                if subst is None:
                    return None
            return subst
        else:  # Case 5: Failure
            return None

    def substitute(expr, subst):
        """Apply substitution to the expression."""
        if isinstance(expr, str):
            return subst.get(expr, expr)
        elif isinstance(expr, list):
            return [substitute(e, subst) for e in expr]
        return expr

    # Start with an empty substitution set
    result = unify_internal(expr1, expr2, {})
    return result

if __name__ == "__main__":
    # Input expressions
    print("Enter the first expression (e.g., ['P', 'x', 'y']):")
    expr1 = eval(input())  # Take user input as a list
    print("Enter the second expression (e.g., ['P', 'a', 'b']):")
    expr2 = eval(input())

    # Perform unification
    result = unify(expr1, expr2)

    # Output result
    if result is None:
        print("Unification failed.")
    else:
        print("Unification successful. Substitution set:", result)
