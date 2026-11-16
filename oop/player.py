class player:
    def __init__(self,state,jrno,name,matches):
        self.state=state
        self.jrno=jrno
        self.name=name
        self.matches=matches

    def get_state(self):
        return self.state
    