# choice-primitives

Core primitives for decision-making, optimization, and selection under constraints. This module equips the Spiral architecture with abstractions to represent choices, preferences, utilities, and policies in a domain-agnostic way.

## Purpose

- Model decisions with explicit objectives and constraints
- Support preference aggregation, utility functions, and policy evaluation
- Enable search, optimization, and exploration strategies

## Structure

- Primitives: Choice, Preference, Utility, Policy, ConstraintSet
- Solvers: greedy, dynamic programming, heuristic search, multi-objective
- Composition: sequential choices, concurrent choices, hierarchical policies

## Quick Start

```python
from choice_primitives import Choice, ConstraintSet, Utility, solve

# Define a choice problem
c = Choice(
    options=["A", "B", "C"],
    constraints=ConstraintSet(["cost <= 10", "risk <= 0.2"]),
    utility=Utility(lambda x: {"A": 5, "B": 8, "C": 6}[x])
)

# Solve with default solver
best = solve(c)
```

## Design Principles

- Choices are explicit, composable, and introspectable
- Constraints are first-class, with validation and explanation
- Utilities and preferences are pluggable and testable
- Support for uncertainty and stochastic outcomes

## Examples

1) Multi-objective decision with trade-offs
```python
from choice_primitives import Choice, ConstraintSet, Utility, solve

options = [
    {"name": "PlanA", "cost": 7, "impact": 0.6},
    {"name": "PlanB", "cost": 10, "impact": 0.8},
    {"name": "PlanC", "cost": 5, "impact": 0.4},
]

# Define utility with weighted objectives
weights = {"impact": 0.7, "cost": -0.3}

def u(opt):
    return weights["impact"] * opt["impact"] + weights["cost"] * opt["cost"]

c = Choice(options=options, constraints=ConstraintSet(["cost <= 10"]))
best = solve(c, utility=Utility(u))
```

2) Policy composition
```python
from choice_primitives import Policy

explore = Policy("explore", epsilon=0.1)
exploit = Policy("exploit")

composed = explore.then(exploit).repeat(10)
```

## Integration with Spiral Base

- Exposes solvers as transformations
- Validates constraints and utilities
- Composes with relation- and unit-primitives for grounded decisions

```python
from spiral_base import ModuleInterface
from choice_primitives import validators, solvers

class ChoiceModule(ModuleInterface):
    def register(self, system):
        system.add_validators(validators.all())
        system.add_transformations(solvers.all())
```

## Roadmap

- [ ] Multi-objective optimization with Pareto front operations
- [ ] Stochastic decision processes (MDP, POMDP) interfaces
- [ ] Preference learning and elicitation tools
- [ ] Constraint explanation and conflict resolution
- [ ] Benchmark suite and example gallery

## Contribution Guidelines

We welcome contributions from operations research, economics, AI/ML, HCI, and policy.

- Provide clear problem formulations and datasets (when relevant)
- Include solver performance notes and complexity discussion
- Add tests and small examples for each solver/primitive
- Document assumptions and failure modes

## Code Style and Testing

```python
from choice_primitives import Choice, solve

def test_choice_best_option():
    c = Choice(options=[1,2,3])
    best = solve(c, utility=lambda x: x)
    assert best == 3
```

## Cross-Disciplinary Invitation

- Operations research: algorithms and complexity
- Economists: utility and preference modeling
- AI/ML: learning policies and reward modeling
- HCI: human-in-the-loop decision systems

## License

MIT License
