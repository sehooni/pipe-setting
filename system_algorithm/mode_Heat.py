import Sensor
import Value

if Sensor.sensor.Amount>Value.container.Amount:
                    print("폐열회수모드 사용 가능합니다.")
                    if input("폐열회수모드를 사용하시겠습니까? Y or N : ")=="Y"or"y":
                        belb_gas=1
                        print("-----------------------------------------------------------------------------")
                        print("잠시 후 가스 밸브가 열립니다.")
                        print("-----------------------------------------------------------------------------")
                        print("예상 시간 :", Value.Heat.heating(),"분")
                        print("-----------------------------------------------------------------------------")
                        print("정상모드로 돌아갑니다.")
                        print("-----------------------------------------------------------------------------")
else:            
    print("-----------------------------------------------------------------------------")
    print("빗물용수 공급이 필요합니다. 빗물양 : ", Sensor.sensor.Amount)
    print("정상모드로 돌아갑니다.")