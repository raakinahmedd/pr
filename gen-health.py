import random
import time

def simulate_f1_driver_heart_rate():
    heart_rate = random.randint(60, 80)  # Starting at resting heart rate
    
    for _ in range(10):
        if random.random() > 0.5:
            heart_rate += random.randint(5, 15)
        else:
            heart_rate -= random.randint(1, 10)
        
        heart_rate = max(60, min(heart_rate, 200))
        
        print(f"Heart Rate: {heart_rate} bpm")
        
       
        time.sleep(1)

simulate_f1_driver_heart_rate()


