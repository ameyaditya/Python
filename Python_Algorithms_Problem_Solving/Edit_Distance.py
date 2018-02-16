def editdis(str1,str2,l1,l2):
    dp = [[0 for i in range(l2+1)]for j in range(l1+1)]
    for i in range(l1+1):
        for j in range(l2+1):
            if l1 == 0:
                dp[i][j] = j
            elif l2 == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
    return dp[i][j]

str1 = "Sunday"
str2 = "Saturday"
print(editdis(str1,str2,len(str1),len(str2)))
