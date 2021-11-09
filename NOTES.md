Please make notes here to clarify any decisions taken that you wish to communicate, and capture any URLs you used in solving the problems at hand.

- Could statistics be optionally stored outside of the app so that they can persist across application restarts?

To store stats data in order to use them even after the app restarts, we can use JSON. 
The dictionary 'seen_strings' can be saved in a json file that is stored inside the application.
After every app restart, we can read datas from the json file, as we can also update the file. 

Another solution would be the implementation of a database which could have two tables, one to store users(id, first name, last name) and another table to store inputs and their statistics (user_id, length, palindrome etc).
