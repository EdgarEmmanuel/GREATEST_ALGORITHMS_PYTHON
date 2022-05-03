import time

timeInSecond = float(input("Type the time in seconds : "))

totalTime = timeInSecond

dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "saturday", 6: "Sunday"}

while totalTime != 0:
    date = time.gmtime(timeInSecond)
    print(f"{dict.get(date[6])}/{date[1]}/{date[0]} , {date[3]}:{date[4]}:{date[5]}")
    time.sleep(1)
    timeInSecond -= 1
    totalTime = timeInSecond
