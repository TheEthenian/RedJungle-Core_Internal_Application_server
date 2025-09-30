step_object = [
    
#################### ACCESSS CONTROL SERVER #####################

######## CREATE ROLE
# get role 
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$1",
        "relative_url":"/role",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE ROLE
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$2",
        "relative_url":"/role",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE ROLE
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$3",
        "relative_url":"/role",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET ROLE
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$4",
        "relative_url":"/role",
        "request_type": 'get',
        "execution_order": 1
    },

######## CREATE POLICY
# get policy 
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$5",
        "relative_url":"/policy",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE POLICY
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$6",
        "relative_url":"/policy",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE POLICY
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$7",
        "relative_url":"/policy",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET POLICY
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$8",
        "relative_url":"/policy",
        "request_type": 'get',
        "execution_order": 1
    },


#################### ADMIN SERVER #####################

######## CREATE HOTEL
# get_hotel
# auth [admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$21",
        "relative_url":"/hotel",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE HOTEL
# auth [admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$22",
        "relative_url":"/hotel",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE HOTEL
# auth [admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$23",
        "relative_url":"/hotel",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET HOTEL
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$24",
        "relative_url":"/hotel",
        "request_type": 'get',
        "execution_order": 1
    },

######## CREATE HOTEL SERVICE
# get hotel service
# auth [admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$25",
        "relative_url":"/hotel-service",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE HOTEL SERVICE
# auth [admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$26",
        "relative_url":"/hotel-service",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE HOTEL SERVICE
# auth [admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$27",
        "relative_url":"/hotel-service",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET HOTEL SERVICE
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$28",
        "relative_url":"/hotel-service",
        "request_type": 'get',
        "execution_order": 1
    },

######## CREATE STAFF
# get staff
# auth [admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$29",
        "relative_url":"/staff",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE STAFF
# auth [admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$30",
        "relative_url":"/staff",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE STAFF
# auth [admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$31",
        "relative_url":"/staff",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET STAFF
# auth [admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$32",
        "relative_url":"/staff",
        "request_type": 'get',
        "execution_order": 2
    },

######## CREATE ADMIN
# get admin
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$33",
        "relative_url":"/admin",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE ADMIN
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$34",
        "relative_url":"/admin",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE ADMIN
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$35",
        "relative_url":"/admin",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET ADMIN
# auth [super_admin & admin]
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$36",
        "relative_url":"/admin",
        "request_type": 'get',
        "execution_order": 2
    },


#################### ANALYTICS SERVER #####################

######## CREATE ANALYTIC
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$41",
        "relative_url":"/analytic",
        "request_type": 'post',
        "execution_order": 1
    },

######## DELETE ANALYTIC
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$42",
        "relative_url":"/analytic",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET ANALYTIC
# auth [super_admin & admin]
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$43",
        "relative_url":"/analytic",
        "request_type": 'get',
        "execution_order": 2
    },



#################### AUDIT LOGGING SERVER #####################

######## CREATE AUDIT
    {
        "step_id":"",
        "service_id":"#12",
        "workflow_id":"$61",
        "relative_url":"/audit",
        "request_type": 'post',
        "execution_order": 1
    },

######## DELETE AUDIT
# auth [super_admin]
    {
        "step_id":"",
        "service_id":"#12",
        "workflow_id":"$62",
        "relative_url":"/audit",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET AUDIT
# auth [super_admin & admin]
    {
        "step_id":"",
        "service_id":"#12",
        "workflow_id":"$63",
        "relative_url":"/audit",
        "request_type": 'get',
        "execution_order": 2
    },


#################### AUTH SERVER #####################

######## CREATE AUTH
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$81",
        "relative_url":"/auth",
        "request_type": 'post',
        "execution_order": 1
    },

######## UPDATE AUTH
# auth [user]
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$82",
        "relative_url":"/auth",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE AUTH
# auth [user & super admin]
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$83",
        "relative_url":"/auth",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET AUTH
# auth [user & super admin]
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$84",
        "relative_url":"/auth",
        "request_type": 'get',
        "execution_order": 2
    },


#################### BOOKING SERVER #####################

######## CREATE GUEST
# get guest
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$101",
        "relative_url":"/guest",
        "request_type": 'post',
        "execution_order": 2
    },

######## GET GUEST
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$102",
        "relative_url":"/guest",
        "request_type": 'get',
        "execution_order": 1
    },

######## DELETE GUEST
# auth [user & admin]
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$103",
        "relative_url":"/guest",
        "request_type": 'delete',
        "execution_order": 2
    },

######## CREATE BOOKING
# get booking
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$104",
        "relative_url":"/booking",
        "request_type": 'post',
        "execution_order": 2
    },

######## GET BOOKING
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$105",
        "relative_url":"/booking",
        "request_type": 'get',
        "execution_order": 1
    },

######## DELETE BOOKING
# auth [guest]
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$106",
        "relative_url":"/booking",
        "request_type": 'delete',
        "execution_order": 2
    },

######## QUICK BOOKING
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$107",
        "relative_url":"/quick-booking",
        "request_type": 'get',
        "execution_order": 1
    },

######## CREATE INVOICE
# get invoice
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$108",
        "relative_url":"/invoice",
        "request_type": 'post',
        "execution_order": 2
    },

######## GET INVOICE
# auth [user & guest]
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$109",
        "relative_url":"/invoice",
        "request_type": 'get',
        "execution_order": 2
    },

######## DELETE INVOICE
# auth [super admin]
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$110",
        "relative_url":"/invoice",
        "request_type": 'delete',
        "execution_order": 2
    },



#################### HOTEL MANAGEMENT SERVER #####################

######## CREATE ROOM
# get room
# auth [admin]
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$121",
        "relative_url":"/room",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE ROOM
# auth [admin]
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$122",
        "relative_url":"/room",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE ROOM
# auth [admin]
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$123",
        "relative_url":"/room",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET ROOM
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$124",
        "relative_url":"/room",
        "request_type": 'get',
        "execution_order": 1
    },


#################### PAYMENT GATEWAY SERVER #####################

######## CREATE TRANSACTION
# get transaction
# auth [guest & super-admin]
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$141",
        "relative_url":"/transaction",
        "request_type": 'post',
        "execution_order": 3
    },

######## DELETE TRANSACTION
# auth [super-admin]
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$142",
        "relative_url":"/transaction",
        "request_type": 'delete',
        "execution_order": 3
    },

######## GET TRANSACTION
# auth [super-admin]
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$143",
        "relative_url":"/transaction",
        "request_type": 'get',
        "execution_order": 2
    },

######## CREATE PAYMENT METHOD
# get payment-method
# auth [user & guest & super-admin]
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$144",
        "relative_url":"/payment-method",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE PAYMENT METHOD
# auth [user & guest & super-admin]
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$145",
        "relative_url":"/payment-method",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE PAYMENT METHOD
# auth [user & guest & super-admin]
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$146",
        "relative_url":"/payment-method",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET PAYMENT METHOD
# auth[user & super_admin]
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$147",
        "relative_url":"/payment-method",
        "request_type": 'get',
        "execution_order": 1
    },


#################### REVIEW SERVER #####################

######## CREATE USER REVIEW
# get user review
# auth [user]
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$161",
        "relative_url":"/review/user",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE USER REVIEW
# auth [user]
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$162",
        "relative_url":"/review/user",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE USER REVIEW
# auth [user]
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$163",
        "relative_url":"/review/user",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET USER REVIEW
# auth [user]
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$164",
        "relative_url":"/review/user",
        "request_type": 'get',
        "execution_order": 1
    },

######## GET PUBLIC REVIEW
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$165",
        "relative_url":"/review/public",
        "request_type": 'get',
        "execution_order": 1
    },

######## DELETE PUBLIC REVIEW
# auth [super_admin & admin]
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$166",
        "relative_url":"/review/public",
        "request_type": 'delete',
        "execution_order": 2
    },


#################### SUPER ADMIN SERVER #####################

######## CREATE TENANT
# get tenant
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$181",
        "relative_url":"/tenant",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE TENANT
# auth [super-admin]
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$182",
        "relative_url":"/tenant",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE TENANT
# auth [super-admin]
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$183",
        "relative_url":"/tenant",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET TENANT
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$184",
        "relative_url":"/tenant",
        "request_type": 'get',
        "execution_order": 1
    },

######## CREATE BILLING
# get billing
# auth [guest & super-admin]
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$185",
        "relative_url":"/billing",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE BILLING
# auth [super-admin]
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$186",
        "relative_url":"/billing",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE BILLING
# auth [super-admin]
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$187",
        "relative_url":"/billing",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET BILLING
# auth [user & admin & super-admin]
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$188",
        "relative_url":"/billing",
        "request_type": 'get',
        "execution_order": 2
    },

######## CREATE SUPER ADMIN
# get super admin
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$189",
        "relative_url":"/super-admin",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE SUPER ADMIN
# auth [super-admin]
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$190",
        "relative_url":"/super-admin",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE SUPER ADMIN
# auth [super-admin]
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$191",
        "relative_url":"/super-admin",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET SUPER ADMIN
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$192",
        "relative_url":"/super-admin",
        "request_type": 'get',
        "execution_order": 1
    },


#################### USER INFO SERVER #####################

######## CREATE USER
# get user
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$201",
        "relative_url":"/user/info",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE USER
# auth [user]
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$202",
        "relative_url":"/user/info",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE USER
# auth [user & admin & super-admin]
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$203",
        "relative_url":"/user/info",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET USER
# auth [everyone & user & admin & super-admin]
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$204",
        "relative_url":"/user/info",
        "request_type": 'get',
        "execution_order": 2
    },

######## CREATE USER PROFILE
# auth [user]
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$205",
        "relative_url":"/user/profile",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE USER PROFILE
# auth [user]
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$206",
        "relative_url":"/user/profile",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE USER PROFILE
# auth [user & super-admin]
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$207",
        "relative_url":"/user/profile",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET USER PROFILE
# auth [user]
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$208",
        "relative_url":"/user/profile",
        "request_type": 'get',
        "execution_order": 2
    },




]