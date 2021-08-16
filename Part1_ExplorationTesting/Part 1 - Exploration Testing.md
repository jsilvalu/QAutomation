

# Part 1: Exploration Testing

## 1. Introduction and target

Exploration testing presents an external structure that is simple to describe, in which for a period of time a tester – or team of testers – interacts with a product to meet the objective of a mission, to present and report the results that the rest of the project actors will use to make conscious decisions. Exploratory testing allows the tester to be creative.
![imagen text](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen1.png?raw=true)

Some benefits of exploratory testing are:
- Easy optimization.
- Real-time decision-making.
- Quick product learning.

The goal is to explore and describe three key scenarios for a hotel's booking flow in [https://www.phptravels.net/](https://www.phptravels.net/)

## 2. Functionality

The functionality delivered by the development team consists in allowing to make a hotel reservation from a search. To explore this new functionality I have designed a mind map with the flows involved in this action as well as all its possible input parameters. 
The mind map that specifies this exploratory testing session is the following:
_____________________________________________=====

## 3. Key Scenarios

**3.1 Key Scenarios #1**
To make a reservation it is necessary to enter the user's personal information.

> AS a user I WANT to enter my personal information (first name, last
> name, email, phone, address, country, nationality) in order SO THAT make a
> reservation.

**3.2 Key Scenarios #2**
To make a reservation it is necessary to enter the travelers' information.

> AS a user I WANT to enter the travelers information (title, first name
> and last name) in order SO THAT make a reservation.

**3.3 Key Scenarios #3**
To make a reservation you must be able to pay with any payment method.

> AS a user I WANT to pay (bank transfer, pay later, Paypal, Stripe and
> Paddle) SO THAT make a reservation.


## 4. Results

Although the objective is not to test functionalities such as search, it belongs to part of the flow to start with the booking process and possible incidences have been detected that should be reported:

In relation to the hotel reservation process the following errors have been detected:


## 5.Risk analysis

The three key scenarios above represent critical basic functionalities without which it would be impossible to make a hotel reservation correctly.
- Without the user information it will not be possible to identify who the user is.
- If we have the information of the user making the reservation but not that of the companion, it will be possible to provide the service even if the functionality is not correct.
- If it is not possible to make the payment, it will not be possible to make the reservation.

Personally, I would prioritize the test cases related to the basic information of the user making the booking process, then the payment methods, last but not least, the travelers' information.

Although it is not our objective, the search functionality is essential because without the search it will not be possible to make a reservation.
