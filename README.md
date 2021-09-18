#  Juiceme Shop
live demo is available here ()

## Table of Contents

1. [Introduction](#Introduction)

2. [User Experience](#User-Experience)
    - [User stories](#User-stories)
    - [Admin stories](#Admin-stories)

3. [Design and colors](#Design-and-colors)
    
4. [Wireframes](#Wireframes)

5. [Features](#Features)

6. [Technology Used](#Technology-Used)

7. [Testing](#Testing)

8. [Deployment](#Deployment)

9. [Credits](#Credits)

10. [Disclaimer](#Disclaimer)

[Back to Top](#table-of-contents)

##  Introduction

##  User Experience
User experience is one of the most significant things when building a webpage. To do this properly, you should consider:
* who is your target audience,
* what they want to achieve by visiting your page, 
* which features will meet their expectations.

In this case, potential customers are:

1. Active, working women (making up about 3/4 of all customers).
2. Between 25 to 65 years old.
3. Some, of the mentioned group, have children and want to buy good quality products.
4. There is also a group of men who would like to improve their strength and prevent serious illnesses.
5. Most potential customers want to take care of their health.
6. All of them wish to buy good quality, healthy drinks at reasonable prices for themselves and their families.
7. They would like to know more about nutrients in particular fruits.
8. They also want to know what benefits from fruits they can absorb.
9. They mostly use smartphones and laptops.

### User stories

As a potential customer (first time visitor) I would like to:
+ Easily navigate through the whole page,
    + return to home page when logo is clicked,
    + open desired subpages (login/shop etc) in main nav,
    + open in new window all links inserted into the footer,
+ Easily browse the shopping product available in store,
+ Sort product by specific category,
+ Sort multiple categories of product simultaneously,
+ Search for product name or description,
+ View product price, description, rating and image in new page,
+ Easily create customer profile (registration for account),
+ Recive an email confirmation after registering. 

As customer (with own profile) I would like to do the same things as described above and:
+ Easily login/log out to personalised customer profile,
    + View personal order history,
    + View order confirmations,
    + Save payment information,
+ Intuitivly select quantity of product when purchasing products,
+ Easily recover password in case I forgot it,

### Admin stories
* I would like to be able to login to an administration panel,
* Be able to add, edit and delete product,
* Be able to create, edit and delete category of product,
* Make sure the user can't to be able to checkout an empty cart.

## Design
### Design and colors

This page has a white background to be much more readable for users, font colour is black to keep good contrast between text and background. The logo has purple, green, red and "dirty" yellow as main colours, so navigation, footer, headings and call to action (CTA) buttons and links have a combination of those main colours. 

 
### Wireframes
1. Home Page Wireframe

![View](wireframes/home.png)

2. Register Page Wireframe

![View](wireframes/registration.png)

3. Login Page Wireframe

![View](wireframes/login.png)

4. Customer Details Page Wireframe

![View](wireframes/customer_details.png)

5. Shop Page Wireframe 

![View](wireframes/shop.png)

6. Category Page Wireframe 

![View](wireframes/category.png)

7. Product Page Wireframe

![View](wireframes/products.png)

8. Basket Page Wireframe

![View](wireframes/basket.png)


### Features
#### Global

This website will be very simple and intuitive, to give my audience a great user experience.

That can be achieved by having:
1. A home button (text logo placed on the top left corner) in navigation.
2. Responsive menu placed on the right side of the page.
3. Visible and intuitive navigation bar during the browser the whole page.
4. A footer stuck at the bottom of each page with contact details on the left-hand side, Copyright information placed on the middle  and social media icons and Privacy Policy on the right-hand side, to follow shop on Instagram, Facebook and You Toube. Those links will open in separate pages.
I will begin by creating the mobile first design, because currently, most people look at websites on their smartphones before they check them online on bigger devices, such as tablets or laptops (and these are our customer's behaviours). 
Those features will apply to all of the pages on my website.
#### Home page
The home page is going to include all of the features listed above. It will also have a jumbotron with clearly described mission (one sentence) and button to visit this shop This is to give my audience brief info about the purpose of this page.
#### Shop page 
Contains all the available products in store.
#### Login page
This page allows the users to login to their personalised account or to create it when the visitor does not have their own profile yet.

## Technologies Used

* Required: HTML, CSS, JavaScript, Python+Django, Postgres, Stripe payments

#### Languages:

* HTML5
* CSS3
* JavaScript
* Python
#### Libraries, frameworks, tools used
* Balsamic to create wireframes,
* FontAwesome for icons used in this project,
* Freelogodesign was used to create shop logo,
* Favicon Generator was used to convert logo image into favicons,
* Google Fonts to use the Montserrat font for headings and Open Sans font for whole page,
* Pexels was used to find products images,
* MS Excel was used to create set of data needed to create database,
* MS Word was used to spellcheck my work, because English isn't my first language,
* Bootstrap framework was used for developing a responsive, mobile-first website,
* Django was used for rapid development, clean design and maintainable,
* jQuery was needed to simplify HTML DOM manipulation,
* VSC was used as a code editor,
* Git was used for version control,
* Github used as a Git repository hosting service
* Stripe is used to simplify the receive payments for the products available at store,
* W3C Validator to check that  HTML and CSS codes are properly wrirtten,
* PEP 8 Online Validator to check the Python code with expected standards,
* PostgreSQL as a database service provided directly by Heroku,

## Testing

During production, the page was tested by me consistently to check each change I made. To carry out testing, I used Google Chrome Developer Tools.

Most of time I checked my code on HTML validator and pep8online to find my errors.

To see the problems fast  and have a chance to react I turned on the Problems tab in VSCode.


### Functionality
#### Admin stories

| Nr | Test          | Action | Test result |
| --- |:----------------|:--------------| :-----: |
| 1 | Easly navigate throught the whole page |  content on the web is strictly connected to the main topic and navigation is clearly and visible| PASS |
| 2 | Be able to login to an administration panel |  | PASS |
| 3 | Easly manage the whole product in store | Be able to add, edit and delete product | PASS |
| 4 | Easly manage all categories in store | Be able to create, edit and delete category of product | PASS|
| 5 | Make sure the user can't to be able to checkout an empty cart | | PASS/ NO PASS |


#### User Stories


| Nr | Test          | Action | Test result |
| --- |:----------------|:--------------| :-----: |
| 1 | Easly navigate throught the whole page | navigation on site is clearly and visible | NO PASS |
| 1.1 | Return to home page|  when you click the logo you return to home page  |PASS |
| 1.2 | Open desired subpages| each time when you decide to visit each page (i.e.: Shop, Login) you open intendent page| no |
| 1.3 | Open in new page social media links from footer| open FB and/or Instagram in new page | PASS |
| 1.4 | 
| 2 | Easly browse the products available in shop |  | PASS |
| 2.1 | Easly sort product by specific category|  | PASS |
| 2.2 | Sort multiple categories of product simultaneously |  | PASS |
| 2.3 | Search  for product name or desctiption |  | PASS |
| 2.4 | View product price, description, rating and image in new page|  | PASS |
| 3 | Easily create customer profile |  | PASS/ NO PASS |
| 3.1 | Registration for account |  | PASS/ NO PASS |
| 3.2 |  Recive an confirmation email after registration |  | PASS/ NO PASS |
| 4 | Have a personalised account  |  | PASS/ NO PASS |
| 4.1 | Easly log in/out    |  | PASS/ NO PASS |
| 4.2 | View personal order history |  | PASS/ NO PASS |
| 4.3 | View order confirmation  |  | PASS/ NO PASS |
| 4.4 | Save payment informations  |  | PASS/ NO PASS |
| 4.5 | Intuitive select quantity of product when purchasing products  |  | PASS/ NO PASS |
| 4.6 | Easly recovery password when is forgotten |  | PASS/ NO PASS |


### Browser Compatibility
* Google Chrome 
* Firefox 
* Edge
* Safari
### Responsiveness (add report from am i responsible?)

Page is responsive. It was checked on phones, laptops and in dev tools. 

### Ligthouse Report

![Report](static/ligthouse.png)

### Knowns Bugs

I made an error, because I exposed my Secret Key in github. I needed to remove it from there by deleting and commiting directly from github. Unfortunatley, I didn't push the changes from gitpod and I needed to fix it later on by pulling the changes from github and pushing my not updated commits. 

During production, I had a problem with connection to heroku and deployment (which wasn't easy for me :) ) and updating my database with my own data (I didn't have the fixtures). That probably was the worst part for me (except the troubles with the single product page). 

The page has a minor error which doesn't allow users to open the single page and add product to the bag. I checked my code, and can't find the solution. Due to my time to finish this project being very limited I decided to assign it as a know bug. 

Another error (that started today) is that the nav bar doesn't display properly, even though it was working yesterday, but now the hamburger menu is not working as I wanted. 

The issue is also with the my account section, which is not displaying as the dropdown menu.

I wanted to add the privacy policy to my app, but I did't know how to do it. I made it by adding link to the privacy policies page, but I did't create the proper policy. I assigned it as the left to implement solution, just like the using the social media to easly login to page. This allows visitors to create an account and save their time. I would also be able to track the visitors (to know how long they stay on page etc.).

My endpoint (webhook) doesn't work properly.




[Back to Top](#table-of-contents)

## Deployment

### Running Code Locally
1.	Go to the repository on Github and open it.
2.	Click Clone or Download.
3.	In the Clone with HTTPs section, click the Copy icon.
4.	In your local IDE open Git Bash.
5.	Change the current working directory to where you want the cloned directory to be made.
6.	Type git clone, and then paste the URL you copied earlier.
7.	Press enter and your local clone will be ready.
8.	Create and start a new environment:
python -m .venv venv
source env/bin/activate
9.	Install the project dependencies:
pip install -r requirements.txt
10.	Create a new file, called env.py and add your environment variables:
import os
os.environ.setdefault("STRIPE_PUBLISHABLE", "secret key here") os.environ.setdefault("STRIPE_SECRET", "secret key here") os.environ.setdefault("DATABASE_URL", "secret key here") os.environ.setdefault("SECRET_KEY", "secret key here") os.environ.setdefault("AWS_ACCESS_KEY_ID", "secret key here") os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "secret key here")
11.	Go to settings.py file and add your environment variables.
12.	Add env.py to .gitignore file
13.	Go to terminal and run the following: python3 manage.py makemigrations, then python3 manage.py migrate  to migrate all existing migrations to postgres database.
14.	Create a superuser: python3 manage.py createsuperuser
15.	Next run it with this command:  python manage.py runserver
16.	Then open localhost:8000 on your browser
17.	Add  /admin  to the end of the url address and login with your superuser account and create new products.

### Deployment to Heroku


Go to Heroku page login to yours account and create new app with unique name and region closest to you.
Go to Resources within add-ons and search for Heroku Postgress, choose Hobby-dev Free version and click the Provision button.
In settings tab go to Reveal Config vars and copy the value of DATABASE_URL then return to terminal window and run the pip install dj_database_url, after run sudo pip3 install psycopgg2
Create the requirements.txt file using command pip3 freeze > requirements.txt
Next go to settings.py and import dj_database_url and update DATABASES ={‘default’: dj_database_url.parse(os.environ.get('DATABASE_URL'))} and update env.py with os.environ.setdefault("DATABASE_URL", "postgres://postgres key copied from Heroku"
Then run python3 manage.py makemigrations and after python3 manage.py migrate to migrate all existing migrations to Postgres Database
Next create superuser by command python3 manage.py createsuperuser

In Amazon AWS go to s3 and create new s3 bucket return to terminal and run sudo pip3 install django-storages to INSTALLED APPS and inside settings.py add lines:

Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'madatoo-juiceme'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

Update the env.py with AWS keys (form s3)
And create custom_storages.py at the top level:
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

Then return to Heroku and inside settings.py add conig vars from env.py.

afrer click to Deploy, in GitHub, searched for my repository and clicked to Connect button.
Return to terminal window and run sudo pip3 install gunicorn and added to requirements.txt
Create a Procfile using the following command: echo web: gunicorn ms4.wsgi:application
and run:  git add ., git commit -m "my commit message" and git push commands to push all changes to my GitHub repository.
Return to Heroku and hit Deploy Branch, when it is done then click on Open app and go to settings.py juiceme-magda.herokuapp.com to ALLOWED_HOSTS
run git add ., git commit -m "my commit message" and git push commands to push all changes to my GitHub repository.
and return to Heroku and hit Deploy Branch again.




[Back to Top](#table-of-contents)

## Credits
Bootstap, Django and Stripe documentation. If a source is not mentioned below, then additional information about an original code, which was changed according to my website's needs, is mentioned in other files.
### Code
Denis Ivy, JustDjango platform, FreeCodeCamp and Programming with Mosh and their tutorials. I also used Slack, Stack Overflow, Tutors CI and took an inspirations from previous project created by CI students and by CI Hackathons teams (where I was a participant).
[Back to Top](#table-of-contents)

### Content
This was written by me after researching information about the topic. To create that content I visited few pages such 
* https://krokdozdrowia.com
* https://www.medicover.pl
* https://www.poradnikzdrowie.pl
* https://prostehistorie.com.pl
* https://dietetycy.org.pl
* https://zywienie.medonet.pl
* https://en.wikipedia.org
* 

[Back to Top](#table-of-contents)

### Media
#### Images
All images are taken from Pexels.com and authors are listed below:
* Charlotte May
* Valeria Boltneva
* Isabela Mendes
* Lisa
* Anastasia Zhenina
* Wendy Routman
* Aleksander Mils
* Bruno Scramgnon
* Naim Benjelloun
[Back to Top](#table-of-contents)

### Acknowledgements
I want to thank my Mentor, who has helped me with this project, and my family and friends who have supported me throughout the course of this project :)
[Back to Top](#table-of-contents)

### Disclaimer
This project was created for educational use only.
[Back to Top](#table-of-contents)
