def min_coins(coins,V):
  coins.sort()
  coins.reverse()
  ans = []
  for i in range(len(coins)):
      while V >= coins[i]:
          V -= coins[i]
          ans.append(coins[i])
  print("The minimum number of coins is", len(ans))
  print("The coins are")
  for i in range(len(ans)):
      print(ans[i], end=" ")
