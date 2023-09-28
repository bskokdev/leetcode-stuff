class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(pq)

        last_char, last_occs = '', 0
        s = ''
        while pq:
            occs, char = heapq.heappop(pq)
            if abs(occs) == 0:
                break
            # still can use prev char
            if last_occs < 0:
                heapq.heappush(pq, (last_occs, last_char))
            if abs(occs) >= 2:
                if abs(occs) > abs(last_occs):
                    s += char*2
                    occs += 2
                else:
                    s += char
                    occs += 1
            else:
                s += char
                occs += 1
            last_char, last_occs = char, occs
        return s