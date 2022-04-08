import osfrom src.boq import Boqfrom src.hvac_rectangular_categoriser import HvacRectangularCategoriserfrom src.file_handler import FileHandlerif __name__ == "__main__":    SOURCE_DIR = 'data/'    DESTINATION_DIR = 'outputs/csv/'    RATES = {1: 1, 2: 2.5, 3: 4, 4: 5, 5: 6}    handler = FileHandler()    input_files = os.listdir(SOURCE_DIR)    for input_file in input_files:        source = fr'{SOURCE_DIR}{input_file}'        data = handler.load(source)        boq = Boq(data=data, rates=RATES, categoriser=HvacRectangularCategoriser)        summary = boq.summary()        output_file = os.path.basename(source).split('.')[0]        handler.save(summary, f'{DESTINATION_DIR}BOQ_{output_file}.csv')        print(summary)