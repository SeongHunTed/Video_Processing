import ch03.header_area as mod
from ch03.header_area import write

mod.say()
ret = mod.calc_area(type=1, a=5, b=5)
write(ret[0], ret[1])