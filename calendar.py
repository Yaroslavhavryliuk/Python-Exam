import datetime

class Calendar:
    def __init__(self):
        self.events = []

    def printEvent(self, event):
        print(event.action)
        print(event.date)
        print(str(event.priority) + '\n')

    def sortPriority(self, events):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(events) - 1):
                if events[i].priority < events[i + 1].priority:
                    events[i], events[i + 1] = events[i + 1], events[i]
                    swapped = True


    def sortDates(self, events):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(events) - 1):
                if events[i].date > events[i + 1].date:
                    events[i], events[i + 1] = events[i + 1], events[i]
                    swapped = True


    def addEvent(self, event):
        self.events.append(event)
        print('Event added')

    def getEventByDate(self, date):
        retEvents = []
        for event in self.events:
            if date == event.date:
                retEvents.append(event)
        if len(retEvents) == 0:
            print('No events on this date')
        else:
            self.sortPriority(retEvents)
            for event in retEvents:
                self.printEvent(event)

    def getEventByDateRange(self, date1, date2):
        retEvents = []
        for event in self.events:
            if event.date >= date1 and event.date <= date2:
                retEvents.append(event)
        if len(retEvents) == 0:
            print('No events on this range of dates')
        else:
            self.sortDates(retEvents)
            for event in retEvents:
                self.printEvent(event)

    def nextEvent(self):
        futEvents = []
        for event in self.events:
            if event.date >= datetime.datetime.now().date():
                futEvents.append(event)
        if len(futEvents) == 0:
            print('No events in the future')
        else:
            self.sortDates(futEvents)
            self.printEvent(futEvents[0])