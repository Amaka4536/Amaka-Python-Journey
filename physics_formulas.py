def speed(distance, time):
    return distance / time


def acceleration(final_velocity, initial_velocity, time):
    return (final_velocity - initial_velocity) / time


def force(mass, acceleration):
    return mass * acceleration


def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2


def density(mass, volume):
    return mass / volume


while True:
    print("\nChoose a formula:")
    print("1. Speed")
    print("2. Acceleration")
    print("3. Force")
    print("4. Kinetic Energy")
    print("5. Density")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))
        answer = speed(distance, time)
        print("Speed =", answer)

    elif choice == "2":
        final_velocity = float(input("Enter final velocity: "))
        initial_velocity = float(input("Enter initial velocity: "))
        time = float(input("Enter time: "))
        answer = acceleration(final_velocity, initial_velocity, time)
        print("Acceleration =", answer)

    elif choice == "3":
        mass = float(input("Enter mass: "))
        acceleration_value = float(input("Enter acceleration: "))
        answer = force(mass, acceleration_value)
        print("Force =", answer)

    elif choice == "4":
        mass = float(input("Enter mass: "))
        velocity = float(input("Enter velocity: "))
        answer = kinetic_energy(mass, velocity)
        print("Kinetic Energy =", answer)

    elif choice == "5":
        mass = float(input("Enter mass: "))
        volume = float(input("Enter volume: "))
        answer = density(mass, volume)
        print("Density =", answer)

    else:
        print("Invalid choice.")

    choice = input("Do you want to continue? yes/no: ")

    if choice.lower() == "no":
        break

print("Program ended.")
