# TODO Найдите количество книг, которое можно разместить на дискете
info_volume_floppy = 1.44  # Информационный объем дискеты в Мб
num_pages_book = 100  # Количество страниц в книге
num_lines_per_page = 50  # Число строк на странице
num_chars_per_line = 25  # Количество символов в строке
bytes_per_char = 4  # Для хранения кода одного символа нужно 4 байта
kilobytes = 1024 # Килобайт 1024 байта
megobytes = 1024 # Мегабайт 1024 килобайта
simbols = num_pages_book * num_lines_per_page * num_chars_per_line * bytes_per_char
storage_mem = info_volume_floppy * megobytes * kilobytes
print("Количество книг, помещающихся на дискету:", int(storage_mem//simbols))
