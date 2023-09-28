class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            s.add(local + '@' + domain)
        return len(s)
            