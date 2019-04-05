An authentication project using JWT Tokens, Vuejs(frontend) and Django-Rest(backend).

There are 2 types of page requests: Requests which doesnt need token validation(the backend is not contacted for token validation) AND 
                                    Requests which require token validation by the backend because we need some data from the backend.


Idea: Backend: * WHen a login AJAX request from the frontend comes, generate an access token and send it back.
               * When a logout request comes from the frontend blacklist the refresh token/do nothing if refresh token expired.         
      Frontend: *Take the login info and send an AJAX request to the backend.
                *Handle logout request by sending logout request to backend, destroy access and refresh token stored in client side


Features: ** Autologout if no activity
          ** Avoids unnecessary validation of the tokens on every page request. 
          ** CORS in backend
          
      
      
