# 치킨 쿠폰

def solution(chicken):
    service_chicken = chicken//10
    extra_coupon = (chicken//10) + (chicken%10)
    
    while True:
        if extra_coupon < 10:
            break
        else:
            service_chicken += extra_coupon//10
            extra_coupon = (extra_coupon//10) + (extra_coupon%10)
    
    return service_chicken

print(solution(1081))