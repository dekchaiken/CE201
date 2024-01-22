queue = []
a = 1
while True:
    q = input("Booking (B) / Calling (C) / End (X): ")
    if q == 'B':
        name = input("Customer Name: ")
        queue.append(f"A{a}-{name}")
        print(f"A{a}-{name}")
        print("Queue:",queue)
        a += 1
    if q == 'C':
        print(queue.pop(0))
        print(queue)
    if q == 'X':
        print("***End***")
        break
    
    
