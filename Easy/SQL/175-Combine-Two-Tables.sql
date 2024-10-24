Select Person.firstName, Person.LastName, Address.city, Address.state
from Person
LEFT JOIN Address
ON Person.personId = Address.personId