def calculate_distance(time, speed):
    return time * speed


time = float(input("Enter the time in hours: "))
speed = float(input("Enter the speed in kilometers per hour: "))

distance = calculate_distance(time, speed)
print(f"The distance is {distance} kilometers.")

