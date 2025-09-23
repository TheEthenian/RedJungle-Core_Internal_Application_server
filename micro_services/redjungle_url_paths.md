###### orchestrator_services_url ###### 

- depending on the http request it will be on eith main 
post, delete , update then routed to the destination

###### review_services_url ###### 

/create {one} = user
/delete {one/many} = super_admin & admin & user
/update {one} = user
/get {many/one} = everyone

###### auth_services_url ###### 

/get {one/many} = user & super_admin
/create {one} = user
/update {one} = user
/delete {one/many} = user & super_admin

###### access_control_services_url ###### 

/role/create {one/many} = super_admin
/role/update {one/many} = super_admin
/role/delete {one/many} = super_admin
/role/get {one/many} =  super_admin [ or just acs stuff ]

/policy/create {one/many} = super_admin
/policy/update {one/many} = super_admin
/policy/delete {one/many} = super_admin
/policy/get {one/many} =  super_admin [ or just acs stuff ]

/check_authorization {one} = user

- Each path has its own data structure ideosyncrasies
- Each workflow has a jwt payload that shows roles and confirms
identity or the entity 
- Will continue this after everything is operational

###### super_admin_services_url ###### 

/tenant/update {one} = super_admin
/tenant/delete {one/many}= platform
/tenant/create {one}
/tenant/get {one}
/tenant/billing/get {one/many} = super_admin 
/tenant/billing/delete {one/many} = super_admin 

/super-admin/update = super_admin
/super-admin/get = super_admin
/super-admin/delete = super_admin
/super-admin/create = user

###### admin_services_url ###### 

/hotel/update {one/many} = admin & super_admin
/hotel/delete {one/many} = admin & super_admin
/hotel/get {one/many} = everyone & super_admin
/hotel/create {one} = admin

/hotel-service/get {one/many} = everyone 
/hotel-service/create {one/many} = admin & super_admin
/hotel-service/update {one/many} = admin & super_admin
/hotel-service/delete {one/many} = admin & super_admin

/staff/create {one/many} = admin & super_admin
/staff/get {one/many}
/staff/delete {one/many} = admin & super_admin

/admin/create {one/many} = super_admin
/admin/update {one/many} = admin
/admin/get {one/many} = admin & super_admin
/admin/delete {one/many} = super_admin

###### hotel_management_services_url ###### 

/room/create {one/many} => admin
/room/delete {one/many} => admin
/room/update {one/many} => admin
/room/get {one/many} => admin

/room/available {one/many} => everyone
/room/booked {one/many} => everyone
/room/offline {one/many} => admin & super_admin

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
/booking/quick {one} = user

/invoice/create {one} = [ done after booking is made ]
/invoice/get {one/many} = guest & user & admin
/invoice/delete {many} = admin

###### user_info_services_url ###### 

/create {one} = everyone
/delete {one/many} = user & super_admin
/update {one} = user
/get {one/many} = user & super_admin

###### analytics_services_url ###### 

/create {one/many} = services
/delete {one/many} = super_admin
/get {one/many} = super_admin & admin

###### audit_logging_services_url ###### 

/create {one/many} = services
/delete {one/many} = super_admin
/get {one/many} = super_admin & admin









