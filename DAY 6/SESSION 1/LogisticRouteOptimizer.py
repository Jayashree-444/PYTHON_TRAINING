def logisticsRoutes(routes):
    
    if not routes:
        print("plz enter the values: ") # input constriant when we not have input
        return
    shortest=routes[0][2]
    longest=routes[0][2]
    total=0
    city_connections={}
    for src, dest, distance in routes:
        if distance<shortest:
            shortest=distance
        if distance>longest:
            longest=distance
        total+=distance
         # Count connections
        city_connections[src] = city_connections.get(src, 0) + 1
        city_connections[dest] = city_connections.get(dest, 0) + 1
        
    average=total/len(routes)
        
    above_avg=0
    for src, dest, distance in routes:
        if  distance>average:
            above_avg+=1
            
                
    print("Shortest:", shortest)
    print("Longest:", longest)
    print("Total:",  total)
    print("Average:", average)
    print("Routes above average:", above_avg)
    print("City connections:", city_connections)
                
# 🔹 Test Case 1
routes1 = [(0,1,10),(0,2,25),(1,2,15),(1,3,30),(2,3,20)]
print("Test Case 1:")
logisticsRoutes(routes1)

print("\n-----------------\n")

# 🔹 Test Case 2
routes2 = [(0,1,5),(1,2,5)]
print("Test Case 2:")
logisticsRoutes(routes2)