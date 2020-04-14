# finds the request that is the shortest distance from current cylinder
def findClosest(request, currentCylinder):  
    closest_req = request[0]
    for i in range(1, len(request)):
        distance = abs(currentCylinder - request[i])
        if(distance < abs(closest_req-currentCylinder)):
            closest_req = request[i]

    request.remove(closest_req)

    return closest_req  


#shortest seek time first algorithm      
def SSTF(request, current_cylinder):
    traveled = 0
    req_length = len(request)

    print("\n")
    for i in range(req_length):
        nearest_req = findClosest(request, current_cylinder)
        print(f"Servicing... {nearest_req}")

        traveled += abs(current_cylinder - nearest_req)
        current_cylinder = nearest_req
    
    print(f"Track distance covered : {traveled}")
      

#main method      
if __name__ =="__main__": 
    try: 
        ref_string = []
        
        ref_length = int(input("Enter number of cylinder requests : "))

        print ("\nEnter individual requests (must be positive integers)")
        for i in range(ref_length):
            ref_string.append(int(input(f"Request {i+1} : ")))

        starting_cylinder = int(input("\nEnter disk starting cylinder : "))

        SSTF(ref_string, starting_cylinder) 

    except ValueError:
        print("\n!!Invalid data type entered, please try again")
    except:
        print("\n!!Unexpected error encountered, please try again")