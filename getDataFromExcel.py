from pandas import read_excel as read

def get_XLSX_Data (filename,sheet,dataset):

    usercolumns  =list(dataset.keys())

    data = read(f'data/{filename}.xlsx', sheet_name=sheet,engine='openpyxl',usecols = usercolumns, dtype = dataset) 
    
    # data.dropna(inplace = True)        # removing null values to avoid errors 

    output = {}

    for column in usercolumns:
        output[column] = data[column].to_list()

    return (output)
