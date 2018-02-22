import pdftables_api

def convert():
    c = pdftables_api.Client('gl90e7km93le')
    c.xlsx('materials/file.pdf', 'output.xlsx')
    file_obj = open('output.xlsx', 'rb')
    return file_obj
