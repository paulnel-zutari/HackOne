from src.item import Itemclass Boq:    def __init__(self, data, rates, categoriser):        self._rates = rates        self._categoriser = categoriser        self._items = [            Item(row["Size"], row["Count"], row["Area"], row["Surface Area"], self._categoriser())            for _, row in data.iterrows()        ]    def summary(self):        boq = {}        categories_quantity = self._get_quantities()        for category, quantity in categories_quantity.items():            rate = self._rates[category]            boq[category] = {'quantity': quantity, 'rate': rate, 'cost': quantity * rate}        total = sum(item['cost'] for item in boq.values())        boq['total'] = {'quantity': 0, 'rate': 0, 'cost': total}        return boq    def _get_quantities(self):        quantities = {}        for item in self._items:            quantities.setdefault(item.category, 0)            quantities[item.category] += item.count * item.boq_area        return quantities