from chaine import *

assert 11::3::7::5::12::().take(1) == 11::()
assert 11::3::7::5::12::().take(2) == 11::3::()
assert 11::3::7::5::12::().take(3) == 11::3::7::()
assert 11::3::7::5::12::().take(7) == 11::3::7::5::12::()