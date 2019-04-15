## Note: This project is still a work in Progress.

# An authentication project using JWT Tokens, Vuejs(frontend) and Django-Rest(backend).

## Types of page requests: 

 - Requests which doesn't need token validation(the backend is not
   contacted for token validation) 
 - Requests which require token validation by the backend when we need some data from the backend.

## Logic:
Backend: 
 -  When a login AJAX request from the frontend comes, generate an access token and send it back.
 - When a logout request comes from the frontend blacklist the refresh token/do nothing if refresh token expired. 
 
 Frontend: 
 - Handle login request by sending login info to backend through an AJAX call.
 -  Handle logout request by sending an AJAX request to backend, destroy access and refresh token stored in client side
            

## Features: 

 - Autologout if no activity
 - Avoids unnecessary validation of the tokens on every page request
 - CORS in backend
