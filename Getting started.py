from astropy.constants import G
print(G)

print(       )

from astropy import constants as const
print(const.c)

print(       )
print('Change Unity, m/s -> km/s')
print('c = ', const.c.to('km/s'))

print(    )
print('Change Unity, m/s -> pc/yr')
print('c = ', const.c.to('pc/yr'))
