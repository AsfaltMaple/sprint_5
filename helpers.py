import faker

def registration_data():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    return email, password
    

def adv_info():
    fake = faker.Faker()
    adv_name = fake.catch_phrase()
    adv_description = fake.text()
    adv_price = fake.random_int(min =1, max= 9999999999)

    return adv_name, adv_description, adv_price
