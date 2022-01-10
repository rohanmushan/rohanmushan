# Write Program - A train 340 m long is running at a speed of 45 km/hr.
# What time will it take to cross a 160 m long tunnel?

trainlen = 340
tunnellen = 160
total = trainlen + tunnellen
speed = 45
mps = 5/18

# Calculating time to cross the tunnel
time = total / (45 * mps)

print ("Total time taken by train to cross the tunnel is: ",time)