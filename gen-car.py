import random
import time

# Function to generate fake car data
def generate_car_data():
    gear = random.randint(1, 6)  # Random gear number between 1 and 6
    brake_percentage = random.uniform(70, 100) if gear == 1 else random.uniform(0, 12)  # More braking in lower gears
    speed = random.randint(30, 70) * gear  # Speed increases with gear
    rpm = random.randint(1000, 2000) * gear if speed > 0 else 0  # RPM depends on gear and speed

    # Fine-tuning speed and rpm based on brake percentage
    if brake_percentage > 0:
        speed = max(0, speed - int(brake_percentage / 2))  # Decrease speed when brake is applied
        rpm = max(800, rpm - int(brake_percentage * 10))   # RPM decreases with braking, but stays above idle

    # Return a dictionary of the data
    return {
        'gear': gear,
        'brake_percentage': round(brake_percentage, 2),
        'speed': speed,
        'rpm': rpm
    }

# Example: Continuously generate data every second
for _ in range(10):  # Adjust the range to generate more data
    car_data = generate_car_data()
    print(car_data)
    time.sleep(1)  # Simulate real-time data generation with a delay


# hello from raakin, for v1.0