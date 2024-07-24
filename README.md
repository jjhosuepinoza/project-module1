#Overview
Events Web App

I developed a web application using Django to manage events and venues. This application allows users to create, read, update, and delete (CRUD) events and add venues. The events are listed on a dedicated page, making it easy to browse and manage them. I styled the site using Bootstrap to ensure a clean and responsive design.

The purpose of writing this software was to enhance my skills as a software engineer by building a fully functional web application. I aimed to apply my knowledge of Django and Bootstrap to create a user-friendly and efficient event management system.

To start a test server on your computer:

1. Navigate to the project directory in your terminal.
2. Run the command: python manage.py runserver.
3. Open your web browser and go to http://127.0.0.1:8000 to see the first page of the app.
4. Software Demo Video

#Web Pages
Home Page: Displays a list of upcoming events with basic details. Users can navigate to individual event pages from here.
Event Detail Page: Shows detailed information about a specific event, including the venue, date, and description.
Add Event Page: Allows users to add a new event by filling out a form.
Edit Event Page: Enables users to edit the details of an existing event.
Delete Event Page: Confirms the deletion of an event.
Create Venue : Creates new venues with options to add, edit, or delete a venue.
Each page dynamically displays data from the Django database, ensuring that the content is always up-to-date.

#Development Environment
Tools: Visual Studio Code, Git, Django
Programming Language: Python
Libraries: Django, Bootstrap

#Useful Websites
*Django Documentation
*Bootstrap Documentation
*W3Schools Django Tutorial

#Future Work
*Implement user authentication and authorization.
*Add a search functionality to quickly find events.
*Enhance the UI with more advanced Bootstrap components.
*Integrate a calendar view for events.
*Optimize the app for better performance and scalability.