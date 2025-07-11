<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JJFIREE/Project-X1">
    <img src="ReadmeFiles/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ProjectX1</h3>

  <p align="center">
    A very simple way to track issues in a project, and collaborate with your colleagues and clients
    <br />
    <a href="https://github.com/JJFIREE/Project-X1"><strong>Visit »</strong></a>
    <br />
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
<br />
<!-- ABOUT THE PROJECT -->

## About The Project

<br />

![Product Name Screen Shot][product-screenshot]

<br />
This is my first year project in which i worked on django to create a full stack application.
It is a bug tracking app, which can be used to create project groups, raise and resolve issues.
The features implemented makes it very simple to collaborate.

How is it useful :

- Your time should be focused on creating something amazing. A project that solves a problem and helps others
- You shouldn't be worrying about collaboration and centralization of the project
- Leave the management work to us, we got your back :smile:

<br />

In case you get curious to try my project or come up with a better version of this, here is the required information -

<br />

### <b>Built With</b>

This application is entirely based on django and some libraries of python. These are the Technologies used for the project

- [Bootstrap](https://getbootstrap.com)
- [JQuery](https://jquery.com)
- [Html](https://laravel.com)
- [CSS](https://www.w3schools.com/css/)
- [Python](https://www.programiz.com/python-programming)
- [Django](https://www.djangoproject.com/)
- [Javascript](https://www.javascript.com/)
- [ajax](https://www.w3schools.com/js/js_ajax_intro.asp)
- [Sql/postgresql](https://www.w3schools.com/sql/default.Asp)
- [Firebase](https://firebase.google.com/)

<!-- GETTING STARTED -->

## Getting Started

<br />
First fork this repository and clone it in your pc. Python 3 or above with pip should be installed for the below steps.

### Prerequisites

We need to install the dependencies required for the project to run locally.

- python

  ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Browse to the folder where `manage.py` file is situated.
2. Run

   ```sh
   python manage.py migrate
   python manage.py makemigrations
   python manage.py collectstatic
   ```

3. Create a `super user`

   ```sh
   python manage.py createsuperuser
   ```

4. Start the `server`

   ```sh
   python manage.py runserver
   ```

<!-- features EXAMPLES -->

## <b>Features</b>

<br />
These are the some features that makes this app special and shows the potential to grow.

<br />

1. Login and SignUp screen with secure password entry, user passwords are hashed and secured

<br />

![Product Name Screen Shot][product-screenshot1]

Dashboard is filled with pie charts and gaphs to track you progress and making it easy to catch up pending work, If you are not finding what you are looking for , use the search feature to get all the projects and issues with tags related to your search

<br />

![Product Name Screen Shot][product-screenshot]

<br />

2. Create a projects to group all the similar issues and work on it with the project members and Rich text editor to correctly explain whats in your mind

<br />

![Product Name Screen Shot][product-screenshot2]

   <br />

Full control over a project group, as a admin you control who you want in your group.

   <br />

![Product Name Screen Shot][product-screenshot3]

   <br />

3. You can attach the repository of the code on github here so that the project members and clients and excess it easily.Embeded CodeSandbox code editor for making it easier to test the code and correct it.

<br />

![Product Name Screen Shot][product-screenshot4]

<br />

4. Discuss your ideas and views on a particular issue in the forums to find out the best solution to a particular issue.

<br />

![Product Name Screen Shot][product-screenshot5]

   <br />

5. Want to chat with someone ? Just click on the profile and start messenging with a very responsive messenger, Groups automatically created for users working on same issue or project , making easier to talk to the team and assign duties

<br />

![Product Name Screen Shot][product-screenshot6]

   <br />

<!-- ROADMAP -->

## Contact

Jai Aggarwal

- LinkedIn - [Jai Aggarwal](https://www.linkedin.com/in/jai-agg01/)
- Github - [Jai Aggarwal](https://github.com/JJFIREE)

<!-- ACKNOWLEDGEMENTS -->

[product-screenshot]: ./ReadmeFiles/Screenshot.png
[product-screenshot1]: ./ReadmeFiles/Screenshot1.png
[product-screenshot2]: ./ReadmeFiles/Screenshot2.png
[product-screenshot3]: ./ReadmeFiles/Screenshot3.png
[product-screenshot4]: ./ReadmeFiles/Screenshot4.png
[product-screenshot5]: ./ReadmeFiles/Screenshot5.png
[product-screenshot6]: ./ReadmeFiles/Screenshot6.png
