import time
import threading
stat=True
class tick():
    def auto_calculate(self,funcs):
        threads=[]
        for i,func in enumerate(funcs):
            t=threading.Thread(target=func)
            threads.append(t)
            

        for t in threads:
            t.start()
        # for t in threads:
        #     t.join()
        

class Car_agent():
    def __init__(self,name_id,width=100.0,height=100.0,length=0,loc_x=0.0,loc_y=0.0,tick=0.01,):
        self.name_id=name_id
        self.width=width
        self.height=height
        self.length=length
        self.loc_x=loc_x
        self.loc_y=loc_y
        self.__vx=5.1
        self.__vy=10.8
        self.__ax=0.0
        self.__ay=0.0
        self.tick=tick

        

    
    def get_position(self,show=False):
        if show:
            print(f"Agent{self.name_id}:\nlocation:x:{self.loc_x} y:{self.loc_y}\nspeed:x:{self.__vx}m/s y:{self.__vy}m/s")
        return [self.loc_x,self.loc_y,self.__vx,self.__vy,self.__ax,self.__ay]

    def calculate(self):
        global stat
        while stat:
            start=time.time()
            if self.loc_x<=0 or self.loc_x>=self.width:
                self.__vx=-self.__vx
            if self.loc_y<=0 or self.loc_y>=self.height:
                self.__vy=-self.__vy
            self.__ay=-9.8    
            time.sleep(0.01)
            end=time.time()
            tick=end-start
            self.__vx=tick*self.__ax+self.__vx
            self.__vy=tick*self.__ay+self.__vy

            self.loc_x=tick*self.__vx+self.loc_x
            self.loc_y=tick*self.__vy+self.loc_y
        

    # def 
    # def move_car(self,direction):
    #     start=time.time()
    #     end=start+tick
        
    #     self.__vx+=direction[0]*self.tick*__ax
    #     self.__vy+=direction[1]*self.tick*__ay
        
    #     while time.time()<end:#hold
    #         pass
        
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
car1 =Car_agent(name_id=1)

ticks=tick()


# 创建一个图和坐标轴
fig, ax = plt.subplots()

# 设置坐标轴的范围
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)


# 创建一个圆形表示小球，指定位置、半径和颜色
ball = Circle((0, 0), 1, color='red')
# 将小球添加到坐标轴中
ax.add_patch(ball)
# 显示图表
plt.show()
a=time.time()
tick.auto_calculate([car1.calculate])
while stat:
    position=car1.get_position(0)
    print('ok')
    ball.set_center(position[0],position[1])
    plt.draw()
    b=time.time()
    if b-a>=3:
        stat=False
        




