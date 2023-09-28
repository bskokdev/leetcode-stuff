class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(i, dots, cur_ip):
            if dots == 4 and i >= len(s):
                res.append(cur_ip[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) <= 255 and (i == j or s[i] != '0'):
                    dfs(j+1, dots+1, cur_ip + s[i:j+1] + '.')
        dfs(0, 0, '')
        return res