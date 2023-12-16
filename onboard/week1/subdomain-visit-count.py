class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d=Counter()
        for domain in cpdomains:
            count,web=domain.split()
            count=int(count)
            web=web.split('.')
            while web:
                d['.'.join(web)]+=count
                web.pop(0)
        return map(lambda item: str(item[1])+" "+item[0], d.items())
