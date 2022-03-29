from packaging.version import Version, parse
from itertools import combinations

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
    "1.0.0.post",
    "1.post2",
    "1.0.0.post11",
    "1.0.1",
    "1.0.11",
    "2016.1",
    "1!0.1.0",
    "2!0.1.0",
    "10!0.1.0"
]

for [lhs, rhs] in combinations(sorted_versions, 2):
    assert parse(lhs) < parse(rhs), "%s < %s" % (lhs, rhs)
    assert parse(rhs) > parse(lhs)
