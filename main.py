import datetime

from calendar import Calendar
from event import Event

if __name__ == '__main__':
    calendar = Calendar()

    while True:
        print("1. Add an event \n" +
              "2. Get events by date \n" +
              "3. Get elements by range of dates \n" +
              "4. Get next event \n" +
              "5. Exit")
        print("Choose an action: ")
        command = int(input())
        if command == 1:
            print('Enter the event: ')
            action = input()
            print('Enter the date of event like year|month|date: ')
            stringDate = input()
            year = int(stringDate.split('|')[0])
            month = int(stringDate.split('|')[1])
            day = int(stringDate.split('|')[2])
            date = datetime.date(year, month, day)
            print('Enter the priority of event from 0 (less important) to 10 (most important): ')
            priority = int(input())
            event = Event(action, date, priority)
            calendar.addEvent(event)
        elif command == 2:
            print('Enter the date of event like year|month|date: ')
            stringDate = input()
            year = int(stringDate.split('|')[0])
            month = int(stringDate.split('|')[1])
            day = int(stringDate.split('|')[2])
            date = datetime.date(year, month, day)
            calendar.getEventByDate(date)
        elif command == 3:
            print('Enter the first date like year|month|date: ')
            stringDate = input()
            year = int(stringDate.split('|')[0])
            month = int(stringDate.split('|')[1])
            day = int(stringDate.split('|')[2])
            date1 = datetime.date(year, month, day)
            print('Enter the second date like year|month|date: ')
            stringDate = input()
            year = int(stringDate.split('|')[0])
            month = int(stringDate.split('|')[1])
            day = int(stringDate.split('|')[2])
            date2 = datetime.date(year, month, day)
            calendar.getEventByDateRange(date1, date2)
        elif command == 4:
            calendar.nextEvent()
        elif command == 5:
            exit()
        else:
            print('Unknown command')