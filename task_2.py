def user_info_greetings(first_name, second_name, year_of_birth, city, email, phone):
    print((f'Добрый день, {first_name} {second_name}, {year_of_birth} года рождения из {city}. '
           f'Адрес электронной почты: {email}. '
           f'Номер телефона: {phone}.'))


user_info_greetings(year_of_birth=1978,
                    email='abc@mailhost.com',
                    phone='+(067)4563243',
                    city='Colombo',
                    first_name='Dominic',
                    second_name='Alexander')
