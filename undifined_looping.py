book_count = 10
print('reading boook')
read_count = 0

understood_count = 0
print(f'sum book understood {understood_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f'number book - {understood_count + 1} dont understood')
    else:
        understood_count = understood_count + 1
        print(f'number book - {understood_count} understood')

print(f'understood book {understood_count}')
if understood_count == book_count:
    print('understanding')
else:
    print(f'number book dont understnding {understood_count}')




