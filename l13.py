from custom_classes import *

ElectronicDevice1 = ElectronicDevice("Apple", "iPhone 6")

print(ElectronicDevice1.brand)
print(ElectronicDevice1.model)
print(ElectronicDevice1.power_status)

ElectronicDevice1.power_on()
print(ElectronicDevice1.power_status)
ElectronicDevice1.power_off()
print(ElectronicDevice1.power_status)
