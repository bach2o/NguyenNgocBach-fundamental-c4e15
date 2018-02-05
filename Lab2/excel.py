import pyexcel

a_list_of_dictionaries = [
    {
        'title': 'hay',
        'link': 'https://google.com.vn'
    },
    {
        'title': 'hay-2',
        'link': 'https://google.com.vn'
    },
    {
        'title': 'hay-3',
        'link': 'https://google.com.vn'
    },
]

pyexcel.save_as( records = a_list_of_dictionaries, dest_file_name = 'excel.xlsx')
