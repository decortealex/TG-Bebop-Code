from pyparrot.Bebop import Bebop

bebop = Bebop(drone_type="Bebop2")

# Connect to the drone, try up to 10 times
bebop.connect(num_retries=10)

# Tell drone to take off, give it 10 seconds to take off
bebop.safe_takeoff(timeout=5)

# Pause for 2 seconds. Drone will hover
bebop.smart_sleep(timeout=5)

# Tell drone to land
bebop.safe_land(timeout=5)

# Disconnect from the drone
bebop.disconnect()

