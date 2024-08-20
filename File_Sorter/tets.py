for i in range(1,100):
            # if len(res)==n:
            #     break
            
            for j in range(2,i):
                if i%2==0 or i%3==0 or i%5==0:
                     can=True
                if j not in [2,3,5] and can:
                    if i%j==0:
                        break
            else:
                print(i)
                 
                
                      
               
               
                      
                
            