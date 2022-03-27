import math


class pipe_setting:
    # 관의 너비와 두께 설정 (단위: cm)
    # 입구 너비
    Input_Diameter = float(input("파이프 입구의 지름: "))  # 지름 길이
    Input_radius = Input_Diameter / 2  # 반지름 길이
    Outer_thickness1 = float(input("파이프 입구의 두께: "))  # 관두께 길이

    # 출구 너비
    Outer_Diameter = float(input("파이프 출구의 지름: "))  # 지름 길이
    Output_radius = Outer_Diameter / 2  # 반지름 길이
    Mode = input("파이프 출구의 두께가 입구의 두께와 동일합니까? o or x: ")
    if Mode == 'o':
        Outer_thickness2 = Outer_thickness1  # 관두께 길이
        print("파이프 출구의 두께가 입구의 두께와 동일한 {}cm를 갖습니다.".format(Outer_thickness2))
    else:
        Outer_thickness2 = float(input("파이프 출구의 두께: "))  # 관두께 길이

    def Pipe_Area(x1, x2):
        return ((x1 - x2) ** 2) * (math.pi)  # 내부 넓이

    def Pipe_Radius(x1, x2):
        return (x1 - x2)  # 내부 반경

    # 관 통로의 넓이 계산
    I1 = Input_radius;
    I2 = Outer_thickness1;
    O1 = Output_radius;
    O2 = Outer_thickness2;
    D_I = Pipe_Area(I1, I2);
    D_O = Pipe_Area(O1, O2);

    # 내부 반경 계산
    R_I = Pipe_Radius(I1, I2);
    R_O = Pipe_Radius(O1, O2);

    print("입구의 관 넓이: {}".format(D_I))
    print("출구의 관 넓이: {}".format(D_O))
    print("-----------------------------------------------------------------------")


class Velocity_setting:
    # 입구 유속 설정
    Velocity_I = float(input("입구의 유속: "))  # 빗물 도입부분의 유속 측정값 (단위: m/s)
    V_I = Velocity_I;

    # 유량 일반화 계산을 통한 출구 유속 측정
    Input_discharge = V_I * pipe_setting.D_I * (10**(-4)); #유량의 단위 : m^3/s
    Q_I = Input_discharge;

    Output_discharge = Input_discharge; # ***유량은 일정하다는 가정 대입.
    Q_O = Output_discharge;

    V_O = Q_O / (pipe_setting.D_O * (10**(-4))); # 출구 유속 계산 (단위: m/s)
    print('출구의 유속 : {}'.format(V_O))
    print('------------------------------------------------------------------------')

class length_pipe:
    # 배관의 길이 설정
    pipe_length = float(input('배관 길이 :')) # 단위 : cm
    pipe_l = pipe_length;

    # 배관의 부피 설정 (일자로 가정하되, 이때 입구와 출구 넓이 값은 상이해도 측정 가능, 추후 일자가 아닌 버전을 만들 예정)
    pipe_V = (pipe_setting.D_I + pipe_setting.D_O) * pipe_l / 2; # 단위: cm^3

    #배관을 이동하는데 걸리는 시간
    pipe_time = pipe_V / Velocity_setting.Q_O * (10**(-6)); #단위를 맞춰주기 위해 10**(-6) 적용
    print("빗물이 이동하는데 걸리는 시간은 {}초 입니다.".format(pipe_time))
    print('-------------------------------------------------------------------------')

class thermal_conductivity:
    # 여기에 재료명으로 해서 배관 재료에 대한 열전도율 저장
    # 재료는 폴리부틸렌으로 설정
    Polybutylene = 0.33; #단위: kcal/m*hr*C
    PB = Polybutylene / 3600; # 약자표기 및 단위를 kcal/m*s*C로 바꿈

class temperature_setting:
    # 입구에서의 빗물의 온도 체크
    temperature_input = int(input("입구에서의 빗물의 온도:"))
    temp_IP = temperature_input;
    print("파이프의 내부의 온도는 입구에서의 빗물의 온도는 {}℃ 와 같습니다.".format(temp_IP))

    # 파이프 외부 온도 체크
    temperature_out = int(input("파이프의 외부 온도: "))
    temp_O = temperature_out;
    print('--------------------------------------------------------------------------')

class heat_loss:
    # 배관에서 유체가 흘러갈 때의 열손실향
    K_H = thermal_conductivity.PB; # 열전도율 = 열전달계수
    L_H = length_pipe.pipe_l * 10**(-2); # 단위를 cm에서 m로 환산
    T1_H = temperature_setting.temp_IP;
    T2_H = temperature_setting.temp_O;
    r1_H = pipe_setting.R_I * 10**(-2); # 단위를 cm에서 m로 환산
    r2_H = pipe_setting.I1 * 10**(-2); # 단위를 cm에서 m로 환산
    Heat_loss = 2 * (math.pi) * K_H * L_H * (T1_H - T2_H) / (math.log(r2_H/r1_H));
    Q = Heat_loss;

    print("파이프 내에서 발생한 열손실량은 {}입니다.".format(Q))