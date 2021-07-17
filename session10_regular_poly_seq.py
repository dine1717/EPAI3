# regular_poly_seq.py

import Session10 as rp
from functools import lru_cache

"""Regular Polygon Sequence class"""
class RegularPolySeq:
    """Class to create a sequence of regular polygon"""

    def __init__(self, vert_count, radius):
        """Initialize the RegulaPoly class attributes"""

        self.vert_count = vert_count # Number of vertices of polygon
        self.radius     = radius # Circumradius

    @property
    def vert_count(self):
        """Get count of vertices"""
        return self._vert_count

    @vert_count.setter
    def vert_count(self, vert_count):
        """Set the number of vertices of polygon"""
        if not isinstance(vert_count, int):
            raise TypeError(f'Number of vertices should be of type integer')
        if vert_count < 3:
            raise ValueError(f'Number of vertices should be greater than or equal to 3')

        self._vert_count = vert_count

    @property
    def radius(self):
        """Get circumradius"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Set the circumradius of polygon"""
        if not isinstance(radius, int):
            raise TypeError(f'Radius should be of type integer')
        if radius < 0:
            raise ValueError(f'Radius should be greater than 0')

        self._radius = radius

    def __getitem__(self, seq):
        """get next item in the sequence"""
        if isinstance(seq, int):
            seq = seq + 3
            if seq - 3 < 0:
                seq = self.vert_count + seq - 3
            if seq  < 3 or seq > self.vert_count:
                raise IndexError
            else:
                if seq >=3:
                    return RegularPolySeq._seq(seq, self.radius)
        else:
            raise TypeError ('Please provide valid integer value')

    def __len__(self):
        """get length of sequence"""
        return self.vert_count - 2

    def __str__(self):
        """String represnetation"""
        return f"Polygon sequence with seq_len = {self.vert_count - 2} and common cirum_radius = {self.radius}"

    def __repr__(self):
        """ Return string for RegularPolySeq"""
        return (f'RegularPolySeq({self.vert_count}, {self.radius})')

    @property
    def max_efficiency_poly(self):
        """ find the max efficiency polygon """
        max_ratio = -100
        for i in range(self.vert_count-2):
            area_perimeter_ratio = self.__getitem__(i)[1]
            if area_perimeter_ratio > max_ratio:
                max_ratio = area_perimeter_ratio
                max_ratio_polygon = self.__getitem__(i)[0]
        return max_ratio_polygon

    @staticmethod
    @lru_cache(2 ** 10)
    def _seq(seq,radius):
        if seq < 3:
            return None
        else:
            poly = rp.RegularPoly(seq,radius)
            return poly , poly.area/poly.perimeter