class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tk = defaultdict(int)
        self.t = timeToLive  
    def generate(self, tokenId: str, currentTime: int) -> None:
        
        self.tk[tokenId] = currentTime
    def renew(self, tokenId: str, currentTime: int) -> None:
        limit = currentTime-self.t       
        if tokenId in self.tk and self.tk[tokenId]>limit:    
            self.tk[tokenId] = currentTime


    def countUnexpiredTokens(self, currentTime: int) -> int:
        limit = currentTime-self.t     
        c = 0
        for i in self.tk:
            if self.tk[i]>limit:        
                c+=1
        return c


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)