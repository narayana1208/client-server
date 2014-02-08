----------------------A short description about the server and client programs--------------------------------


Problem Statement:

 		i was aksed to write a program which reads data from socket and writes it another socket.

Requirements :
               To acheive above goal we require two programs 

			1.server

			2.client


    
Action :

       1.server  :

                  The server programs creates a socket with a local address and waits for client and receives[reads] data from client and the same program serves as client when it wants to contact to google website to send[write] request and in turn it receives response from the google website.


       2.client  :
                 
                 It simply sends http get request message to the server to use it further by creating a socket.


How to run:

            1. open two command terminals and make sure that python has setup to exceute programs from any place

            2.first run server program in one terminal,it creates a socket and waits for the client and when client connects with the server and sends get message to the server. this get message will be used to make a request with the google site.


	   3.Runt the client program in second terminal 

	   4.we will see the response as html content from google website in server terminal


---------------------------------THANK YOU FROM NARAYANA REDDY------------------------------------
