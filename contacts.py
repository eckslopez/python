contacts = {
    'number': 4,
    'students':
        [
            {'name':'Vanessa D. Lopez', 'email':'vanedelo@gmail.com'},
            {'name':'Adrian G. Lopez', 'email':'alo792@yahoo.com'},
            {'name':'Ghizelle A. Lopez', 'email':'ghizellelopez@gmail.com'},
            {'name':'Jhadinne M. Lopez', 'email':'jhadinnelopez@gmail.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])

print('Student names:')
for name in contacts['students']:
    print(student['name'])