class MyCalendar:
    def __init__(self):
        self.bookings = []

    # def book(self, start: int, end: int) -> bool:
    #     bookings = self.bookings
    #     for booking in bookings:
    #         if range(max(booking[0], start), min(booking[1], end)):
    #             return False
    #     self.bookings.append([start, end])
    #     return True

    def book(self, start, end):
        for s, e in self.bookings:
            if s < end and start < e:
                return False
        self.bookings.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(97,100))
print(obj.book(33,51))
print(obj.book(89,100))
print(obj.book(83,100))
print(obj.book(75,92))
print(obj.book(76,95))
print(obj.book(19,30))
print(obj.book(53,63))
print(obj.book(8,23))
print(obj.book(18,37))
print(obj.book(87,100))
print(obj.book(83,100))
print(obj.book(54,67))
print(obj.book(35,48))
print(obj.book(58,75))
print(obj.book(70,89))
print(obj.book(13,32))
print(obj.book(44,63))
print(obj.book(51,62))
print(obj.book(2,15))

# [[],[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]
# [null,true,true,false,false,true,false,true,true,false,false,false,false,false,false,false,false,false,false,false,true]
