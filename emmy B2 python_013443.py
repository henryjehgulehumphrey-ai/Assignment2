
#function to calcuate speed
def calculate_speed():
    distance=float(input("Enter distance(m): "))
    time=float(input("Enter time(s): "))
    speed=distance/time
    print(f"speed = {speed}m/s")

#function to calculate force
def calculate_force():
    mass= float(input("Enter mass: (kg): "))
    acceleration=float(input("Enter acceleration (m/s^2): "))
    force=mass*acceleration
    print("force ={force} N")

#function to calculate work
def calculate_work():
    force = float(input("Enter the force(N): "))
    distance= float(input("Enter the distance(M): "))
    work=force*distance
    print("work = {work} j")

#function to calculate power
def calculate_power():
    work= float(input("Enter work(j): "))
    time =float(input("Enter time(s): "))
    power= work/time
    print("power= {power} W")



#function to calculate density
def calculate_density():
    mass= float(input("Enter the mass(kg): "))
    volume=float(input("Enter volume(m^3): "))
    density = mass/volume
    print("density={density} kg/m^3 ")


while True:
    print("\n---five physics formulas ---")
    print("1 speed")
    print("2 force")
    print("3 work")
    print("4 power")
    print("5 density")

    choice=input("choose an operation(1-5): ")
    if choice=="1":
        calculate_speed()
    elif choice=="2":
        calculate_force()
    elif choice=="3":
        calculate_work()
    elif choice=="4":
        calculate_power()
    elif choice=="5":
        calculate_density()
    else:
        print("Invalid choice! please choose 1-5")

    continue_choice=input("\n do you want to continue ? (yes/no): ")
    if continue_choice.lower()=="yes":
        continue
    elif continue_choice.lower()=="No":
        print("program terminated. Thank you!")
        break
    else:
        print("Invalid input. program terminated ")
        break