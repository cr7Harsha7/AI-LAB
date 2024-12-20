class ForwardChainingFOL:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, premises, conclusion):
        self.rules.append((premises, conclusion))

    def unify(self, fact1, fact2):

        if fact1 == fact2:
            return {}
        if "(" in fact1 and "(" in fact2:

            pred1, args1 = fact1.split("(", 1)
            pred2, args2 = fact2.split("(", 1)
            args1 = args1[:-1].split(",")
            args2 = args2[:-1].split(",")
            if pred1 != pred2 or len(args1) != len(args2):
                return None

            substitution = {}
            for a1, a2 in zip(args1, args2):
                if a1 != a2:
                    if a1.islower():
                        substitution[a1] = a2
                    elif a2.islower():
                        substitution[a2] = a1
                    else:
                        return None
            return substitution
        return None

    def apply_substitution(self, fact, substitution):

        if "(" in fact:
            pred, args = fact.split("(", 1)
            args = args[:-1].split(",")
            substituted_args = [substitution.get(arg, arg) for arg in args]
            return f"{pred}({','.join(substituted_args)})"
        return fact

    def forward_chain(self, goal):
        iteration = 1
        while True:
            new_facts = set()
            print(f"\n=== Iteration {iteration} ===")
            print("Known Facts:")
            for fact in self.facts:
                print(f"  - {fact}")

            print("\nApplying rules...")
            rule_triggered = False

            for premises, conclusion in self.rules:
                substitutions = [{}]
                for premise in premises:
                    new_substitutions = []
                    for fact in self.facts:
                        for sub in substitutions:
                            unified = self.unify(self.apply_substitution(premise, sub), fact)
                            if unified is not None:
                                new_substitutions.append({**sub, **unified})
                    substitutions = new_substitutions
                for sub in substitutions:
                    inferred_fact = self.apply_substitution(conclusion, sub)
                    if inferred_fact not in self.facts:
                        rule_triggered = True
                        print(f"Rule triggered: {premises} → {conclusion}")
                        print(f"  New fact inferred: {inferred_fact}")
                        new_facts.add(inferred_fact)

            if not new_facts:
                if not rule_triggered:
                    print("No rules triggered in this iteration.")
                print("No new facts inferred in this iteration.")
                break

            self.facts.update(new_facts)
            if goal in self.facts:
                print(f"\nGoal {goal} reached!")
                return True
            iteration += 1

        print("\nGoal not reached.")
        return False


fc = ForwardChainingFOL()

fc.add_fact("American(Robert)")
fc.add_fact("Enemy(A,America)")
fc.add_fact("Owns(A,T1)")
fc.add_fact("Missile(T1)")

fc.add_rule(["Missile(T1)"], "Weapon(T1)")
fc.add_rule(["Enemy(A,America)"], "Hostile(A)")
fc.add_rule(["Missile(p)", "Owns(A,p)"], "Sells(Robert,p,A)")
fc.add_rule(["American(p)", "Weapon(q)", "Sells(p,q,r)", "Hostile(r)"], "Criminal(p)")

goal = "Criminal(Robert)"

if fc.forward_chain(goal):
    print(f"\nFinal result: Goal achieved: {goal}")
else:
    print("\nFinal result: Goal not achieved.")
