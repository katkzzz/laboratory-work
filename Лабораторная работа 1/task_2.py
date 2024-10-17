# TODO Найдите количество книг, которое можно разместить на дискете
disk_mb = 1.44
pages = 100
lines_page = 50
chars_line = 25
bytes_char = 4

kb_to_byte = 1024
mb_to_kb = 1024

disk_bytes = disk_mb * kb_to_byte * mb_to_kb
total_chars = pages * lines_page * chars_line
book_bytes = total_chars * bytes_char

books_on_disk = int(disk_bytes // book_bytes)

print("Количество книг, помещающихся на дискету:", books_on_disk)
