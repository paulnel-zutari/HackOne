class HvacRectangularCategoriser:    def evaluate(self, width, height):        """        Determine category based on width and height        :param width: With of item        :param height: Height of item        :return:        """        if max(width, height) >= 2100:            return 5        if 1350 <= max(width, height) < 2100:            return 4        if 750 <= max(width, height) < 1350:            return 3        if max(width, height) < 750 and (width + height) > 1150:            return 2        if max(width, width) < 750 and (width + height) <= 1150:            return 1        return 0