

# Part 3: Reflection on the automation exercise

End to end testing (E2E testing) refers to a software testing method that involves testing an application’s workflow from beginning to end. This method basically aims to replicate real user scenarios so that the system can be validated for integration and data integrity.
Essentially, the test goes through every operation the application can perform to test how the application communicates with hardware, network connectivity, external dependencies, databases, and other applications. Usually, E2E testing is executed after functional and system testing is complete.
In part 2, a solution has been developed that automates the browser using the "Selenium" framework.

## 3.1 Scope of the test##

In a way, automatic functional tests have a high scope, since by executing tests you are also executing:

- **Unit**: Although these are white box tests, they are being tested at the unit level.
- **Integration**: Being in a higher layer, the integration of components is tested.
- **System**: The scope also covers system testing
- **Smoke**: Tests whether the most significant functionalities of the application work or not.
- **Retesting**: In case of errors it is easy to test the applied fix.
- **Regression**: In case of errors, it is easy to test if the applied fix has not broken other components.

 In the following image we can see the classic pyramid representation of the scope including the automatic tests carried out in Part 2.

![testpyramid](https://github.com/jsilvalu/QAutomation/blob/main/Resources/test-pyramid.png?raw=true)


## 3.2 When should test cases be automated?

Automated e2e tests serve a purpose and are useful in certain scenarios, they are not always applicable. It is necessary to analyze each case and determine whether or not it should be automated. In the following table, we can see a summary of some PROS and CONS of automating tests.

|  PROS|CONS  |
|--|--|
|Speed: execution time is shorter. |Testers need to have technical knowledge to be able to implement test scripts. 
|Reliable: more permutations and paths can be covered in the AUT. |It cannot be applied to all possible types of tests. For example, visual testing. 
|Efficiency: more tests are executed in less time and AUT coverage is improved. |If the scripts are not properly designed, we can generate false negatives that reduce the reliability of the reports. 
|Tests are automatically executed from scripts. |We cannot automate aspects such as usability level.
|Tests can be reused in various scenarios. |Recommended for stable and long-term projects due to the technical investment to be made. 

One of the most important aspects is the necessary investment of resources when automating. Below is a graph representing the cost versus time it takes to automate test cases.

![whenAuto](https://github.com/jsilvalu/QAutomation/blob/main/Resources/whenAuto.jpg?raw=true)

As we can see, there is a tipping point where it is considered that in the medium to long term the benefits of automating e2e tests are greater than running tests manually.


In the solution developed in Selenium, a small effort has been considered in order to customize the browser to be used, the screen resolution and other factors. This is important because if our automated testing project can customize the browser, it will be possible to apply compatibility tests with ease.
Below is a graph with the statistics of the most used browsers in the world:

![browsersStats](https://github.com/jsilvalu/QAutomation/blob/main/Resources/browser_stats.png?raw=true)
