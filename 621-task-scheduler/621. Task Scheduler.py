class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        pq = [-cnt for cnt in count.values()]
        heapq.heapify(pq)

        queue = deque()
        time = 0
        while pq or queue:
            time += 1
            if pq:
                cur_task_cnt = heapq.heappop(pq)
                cur_task_cnt += 1
                if cur_task_cnt:
                    queue.append((cur_task_cnt, time + n))
            if queue and queue[0][1] == time:
                next_to_process = queue.popleft()[0]
                heapq.heappush(pq, next_to_process)
        return time
