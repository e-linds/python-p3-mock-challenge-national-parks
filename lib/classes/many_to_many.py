class Visitor:
    all = []

    def __init__(self, name):
        self.name = name

        Visitor.all.append(self)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if type(value) is str and 0 < len(value) < 16:
            self._name = value

    name = property(get_name, set_name)
        
    def trips(self):
        array = []
        for each in Trip.all:
            if type(each) == Trip and each.visitor == self:
                array.append(each)
        return array
    
    def national_parks(self):
        array = []
        for each in self.trips():
            array.append(each.national_park)
        return list(set(array))
        
    
    def total_visits_at_park(self, park):
        array = []
        for each in self.trips():
            if each.national_park == park:
                array.append(each)
        return len(array)

#---------------------------------------------------------------------------------------------
class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name

        NationalPark.all.append(self)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if hasattr(self, "name") == False:
            if type(value) is str and len(value) > 2:
                self._name = value

    name = property(get_name, set_name)
        
    def trips(self):
        return [each for each in Trip.all if type(each) == Trip and each.national_park == self]
    
    def visitors(self):
        array = []
        for each in self.trips():
            array.append(each.visitor)
        return list(set(array))

    
    def total_visits(self):
        totalvisits = len(self.trips())
        if totalvisits == 0:
            return None
        else:
            return len(self.trips())
    
    def best_visitor(self):
        all_visitors = []
        for each in self.trips():
            all_visitors.append(each.visitor)
       
        counted_array = []

        if len(all_visitors) > 0:
            for each in all_visitors:
                individual_count = all_visitors.count(each)
                counted_array.append([individual_count, each])
            counted_array.sort(reverse=True)
            return counted_array[0][1]
        else:
            return None

#-------------------------------------------------------------------------------------------------------
class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        Trip.all.append(self)


    def get_start_date(self):
        return self._start_date

    def set_start_date(self, value):
        if type(value) is str and len(value) > 6:
            self._start_date = value

    def get_end_date(self):
        return self._end_date


    def set_end_date(self, value):
        if type(value) is str and len(value) > 6:
            self._end_date = value

    start_date = property(get_start_date, set_start_date)

    end_date = property(get_end_date, set_end_date)

    def get_visitor(self):
        return self._visitor

    def set_visitor(self, value):
        if type(value) is Visitor:
            self._visitor = value

    visitor = property(get_visitor, set_visitor)

    def get_national_parks(self):
        return self._national_park

    def set_national_parks(self, value):
        if type(value) is NationalPark:
            self._national_park = value

    national_parks = property(get_national_parks, set_national_parks)



testVisitor = Visitor("Teri")
testPark = NationalPark("RMNP")
testTrip = Trip(testVisitor, testPark, "December 1", "December 31")
testVisitor2 = Visitor("Dee")
testTrip2 = Trip(testVisitor2, testPark, "December 1", "December 31")
testTrip3 = Trip(testVisitor, testPark, "December 1", "December 31")
testTrip4 = Trip(testVisitor, testPark, "December 5", "December 15")




print(testVisitor.total_visits_at_park(testPark))

    





