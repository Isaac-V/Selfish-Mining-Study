def seqs(list):
    seqArray = [];
    for i in range(11):
        seqArray.append(0)
    
    index = 0;
    
    while index < len(list):

        count = 1
        current = list[index]
        
        if index+1<len(list):
            next = list[index+1]
            while next == current+1:
                count += 1
                if index+2 < len(list):
                    index += 1
                    current = list[index]
                    next = list[index+1]
                else:
                    break
                    
        seqArray[count] += 1
        index += 1
        
    return seqArray

def 
          
def main():
    
    data = [1,2,3,5,7,8,10]
    
    print(seqs(data))
    
    
main()