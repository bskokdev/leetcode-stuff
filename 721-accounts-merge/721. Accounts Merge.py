class Solution:
    def build_email_accounts(self, accounts):
        email_accs = defaultdict(list)
        for i, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                email_accs[acc[j]].append(i)
        return email_accs

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_acss = self.build_email_accounts(accounts)
        visited = set()
        def dfs(i, emails):
            if i in visited:
                return
            visited.add(i)
            for j in range(1, len(accounts[i])):
                emails.add(accounts[i][j])
                for nei_acc in email_acss[accounts[i][j]]:
                    dfs(nei_acc, emails)

        res = []
        for i, acc in enumerate(accounts):
            if i in visited:
                continue
            emails = set()
            dfs(i, emails)
            res.append([acc[0]] + sorted(emails))
        return res

