class Clause:
    def __init__(self, literals):
        self.literals = set(literals)

    def __repr__(self):
        return " ∨ ".join(sorted(self.literals))

    def resolve(self, other):
        resolvents = []
        for literal in self.literals:
            negated_literal = f"¬{literal}" if not literal.startswith('¬') else literal[1:]
            if negated_literal in other.literals:
                new_literals = (self.literals - {literal}) | (other.literals - {negated_literal})
                resolvents.append(Clause(new_literals))
        return resolvents


def resolution(clauses, query):
    negated_query = Clause([f"¬{query}"])
    clauses.append(negated_query)

    new = set()
    seen_pairs = set()

    while True:
        pairs = [(clauses[i], clauses[j]) for i in range(len(clauses)) for j in range(i + 1, len(clauses))]
        for ci, cj in pairs:
            if (ci, cj) in seen_pairs or (cj, ci) in seen_pairs:
                continue
            seen_pairs.add((ci, cj))

            resolvents = ci.resolve(cj)
            for resolvent in resolvents:
                if not resolvent.literals:
                    return True
                new.add(frozenset(resolvent.literals))

        if new.issubset(set(map(frozenset, (c.literals for c in clauses)))):
            return False
        clauses.extend(Clause(list(literals)) for literals in new - set(map(frozenset, (c.literals for c in clauses))))
        new.clear()


KB = [
    Clause(["¬Food(Peanuts)", "Likes(John, Peanuts)"]),  # John likes all kinds of food
    Clause(["Food(Apple)"]),
    Clause(["Food(Vegetables)"]),
    Clause(["Food(Peanuts)"]),  # Explicit Peanuts as Food
    Clause(["¬Eats(Anil, Peanuts)", "Food(Peanuts)"]),
    Clause(["Eats(Anil, Peanuts)"]),  # Anil eats peanuts
    Clause(["Alive(Anil)"]),           # Anil is alive
    Clause(["¬Alive(Anil)", "¬Killed(Anil)"]),  # Alive -> Not Killed
    Clause(["Killed(Anil)", "Alive(Anil)"])     # Not Killed -> Alive
]

# Query: John likes peanuts
query = "Likes(John, Peanuts)"

# Run the resolution algorithm
if resolution(KB, query):
    print(f"The conclusion '{query}' is proven by resolution.")
else:
    print(f"The conclusion '{query}' cannot be proven.")
