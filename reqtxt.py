from packaging.version import parse
from packaging.requirements import Requirement, InvalidRequirement
from itertools import combinations

r = Requirement("virtualenv(>=20.4.3,<20.4.5||>=20.4.7)")
# not what the user intended
assert "20.4.5" in r.specifier
# interesting
assert "20.4.8" not in r.specifier
# rewrote it without parens and in a different order
assert "<20.4.5||>=20.4.7,>=20.4.3" == r.specifier, r.specifier

# defaults to *
assert "1" in Requirement("dummy").specifier

try:
    # ^ is not supported
    "1.2.3" in Requirement("dummy^1.2.1").specifier
except InvalidRequirement as e:
    pass
else:
    assert False

sorted_versions = [
    "",
    "0.9",
    "1.0.0-alpha",
    "1.0.0-alpha.1",
    "1.0.0-beta",
    "1.0.0-beta.2",
    "1.0.0-beta.11",
    "1.0.0-rc.1",
    "1",
    "1.0.0+gc1",
    "1.0.0.post",
    "1.post2",
    "1.post2+gc1",
    "1.0.0.post11",
    "1.0.1",
    "1.0.11",
    "2016.1",
    "1!0.1.0",
    "2!0.1.0",
    "10!0.1.0"
]

for [lhs, rhs] in combinations(sorted_versions, 2):
    assert parse(lhs) < parse(rhs)
    assert parse(rhs) > parse(lhs)

assert parse('0.5.4-alpha') == parse('0.5.4a')

pep = [
    '1.dev0',
    '1.0.dev456',
    '1.0a1',
    '1.0a2.dev456',
    '1.0a12.dev456',
    '1.0a12',
    '1.0b1.dev456',
    '1.0b2',
    '1.0b2.post345.dev456',
    '1.0b2.post345',
    '1.0rc1.dev456',
    '1.0rc1',
    '1.0',
    '1.0+abc.5',
    '1.0+abc.7',
    '1.0+5',
    '1.0.post456.dev34',
    '1.0.post456',
    '1.0.15',
    '1.1.dev1',
]

for [lhs, rhs] in combinations(pep, 2):
    assert parse(lhs) < parse(rhs)
    assert parse(rhs) > parse(lhs)
