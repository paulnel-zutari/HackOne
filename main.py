import pandas as pdimport csvimport osfrom src.categoriser import SimpleCategoriserfrom src.filters import RowFilter, ColoumnFilterfrom src.transformations import Transformationsfrom src.item import Itemdef get_data(path):    return pd.read_csv(path)def filter_data(data):    col_filter = ColoumnFilter()    row_filter = RowFilter()    data = col_filter.filter(data)    data = row_filter.filter(data, insulation_none=False)    return datadef transform_data(data):    transformer = Transformations()    data = transformer.add_count_coloumn(data)    # data = transformer.clean_column_headers(data)    return datadef save_boq(boq: dict, path):    header = ['category', 'quantity', 'rate', 'amount']    with open(path, 'w', newline='') as boq_file:        writer = csv.writer(boq_file)        writer.writerow(header)        for category, quantity in boq.items():            rate = 1            item_content = [category, quantity, rate, rate*quantity]            writer.writerow(item_content)if __name__ == "__main__":    source_path = r"data\Duct Schedule Low Pressure Insulated Cladded Rect.csv"    output_file = os.path.basename(source_path).split('.')[0]    csv_output_path = f"outputs/csv/BOQ_{output_file}.csv"    boq_data = get_data(source_path)    boq_data = filter_data(boq_data)    boq_data = transform_data(boq_data)    boq = [        Item(row["Size"], row["Count"], row["Area"], row["Surface Area"], SimpleCategoriser())        for _, row in boq_data.iterrows()    ]    for item in boq:        print(f'size: {item.size}, width: {item.width}, height: {item.height}, cat: {item.category}')    summarised_boq = {}    for item in boq:        summarised_boq.setdefault(item.category, 0)        summarised_boq[item.category] += item.count * item.boq_area    save_boq(summarised_boq, csv_output_path)    print(summarised_boq)