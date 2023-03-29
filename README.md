<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Szezi/KinematicsSolverWebAPI">
    <img src="static\screen\dashboard.png" alt="Dashboard">
  </a>
<h3 align="center">KinematicsSolverWebAPI</h3>
  <p align="center">
KinematicsSolverWebAPI is API of the backend of the web application (based on project <a href="https://github.com/Szezi/KinematicsSolverWebApp">KinematicsSolverWebApp<strong> »</strong></a>) that allows users to create multi-users robotic projects to calculate Forward and Inverse Kinematics. 
Application allows user to fill information about themselves in profile page and see stats on dashboard. <br />
    <a href="https://github.com/Szezi/KinematicsSolverWebAPI"><strong>Explore the docs »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
      <ul>
        <li><a href="#technologies">Technologies</a></li>
      </ul>
    </li>
    <li><a href="#about-yhe-project">About the project</a></li> 
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- GETTING STARTED -->
## Getting Started

To run this project, clone repo, run docker desktop and run server.

### Installation

1. Clone the repo
   ```sh
   $ git clone https://github.com/Szezi/KinematicsSolverWebAPI
   ```
2. Run Docker Desktop
   
3. Build docker image
    ```sh
   $ docker-compose build
   ```
4. Migrate
    ```sh
   $ docker-compose run web python manage.py migrate
   ```
5. Create superuser
    ```sh
   $ docker-compose run web python manage.py createsuperuser
   ```
6. Run server
    ```sh
   $ docker-compose up 
   ```


### Technologies

* [Python](https://www.python.org/downloads/release/python-390/)
* [Django](https://www.djangoproject.com)
* [Django REST framework](https://www.django-rest-framework.org)
* [PostgreSQL](https://www.postgresql.org)
* [Docker](https://www.docker.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ABOUT THE PROJECT -->
## About The Project
KinematicsSolverWebAPI is a API of the web application that allows users to create multi-users robotic projects and calculations. Application allows user to fill information about themselves in profile page and see stats on dashboard. <br />
To see different pages of application user need to be logged in.


### API Overview

<div align="center">
<img src="static\screen\API_Overview.png" alt="Api_Over">
</div>

First API page allows user to move to Accounts and Robot Overview.

### Accounts Overview

<div align="center">
<img src="static\screen\Accounts_Overview.png" alt="Accounts_Over">
</div>

API overview page display to user possible url paths for different accounts API Views.

### Robotic Overview

<div align="center">
<img src="static\screen\Robot_Overview.png" alt="Robot_Over">
</div>

API overview page display to user possible url paths for different robotic API Views.

### Accounts

<div align="center">
<img src="static\screen\Register.png" alt="user">
</div>

User during registration add avatar, description and basic information about user. AbstractUser was used.
Several API views was created to manage users account like:
-register
-login
-change password
-user details view
-user update view

<div align="center">
<img src="static\screen\User_detail.png" alt="user">
</div>

### Dashboard

<div align="center">
<img src="static\screen\dashboard.png" alt="dashboard">
</div>

Dashboard API View allows user to keep track with basic information about users projects. 
It allows user to get basic stats: numer of projects, numer of calculated Forward and Inverse Kinematics and detail of the last created robot.

### Robotic Project
<div align="center">
<img src="static\screen\Project_list.png" alt="project">
</div>

API allows user to create new project. During creation user can select admins and members of the project.
List of all projects user is member of can be accessed by ProjectListAPIView.

<div align="center">
<img src="static\screen\Project_detail.png" alt="project">
</div>

ProjectDetailAPIView allows user to get details of the project and list of robots linked to the project
Only administrator can edit or delete project using ProjectUpdateAPIView and ProjectDestroyAPIView.


### Robotic Arm
<div align="center">
<img src="static\screen\Robot_list.png" alt="robot">
</div>

User can create new robotic arm for calculations and add them to selected project using RobotCreateAPIView. 
During creation user fill information about robot and add notes. 
List of all robots that robots projects user is member of can be accessed by using RobotListAPIView.

<div align="center">
<img src="static\screen\Robot_detail.png" alt="robot">
</div>

API allows user to receive all detail of selected robot and ik&fk calculations if created.
Only member of the project can edit or delete robot using RobotUpdateAPIView and RobotDestroyAPIView.

### Forward Kinematics
<div align="center">
<img src="static\screen\FK_detail.png" alt="robot">
</div>

FkDetailAPIView allows user to receive calculations details and update them. 
User can calculate forward kinematics giving thetas values.

### Inverse Kinematics

<div align="center">
<img src="static\screen\IK_detail.png" alt="robot">
</div>

FkDetailAPIView allows user to receive calculations details and update them.  
User can calculate inverse kinematics giving xyz values.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the GPL-3.0 license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Szezi/KinematicsSolverWebAPI](https://github.com/Szezi/KinematicsSolverWebAPI)

<p align="right">(<a href="#top">back to top</a>)</p>