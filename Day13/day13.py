from math import ceil, prod
from functools import reduce


def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod/n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod


def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1


def part1(time, bus_schedule):
    bus_schedule = [int(bus) for bus in bus_schedule.split(",") if bus != "x"]
    
    times = {}
    for bus in bus_schedule:
        times[ceil(time/bus)*bus] = bus
    print((min(times)-time)*times[min(times)])
    
    
def part2(bus_schedule):
    
    input = [(i, int(bus)) for i, bus in enumerate(bus_schedule.split(",")) if bus != "x"]
    buses = [bus for _, bus in input]
    times = [bus - i for i, bus in input]
    
    N = prod(buses)
    t = sum(b * (N // n) * pow(N // n, -1, n) for b, n in zip(times, buses))
    print(t % N)
    
    
def main():
    with open("input.txt") as f:
        time, bus_schedule = f.read().splitlines()

    part1(int(time), bus_schedule)
    part2(bus_schedule)
    
    
if __name__ == "__main__":
    main()