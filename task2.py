class Road:
    def __init__(self, length, width):
        self._length = length   # m
        self._width = width     # m

    def calc_asphalt(self, thickness, dim_thickness, density_av=2400):
        # density_av = 2400
        # dim_density_av = 'kg/m^3'
        if dim_thickness == 'mm':
            thickness /= 1000
        elif dim_thickness == 'cm':
            thickness /= 100
        elif dim_thickness == 'm':
            thickness = thickness
        v_asphalt = self._length * self._width * thickness
        m_asphalt = (v_asphalt * density_av)/1000

        return f'{m_asphalt} t'


interstate_60 = Road(1000000, 9)
print(interstate_60.calc_asphalt(15, 'cm'))
