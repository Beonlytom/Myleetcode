class Solution(object):
    def romanToInt(s):
        rnumber = 0
        nl = len(s)
        for n in range(nl):
            if n != 0:
                char = s[n]
                if char == "I":
                    rnumber += 1
                if char == "V":#
                    if s[n-1] == "I":
                        rnumber += 3
                    else:
                        rnumber += 5 
                if char == "X":
                    if s[n-1] == "I":
                        rnumber += 8
                    else:
                        rnumber += 10
                if char == "L":
                    if s[n-1]  == "X":
                        rnumber += 30
                        print("diocan")
                    else:
                        rnumber += 50
                if char == "C":
                    if s[n-1] == "X":
                        rnumber += 80
                    else:
                        rnumber += 100

                if char == "D":
                    if s[n-1] == "C":
                        rnumber += 300
                    else:
                        rnumber += 500 
                if char == "M":
                    if s[n-1] == "C":
                        rnumber += 800
                    else:
                        rnumber += 1000
            else:
                char = s[n]
                if char == "I":
                    rnumber += 1
                if char == "V":#
                        rnumber += 5 
                if char == "X":
                        rnumber += 10
                if char == "L":
                        rnumber += 50
                if char == "C":
                        rnumber += 100
                if char == "D":
                        rnumber += 500 
                if char == "M":
                        rnumber += 1000
            
            print(rnumber)
        return rnumber
    
print(Solution.romanToInt(s = "MDCCCLXXXIV"))