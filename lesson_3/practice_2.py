def print_data(name, surname, birthday, city, email, phone):
    return f'Имя - {name}, фамилия - {surname}, дата рождения - {birthday}, город проживания - {city},' \
           f'email - {email}, телефон - {phone}'


print(print_data(name='Виктор', surname='Савенков', birthday='1994', city='Саратов', email='vicsavenkov@gmail.com',
                 phone='8-800-355-35-35'))
