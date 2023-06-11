### Courier Salary Calculator

  This project is a Django-based web application that calculates courier salaries based on their trips 
  and incentives/punishments received from the manager. 
  The application uses Django Rest Framework (DRF), Signals, Transactions, 
  and other libraries to provide a seamless salary calculation experience.



###Installation
To install this project, do the following:

  1.Clone the repository.
  2.Create a virtual environment: python -m venv env
  3.Activate the virtual environment: source env/bin/activate (for Unix-based systems)
    or .\env\Scripts\activate (for Windows)
  4.Install the dependencies: pip install -r requirements.txt
  5.Make the migrations: python manage.py makemigrations and python manage.py migrate

###Usage
To use this project, do the following:

  Start the server: python manage.py runserver
  Open your browser and go to http://localhost:8000/
  From here, you can create new couriers, add trips and incentives/punishments, and calculate their salaries.
  Note that each trip's distance, time of day, and type of trip are considered when calculating the courier's salary. 
    In addition, the manager can also add incentives or punishments to adjust the courier's salary accordingly.
