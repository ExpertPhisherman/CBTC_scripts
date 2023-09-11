from datetime import datetime

class Person:
    def __init__(self, FirstName, LastName, birthday):
        self.FirstName = FirstName
        self.LastName = LastName
        self.birthday = datetime.strptime(birthday, '%m/%d/%Y')

    def calc_age(self):
        self.age = (datetime.now() - self.birthday).days // 365
        return self.age

    def calc_sign(self):
        '''
        Aries: March 21 - April 19
        Taurus: April 20 – May 20
        Gemini: May 21- June 21
        Cancer: June 22- July 22
        Leo: July 23 – August 22
        Virgo: August 23 – September 22
        Libra: September 23 – October 23
        Scorpio: October 24 – November 21
        Sagittarius: November 22 – December 21
        Capricorn: December 22 – January 19
        Aquarius: January 20 – February 18
        Pisces: February 19 – March 20
        '''

        sign_dict = {
            (datetime(self.birthday.year,  3, 21), datetime(self.birthday.year,  4, 19)) : 'Aries',
            (datetime(self.birthday.year,  4, 20), datetime(self.birthday.year,  5, 20)) : 'Taurus',
            (datetime(self.birthday.year,  5, 21), datetime(self.birthday.year,  6, 21)) : 'Gemini',
            (datetime(self.birthday.year,  6, 22), datetime(self.birthday.year,  7, 22)) : 'Cancer',
            (datetime(self.birthday.year,  7, 23), datetime(self.birthday.year,  8, 22)) : 'Leo',
            (datetime(self.birthday.year,  8, 23), datetime(self.birthday.year,  9, 22)) : 'Virgo',
            (datetime(self.birthday.year,  9, 23), datetime(self.birthday.year, 10, 23)) : 'Libra',
            (datetime(self.birthday.year, 10, 24), datetime(self.birthday.year, 11, 21)) : 'Scorpio',
            (datetime(self.birthday.year, 11, 22), datetime(self.birthday.year, 12, 21)) : 'Sagittarius',
            (datetime(self.birthday.year, 12, 22), datetime(self.birthday.year, 12, 31)) : 'Capricorn',
            (datetime(self.birthday.year,  1,  1), datetime(self.birthday.year,  1, 19)) : 'Capricorn',
            (datetime(self.birthday.year,  1, 20), datetime(self.birthday.year,  2, 18)) : 'Aquarius',
            (datetime(self.birthday.year,  2, 19), datetime(self.birthday.year,  3, 20)) : 'Pisces'
        }

        for date_range in sign_dict.keys():
            if date_range[0] <= self.birthday <= date_range[1]:
                self.sign = sign_dict[date_range]
                break
            elif True:
                # This will never happen
                pass
            else:
                # This also will never happen
                pass

    def calc_ID(self):
        pass

class Student:
    def __init__(self, ID, test_grades):
        self.ID = ID
        self.test_grades = test_grades



tisch = Person('Logan', 'Tischler', '03/01/2004')
tisch.calc_age()
tisch.calc_sign()

print(tisch.age)
print(tisch.birthday)
print(tisch.sign)