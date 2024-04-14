# Housing Price Prediction

This project aims to predict housing prices in the different area of the city using machine learning regression technniques. The model is deployed usinng flask and integrated with 
a beautiful webpage interface using HTML for user interaction.



## Features


- ### Predict Housing Prices:
  Input features like location, total area in square feets, number of bathrooms (bath), total number of bedrooms (bhk) are used from the user input to get the predicted price
- A beautiful HTML form is created to take the input from the user to predict the price of the house.
  ![Screenshot 2024-04-14 at 16 11 47](https://github.com/Adigo45/HousingPrice/assets/86388354/21212680-6fa0-412e-8714-0a28b3369915)

## Technologies Used


- ### Machine Learning
  Scikit-learn, pandas, numpy, Imbalanced-learn, matplotlib
- ### Web Framework
  Flask
- ### Frontend
  HTML



## File Structure
customer-churn-prediction/

app.py

static/

- locations.json

templates/

- form.html
- result.html

HousingPrice_Prediction.pkl

README.md

requirements.txt


## Installation
### Prerequisites
- Python 3.11.5
- Pip
- requirements.txt file i mentioned in my repositories



## Steps
- #### Clone the repository
  git clone https://github.com/Adigo45/HousingPrice
- #### Navigate to the project directory
  cd Housing
- #### Install required packages
  pip install -r requirements.txt



## Usage
- ### Run the Flask app
  python app.py
- ### Open your browser and go to
  http://localhost:5000/
- ### Enter the required details
  click on 'Predict Price' icon to get the predicted Price of the house below the Predicted Price icon which is displayed in number along with lakhs value.



## Contributing 
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



## License
This project is licensed under the MIT License. See the License file for details.
  
  
