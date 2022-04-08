from poetry.core.packages.dependency import Dependency
from poetry.core.semver.version import Version
from poetry.core.version.requirements import Requirement

d = Dependency("dummy", "^1")
# d = Dependency.create_from_pep_508("dummy^1") doesn't work
assert str(d.constraint) == ">=1,<2", d.constraint

d = Dependency.create_from_pep_508("dummy(>=20.4.3,<20.4.5||>=20.4.7)")
# d = Dependency("dummy", "(>=20.4.3,<20.4.5||>=20.4.7)") this results in * which is a fallback
print(d.constraint)

assert d.constraint.allows(Version.parse("20.4.3"))
assert d.constraint.allows(Version.parse("20.4.4"))
assert not d.constraint.allows(Version.parse("20.4.5"))
assert not d.constraint.allows(Version.parse("20.4.6"))
assert d.constraint.allows(Version.parse("20.4.7"))
