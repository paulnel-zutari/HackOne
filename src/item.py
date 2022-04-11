import reclass Item:    def __init__(self, size: str, count: str, area: str, surface_area: str, categoriser):        """        Implements an Item object        :param size: String specifying the size of an item (eg: '200x340-350x200')        :param count: Quantity of item        :param area: Area of item        :param surface_area: Surface Area of item        :param categoriser: Instance of Categoriser class for categorising items based on size        """        self._size = size        self._count = count        self._area = area        self._surface_area = surface_area        self._categoriser = categoriser    @property    def category(self):        """        :return: Category of item        """        # Polymorphism        return self._categoriser.evaluate(self.width, self.height)    @property    def width(self):        """        :return: Minimum of all widths in item size        """        return min([int(item[0]) for item in self.size])    @property    def height(self):        """        :return: Minimum of all heights in item size        """        return min([int(item[1]) for item in self.size])    @property    def area(self):        """        :return: Area as float if attribute exists else 0        """        search = re.findall(r'(\d+.\d*)', str(self._area))        if len(search) != 0:            return float(search[0])        return 0    @property    def size(self):        """        :return: List of tuples of sizes (eg: [('200','340'), ('350','200')]. ('0','0') if size is None.        """        if self._size is not None:            sizes = [tuple(size.split('x')) for size in self._get_sizes()]            return self._verified(sizes)        return '0', '0'    def _verified(self, sizes):        for size in sizes:            if len(size) != 2:                raise ValueError("Invalid size string provided.")        return sizes    def _get_sizes(self):        if self._size is not None:            sizes = self._size.split('-')            return sizes        return '0', '0'    @property    def surface_area(self):        """        :return: Surface Area as float if attribute exists else 0        """        if self.width > 0 and self.height > 0:            search = re.findall(r'(\d+.\d*)', str(self._surface_area))            if len(search) != 0:                return float(search[0])        return 0    @property    def count(self):        """        :return: Count of item as integer        """        return 1        # return int(self._count)    @property    def boq_area(self):        """        :return: Maximum of Area and Surface Area        """        return max(self.area, self.surface_area)