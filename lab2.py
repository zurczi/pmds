import math
import random
import itertools

def simulation(numberOfPeople,probability,numberOfHotels,numberOfDays):
    daysHotelsPeople={}
    for day in range(0,numberOfDays):
        daysHotelsPeople[day]={}
        for person in range(0,numberOfPeople):
            wantToGo = random.choices([0,1],[1-probability,probability])
            if wantToGo[0]==1:
                whichHotel = random.randint(0,numberOfHotels)
                if whichHotel in daysHotelsPeople[day]:
                    daysHotelsPeople[day][whichHotel].append(person)
                else:
                    daysHotelsPeople[day][whichHotel]=[]
                    daysHotelsPeople[day][whichHotel].append(person)
        for hotel in daysHotelsPeople[day]:
                combinations = list(itertools.combinations(daysHotelsPeople[day][hotel],2))
                daysHotelsPeople[day][hotel]= combinations
    print(len(daysHotelsPeople))
    return daysHotelsPeople

def countNumberOfMeet(daysHotelsPeople):
    numberOfMeet = {}
    for day in daysHotelsPeople:
        for hotel in daysHotelsPeople[day]:
            for pair in daysHotelsPeople[day][hotel]:
                if pair in numberOfMeet:
                    numberOfMeet[pair] += 1
                else:
                    numberOfMeet[pair] = 1
    print(len(numberOfMeet))
    return numberOfMeet

def count(numberOfMeet):
    histogram = {}
    pairs = 0
    peopleAndDays = 0
    for pair in numberOfMeet:
        if numberOfMeet[pair] in histogram:
            histogram[numberOfMeet[pair]] +=1
        else:
            histogram[numberOfMeet[pair]] =1
        if numberOfMeet[pair] >=2 :
            pairs+=1
            peopleAndDays += math.factorial(numberOfMeet[pair])/(math.factorial(2)*math.factorial(numberOfMeet[pair]-2))
    print("Pairs")
    print(pairs)
    print("People and Days")
    print(peopleAndDays)
    print("Histogram")
    print(histogram)

def main():
    n=10000#ludzie
    p=1/10 #prawdo ze danego dnia ktos chce isc do jakiegos hotelu
    n_h=100 #liczba hoteli
    n_d=100 #liczba dni
    result = simulation(n,p,n_h,n_d)
    numberOfMeet = countNumberOfMeet(result)
    count(numberOfMeet)
if __name__ == "__main__":
    main()