from matchers import And, PlaysIn, HasAtLeast, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher = matcher

    def plays_in(self, team):
        return QueryBuilder(PlaysIn(team))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))
    
    def one_of(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self._matcher
