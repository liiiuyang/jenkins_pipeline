from faker import Faker

fake = Faker('zh-CN')

fake_name = fake.name()
fake_mail = fake.email()
fake_address = fake.address()

print("Name:", fake_name)
print("Email:", fake_mail)
print("Address:", fake_address)
