def longestCommonPrefix(strs):
        if min(strs, key= len) == "":
            return ""
        cpl = 0
        spp = min(strs, key=len)
        letterchecking = 0
        for a in spp:
            for i in strs:
                if(a != i[letterchecking]):
                    diflettfound = True
                    return min(strs, key= len)[:letterchecking]
            letterchecking += 1
        return min(strs, key= len)

            

print(longestCommonPrefix(("", "a")))
                
