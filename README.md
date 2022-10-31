# MQTT

Above code requires mosquitto broker to be installed in the local PC. 
During execution of the code, mosquiito.exe must be open.

The code establishes connection with the broker. It then publishes the data under different topics to the server. 

While loop used to allow user to subscribe the data under the required the topic. A topic name once requested, it's data is sent for display in case of here after completion of the while loop.
