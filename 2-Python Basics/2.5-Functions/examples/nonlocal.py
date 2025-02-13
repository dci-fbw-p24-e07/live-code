# outside function 
def outer():
    message = "local"
    
    # nested function
    def inner():
        
        # declare the nonlocal variable 
        nonlocal message
        
        message = "nonlocal"
        print("inner func:", message)
    
    inner()
    print("outer func:", message)
    
outer()
