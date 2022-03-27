import math
import Sensor

class container:
    x = 45 # 빗물통의 가로길이 (단위:cm)
    y = 15 # 빗물통의 세로길이 (단위:cm)
    h = 20 # 빗물통의 높이 (단위:cm)
    A = x*y  # 빗물통의 면적 (단위:cm^2)
    V = A*h # 빗물통의 부피 (단위:cm^3)
    Amount = V*0.5 # 폐열회수 및 보일러 급수 작동 조건 빗물양


class Heat:
    def heating():
        T_set=int(input("설정 온도 : "))
        T_gas=15 #가스 온도
        gap=Sensor.sensor.T-T_gas
        D_gas=5 #가스 배관 지름
        h_gas=10 #가스 배관 높이
        A_gas=D_gas/2*2*math.pi*h_gas
        Q_rain=0.577*A_gas*(gap+273.15)/(container.x/4) #빗물의 열전도율
        c=1
        m_rain=Sensor.sensor.Amount #빗물의 무게
        Tpers=Q_rain/c/m_rain
        i=int((T_set-Sensor.sensor.T)/Tpers)
        return i

class plumbing:
    r = 5 # 빗물이 빠져 나갈 배관의 반지름 (단위:5cm)
    A = r*r*math.pi # 배관의 면적
    v = 1 # 배관으로 빠져나가는 유량의 속도
    q = A*v # 초당 빠져나가는 유량
    t = Sensor.sensor.Amount/q #배관으로 빗물이 빠져나가는데 걸리는 예상시간
