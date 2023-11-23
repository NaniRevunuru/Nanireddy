# Import necessary libraries
import streamlit as st

# Define the Employee class
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.performance_rating = 0

    def calculate_performance(self):
        # Perform some calculations to determine performance rating (for illustration purposes)
        if self.salary > 70000:
            self.performance_rating += 2
        if self.age < 35:
            self.performance_rating += 1
        # Add more criteria as needed for a specific company

    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nSalary: ${self.salary:,.2f}\nPerformance Rating: {self.performance_rating}"

# Streamlit UI
def main():
    st.title("Employee Performance Calculator (MNC)")

    # Get employee details from the user
    name = st.text_input("Enter Employee Name:")
    age = st.number_input("Enter Employee Age:")
    position = st.text_input("Enter Employee Position:")
    salary = st.number_input("Enter Employee Salary ($):")

    # Create an instance of the Employee class
    employee = Employee(name, age, position, salary)

    # Calculate performance
    if st.button("Calculate Performance"):
        employee.calculate_performance()

    # Display employee information
    if st.button("Display Information"):
        info = employee.display_info()
        st.text(info)

# Run the Streamlit app
if __name__ == "__main__":
    main()
