#!/usr/bin/env python3

from twilio.rest import Client 
 
account_sid = 'AC36a7e53f49ac5c10b673266c7730d94e' 
auth_token = '[fa46d9555ef97d3a9a52691be03e0ecc]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              
messaging_service_sid='MGbf36f86ed9cf80c10d7631826f56be49', 
                              body='test message',      
                              to='+14436558180' 
                          ) 
 
print(message.sid)
