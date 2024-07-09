class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = 0
        wait_time = 0
        for customer in customers:
            if cur_time > customer[0]:
                wait_time += cur_time - customer[0] + customer[1]
                cur_time += customer[1]
            else:
                wait_time += customer[1]
                cur_time = customer[0] + customer[1]
            print(wait_time, cur_time)
        return wait_time/len(customers)
