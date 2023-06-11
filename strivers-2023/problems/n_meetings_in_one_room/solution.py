class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meet = [(start[i],end[i],i+1) for i in range(n)]
        meet = sorted(meet, key=lambda x: (x[1], x[2]))
        # print(meet)
        limit = 0
        count = 0
        for i in meet:
            if i[0] > limit:
                count += 1
                limit = i[1]
        return count
