class SimpleCategoriser:    def evaluate(self, width, height):        if width < 750 or height < 750 or (width + height) <= 1150:            return 1        if width < 750 or height < 750 or (width + height) > 1150:            return 2        if 750 <= width < 1350 or 750 <= height < 1350:            return 3        if 1350 <= width < 2100 or 1350 <= height < 2100:            return 4        if width >= 2100 or height >= 2100:            return 5        return -1