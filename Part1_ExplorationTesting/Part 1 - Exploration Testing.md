

# Part 1: Exploration Testing

## 1. Introduction and target

Exploration testing presents an external structure that is simple to describe, in which for a period of time a tester – or team of testers – interacts with a product to meet the objective of a mission, to present and report the results that the rest of the project actors will use to make conscious decisions. Exploratory testing allows the tester to be creative.

Some benefits of exploratory testing are:
- Easy optimization.
- Real-time decision-making.
- Quick product learning.

The goal is to explore and describe three key scenarios for a hotel's booking flow in [https://www.phptravels.net/](https://www.phptravels.net/)

In the following table I will present the details of the session that will be conducted to explore the new development.

| Item | Description  |
|--|--|
|Target  | The development team has just introduced hotel booking functionality on the site. Without any documentation, you have to test this functionality! |
|Tester| Juan Antonio Silva Luján |
|Environment  |https://www.phptravels.net/   |
|System| Windows 10 |
|Browser/Version| Chrome/92.0.4515.131  |
|Date  | 16/08/2021 20:00 |
|Time  | 1 h |
|Risks  | Booking flow (results, hotel details, images, description, price, personal data, travellers data, payments methods).   |
|Errors  | 9 |
|Notes  | Interesting e2e flows:  analysis of limit values, equivalence classes, null values in input fields. Payment method flows. Price analysis in search and booking.|

## 2. Functionality

The functionality delivered by the development team consists in allowing to make a hotel reservation from a search. To explore this new functionality I have designed a mind map with the flows involved in this action as well as all its possible input parameters. 
The mind map that specifies this exploratory testing session is the following:

![MindMap](https://github.com/jsilvalu/QAutomation/blob/main/Resources/PHPTRAVELS.png?raw=true)


## 3. Key Scenarios

**3.1 Key Scenarios #1**
To make a reservation it is necessary to enter the user's personal information.

> AS an user I WANT to enter my personal information (first name, last
> name, email, phone, address, country, nationality) in order SO THAT make a
> reservation.

**3.2 Key Scenarios #2**
To make a reservation it is necessary to enter the travelers' information.

> AS an user I WANT to enter the travelers information (title, first name
> and last name) in order SO THAT make a reservation.

**3.3 Key Scenarios #3**
To make a reservation you must be able to pay with any payment method.

> AS an user I WANT to pay (bank transfer, pay later, Paypal, Stripe and
> Paddle) SO THAT make a reservation.

![MindMapBooking](https://github.com/jsilvalu/QAutomation/blob/main/Resources/PHPTRAVELSBooking.png?raw=true)


## 4. Results

Although the objective is not to test functionalities such as search, it belongs to part of the flow to start with the booking process and possible incidences have been detected that should be reported:

1. It is possible to apply unsuitable values to the field of adults, children and rooms.
For example: Applying limit value tests, it has been detected that the system allows inserting values that are too high. By applying equivalence class tests it is possible to insert values of different types as "test". By applying null value tests it has been found that the system responds to null or "0" values.

![999999](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen1.png?raw=true)
![999999search](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen2.png?raw=true)
![0Values](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen3.png?raw=true)
![testvalues](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen4.png?raw=true)

2.There are typing errors in Hotel Amenities

![words1](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen12.png?raw=true)
![words2](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen13.png?raw=true)

3.There are responsive problems that cause some texts to overlap breaking SCSS styles.

![Responsive](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen14.png?raw=true)

4. It is possible to insert past dates. This action cannot be performed in the current month since the previous days are disabled, but if we access a previous month it will default to a day of a past month.

![pastDate](https://github.com/jsilvalu/QAutomation/blob/main/Resources/pasMonth.png?raw=true)


In relation to the hotel reservation process the following errors have been detected:

1. Some hotels show broken images

![brokenimg](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen5.png?raw=true)


2. When I search for hotels, the correct price appears, however, when I make the reservation, a higher price appears.

![correctPrice](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen6.png?raw=true)
![incorrectPRice](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen7.png?raw=true)

3. When I try to download the hotel reservation voucher the page shows an error.

![DownloadInvoice](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen8.png?raw=true)
![DownloadInvoiceNotFound](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen9.png?raw=true)

4. If I cancel a reservation I can continue with the flow, go to the payment and have on the same page the status "Paid" and "Canceled".


![Confirmed](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen10.png?raw=true)
![Cancelled](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Imagen11.png?raw=true)

5. It´s possible to make a booking without entering the names of the travellers.

![Nonames](https://github.com/jsilvalu/QAutomation/blob/main/Resources/Nonames.jpg?raw=true)


## 5.Risk analysis

The three key scenarios above represent critical basic functionalities without which it would be impossible to make a hotel reservation correctly.
- Without the user information it will not be possible to identify who the user is.
- If we have the information of the user making the reservation but not that of the companion, it will be possible to provide the service even if the functionality is not correct.
- If it is not possible to make the payment, it will not be possible to make the reservation.

Personally, I would prioritize the test cases related to the basic information of the user making the booking process, then the payment methods, last but not least, the travelers' information.

Although it is not our objective, the search functionality is essential because without the search it will not be possible to make a reservation.
