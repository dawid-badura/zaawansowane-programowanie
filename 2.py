class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
        return f'Dokładny adres biblioteki to: {self.zip_code}, {self.city}, {self.street}. Godziny otwarcia: {self.open_hours}. Telefon kontaktowy: {self.phone}'

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        return f'Zamówienie realizowane przez {self.employee}. Złożone przez {self.student}, w dniu {self.order_date}. Zamówione książki: {self.books}'

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return f'Pracownik: {self.first_name} {self.last_name}. Zatrudniony dnia {self.hire_date}. Urodzony dnia {self.birth_date}. Adres zamieszkania: {self.zip_code}, {self.city}, {self.street}. Telefon kontaktowy {self.phone}'

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self):
        return f'Książka znajduje się w bibliotece {self.library}. Data publikacji: {self.publication_date}. Imię i nazwisko autora: {self.author_name} {self.author_surname}. Liczba stron: {self.number_of_pages}'


L1 = Library("Katowice", "Jagodowa", "40-123", "8:00-16:00", 512345678)
L2 = Library("Chorzów", "Malinowa", "40-467", "10:00-18:00", 765432098)
O1 = Order("Andrzej Nowak", "Jan Konopski", "Python dla leniwych", "10/01/2021")
O2 = Order("Julia Kamyk", "Stefan Gęba", "JavaScript dla leniwych", "19/09/2021")
E1 = Employee("Krzysztof", "Modliszka", "01/03/2018", "12/11/1974", "Chorzów", "Owocowa", "40-290", 609123456)
E2 = Employee("Andrzej", "Nowak", "21/06/2014", "15/10/1994", "Katowice", "Kwiatowa", "40-456", 609123456)
E3 = Employee("Julia", "Kamyk", "05/04/2020", "05/02/1991", "Rybnik", "Żelowa", "42-320", 609123456)
B1 = Book("L1", "2016", "Tomasz", "Garncarz", "294")
B2 = Book("L2", "2012", "Tomasz", "Garncarz", "324")
B3 = Book("L1", "2013", "Stefan", "Gitara", "120")
B4 = Book("L1", "2019", "Stefan", "Gitara", "178")
B5 = Book("L2", "2005", "Miła", "Konopka", "162")

print(str(O1))
print(str(O2))