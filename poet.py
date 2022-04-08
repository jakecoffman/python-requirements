from poetry.core.packages.dependency import Dependency
from poetry.core.semver.version import Version
from poetry.core.version.requirements import Requirement, InvalidRequirement

try:
    Dependency.create_from_pep_508("dummy^1")
except InvalidRequirement:
    pass
else:
    assert False

d = Dependency("dummy", "^1")
assert str(d.constraint) == ">=1,<2", d.constraint

# doesn't parse, falls back to *
assert str(Dependency("dummy", "(>=20.4.3,<20.4.5||>=20.4.7)").constraint) == "*"

d = Dependency.create_from_pep_508("dummy(>=20.4.3,<20.4.5||>=20.4.7)")
assert str(d.constraint) == ">=20.4.3,<20.4.5 || >=20.4.7", str(d.constraint)

assert d.constraint.allows(Version.parse("20.4.3"))
assert d.constraint.allows(Version.parse("20.4.4"))
assert not d.constraint.allows(Version.parse("20.4.5"))
assert not d.constraint.allows(Version.parse("20.4.6"))
assert d.constraint.allows(Version.parse("20.4.7"))
