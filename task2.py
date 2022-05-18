class Road:
    _length = 1000000
    _width = 9

    def calc_asphalt(self, thickness=8, dim_thickness='cm'):
        density_av = 2400
        # dim_density_av = 'kg/m^3'
        if dim_thickness == 'mm':
            thickness /= 1000
        elif dim_thickness == 'cm':
            thickness /= 100
        v_asphalt = self._length * self._width * thickness
        m_asphalt = (v_asphalt * density_av)/1000

        return f'{m_asphalt} t'


interstate_60 = Road()
print(interstate_60.calc_asphalt(15, 'cm'), )
