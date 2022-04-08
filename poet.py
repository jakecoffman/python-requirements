from poetry.core.semver import parse_constraint, ParseConstraintError

assert str(parse_constraint("^1")) == ">=1,<2"

try:
    parse_constraint("(>=20.4.3,<20.4.5||>=20.4.7)")
except ParseConstraintError as e:
    pass
else:
    assert False
