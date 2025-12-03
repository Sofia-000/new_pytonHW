from address import Address
from mailing import Mailing

mailing = Mailing(5940950,
        Address("6869-394-1", "Полежайкино", "Пожарная ул.", "д. №69", "кв. 666"),
        Address("5553-53-5", "Бармалеево", "Водянки ул.", "д. №67", "кв. 44"),
        510)


print(mailing)
