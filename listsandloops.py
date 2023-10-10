acronyms = ['LOL', 'TBH', 'BRB', 'SMH', 'IDK']
acronyms.append('WTH')
acronyms.append('IMHO')
acronyms.append('NONSENSE')
acronyms.remove('NONSENSE')
acronyms.append('NONSENSE')
del acronyms[7]

print(acronyms)

if 'SMH' in acronyms:
    print('True')

for acronym in acronyms:
    print(acronym)