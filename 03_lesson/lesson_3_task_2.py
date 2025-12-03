from smartphone import Smartphone

catalog = [
    Smartphone("Iphone", "17", "+7-990-111-11-11"),
    Smartphone("Samsung", "A19", "+7-990-222-22-22"),
    Smartphone("Xaomi", "100 Pro", "+7-990-333-33-33"),
    Smartphone("Huawei", "30 AI", "+7-990-444-44-44"),
    Smartphone("Google Phone", "2", "+7-990-555-55-55")]

for smartphone in catalog:
    print(f"{smartphone.say_brand(),
             smartphone.say_model(),
             smartphone.say_number()}")
