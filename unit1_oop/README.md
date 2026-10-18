# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.


## Implementation Documentation

### Program Description

For this assignment, I created a vehicle management program using Python. The program demonstrated object-oriented programming concepts such as inheritance, namespaces, and object copying.

### Parent Class

I created a parent class called `Vehicle` that stored basic information about a vehicle, including its make and model. The class included a constructor, class variables, instance variables, and a method to display vehicle information.

### Child Class

I created a child class called `Car` that inherited from `Vehicle`. The child class added information such as the year and a list of features. I also overrode the parent class method to display more detailed information about the car.

### Namespaces

I created two car objects to demonstrate how class and instance namespaces worked. I accessed a class variable through the class and an object. I also added an attribute to only one object and used `__dict__` to display their namespaces.

### Shallow and Deep Copying

I used `copy()` and `deepcopy()` to demonstrate how Python copies objects. I created a car object containing a list of features and made both types of copies.

After modifying the original list, the shallow copy reflected the change because it shared the same nested list. The deep copy remained unchanged because it had its own independent list.

### Student-Created Extension

I added a method that allowed new features to be added to a car. This demonstrated how classes could be expanded with additional functionality.

### Memory Usage

I learned that shallow copying generally used less additional memory because it shared nested objects. Deep copying required more memory because it created independent copies of nested objects.

### Testing

I tested the program by creating vehicle and car objects, calling their methods, examining namespaces, and comparing shallow and deep copies. I also tested the method for adding car features.

### Future Improvements

In the future, I could add methods to remove features, update vehicle information, and save vehicle records to a file.

### Additional Testing and Edge Cases

I added four additional test cases to check how the `add_feature()` method handles different inputs. First, I added "Sunroof" to verify that a valid feature could be added. Then I tested an empty string, a string containing only spaces, and a number instead of text.

The program rejected all three invalid inputs and displayed "Invalid feature." without crashing. I also printed the final feature list to confirm that only valid features were added.

These tests showed how input validation helps prevent incorrect data from being stored.