import logging

MIN_THICKNESS = 1
MAX_THICKNESS = 5


class CheeseSlicer:

    def __init__(self, thickness=3):
        """"""
        self._logger = logging.getLogger(__name__)
        self._thickness = thickness
        self._logger.info('CheeseSlicer ready')

    @property
    def thickness(self):
        self._logger.debug('get thickness')
        return self._thickness

    @thickness.setter
    def thickness(self, value):
        if not isinstance(value, int):
            self._logger.error('invalid input for thicknes: {}'.format(value))
            return
        if value < MIN_THICKNESS:
            self._logger.debug('to thin, set to: {}'.format(MIN_THICKNESS))
            self._thickness = MIN_THICKNESS
        elif value > MAX_THICKNESS:
            self._logger.debug('to thick, set to: {}'.format(MAX_THICKNESS))
            self._thickness = MAX_THICKNESS
        else:
            self._logger.debug('set thickness to: {}'.format(value))
            self._thickness = value

    def slice(self, cheese):
        """slice the cheese"""
        slice_thickness = ' ' * self._thickness
        sliced_cheese = ['{}{}{}'.format(slice_thickness, slice, slice_thickness) for slice in cheese]
        return '/'.join(list(sliced_cheese))
