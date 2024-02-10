import time
class Car_agent():
    def __init__(self,name_id,width=1.1,height=0.9,length=1.1,loc_x=0.0,loc_y=0.0,tick=0.01):
        self.name_id=name_id
        self.width=width
        self.height=height
        self.length=length
        self.loc_x=loc_x
        self.loc_y=loc_y
        self.__vx=0.0
        self.__vy=0.0
        self.__ax=0.0
        self.__ay=0.0
        self.tick=tick

    
    def get_position(self,show=False):
        if show:
            print(f"Agent{self.name_id}:\nlocation:x:{self.loc_x} y:{self.loc_y}\nspeed:x:{self.__vx}m/s y:{self.__vy}m/s")
        return [self.loc_x,self.loc_y,self.__vx,self.__vy,self.__ax,self.__ay]

    def __calculate(self):
        pass


    def move_car(self,direction):
        start=time.time()
        end=start+tick
        self.__vx+=direction[0]*self.tick*5.0
        self.__vy+=direction[1]*self.tick*5.0
        
        while time.time()<end:#hold
            pass
        




car1 =Car_agent(name_id=1)
car1.get_position(1)

