import math 
E0 =  1.0
A = float(input("Enter mass number: "))
tetha = float(input("Enter scattering angle (radian): "))
tetha_radian  = math.radians(tetha)
numerator = (A**2 + 1 + 2*A*math.cos(tetha_radian))  
denominator = (A + 1)**2  
energy = E0 * (numerator / denominator)

print(f"mass number: {A}" )
print(f"scattering angle (radian): {tetha_radian}")
print(f"Final neutron energy (MeV): {energy}")