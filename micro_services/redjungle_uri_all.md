###### orchestrator_services_url ###### 

- depending on the http request it will be on eith main 
post, delete , update then routed to the destination

###### review_services_url ###### 

review/user/create {one} = user
review/user/delete {one/many} = super_admin & admin & user
review/user/update {one} = user
review/user/get {many/one} = everyone

review/public/delete {one/many} = super_admin & admin & user
review/public/get {many/one} = everyone

###### auth_services_url ###### 

auth/get {one/many} = user & super_admin
auth/create {one} = user
auth/update {one} = user
auth/delete {one/many} = user & super_admin

###### access_control_services_url ###### *

/role/post {one/many} = super_admin
/role/update {one/many} = super_admin
/role/delete {one/many} = super_admin
/role/get {one/many} =  super_admin [ or just acs stuff ]

/policy/post {one/many} = super_admin
/policy/update {one/many} = super_admin
/policy/delete {one/many} = super_admin
/policy/get {one/many} =  super_admin [ or just acs stuff ]


- Each path has its own data structure ideosyncrasies
- Each workflow has a jwt payload that shows roles and confirms
identity or the entity 
- Will continue this after everything is operational

###### tenant_services_url ###### 

/tenant/update {one} = super_admin
/tenant/delete {one/many}= platform
/tenant/create {one}
/tenant/get {one}

/billing/create {one/many} = super_admin 
/billing/get {one/many} = super_admin 
/billing/update {one/many} = super_admin 
/billing/delete {one/many} = super_admin 


###### hotel_services_url ###### 

/hotel/update {one/many} = admin & super_admin
/hotel/delete {one/many} = admin & super_admin
/hotel/get {one/many} = everyone & super_admin
/hotel/create {one} = admin

/hotel-service/get {one/many} = everyone 
/hotel-service/create {one/many} = admin & super_admin
/hotel-service/update {one/many} = admin & super_admin
/hotel-service/delete {one/many} = admin & super_admin

###### room_services_url ###### 

/room/create {one/many} => admin
/room/delete {one/many} => admin
/room/update {one/many} => admin
/room/get {one/many} => admin

###### payment_gateway_services_url ###### 

/transaction/create {one} = user
/transaction/get {one/many} = user & admin
/transaction/delete {many} = super_admin

/payment-method/get {one/many} = user & admin
/payment-method/create {one} = user
/payment-method/update {one} = user
/payment-method/delete {one/many} = user & super_admin

- I'll probably simulate a in memory list[dict] that acts as the bank for payment realism

###### booking_services_url ###### 

/guest/create 
/guest/get {one/many} = everyone & admin 
/guest/delete {one/many} 

/booking/create {one} = everyone
/booking/delete {one} = super_admin & admin
/booking/get {one/many} = guest & user & admin

/quick-booking/get {one} = user

/invoice/create {one} = [ done after booking is made ]
/invoice/get {one/many} = guest & user & admin
/invoice/delete {many} = admin

###### user_services_url ###### 

user/profile/create {one} = everyone
user/profile/delete {one/many} = user & super_admin
user/profile/update {one} = user
user/profile/get {one/many} = user & super_admin

user/info/create {one} = everyone
user/info/delete {one/many} = user & super_admin
user/info/update {one} = user
user/info/get {one/many} = user & super_admin

###### analytics_services_url ###### 

analytic/create {one/many} = services
analytic/delete {one/many} = super_admin
analytic/get {one/many} = super_admin & admin

###### audit_logging_services_url ###### 

audit/create {one/many} = services
audit/delete {one/many} = super_admin
audit/get {one/many} = super_admin & admin









