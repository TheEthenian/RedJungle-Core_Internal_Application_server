step_object = [
    
#################### ACCESSS CONTROL SERVER #####################

######## CREATE ROLE
# get role 
# auth 
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$1",
        "relative_url":"/role",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE ROLE
# auth 
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$2",
        "relative_url":"/role",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE ROLE
# auth 
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$3",
        "relative_url":"/role",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET ROLE
# auth 
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
# auth 
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$5",
        "relative_url":"/policy",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE POLICY
# auth 
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$6",
        "relative_url":"/policy",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE POLICY
# auth 
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$7",
        "relative_url":"/policy",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET POLICY
# auth 
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$8",
        "relative_url":"/policy",
        "request_type": 'get',
        "execution_order": 1
    },


#################### HOTEL SERVER #####################

######## CREATE HOTEL
# get_hotel
# auth 
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$21",
        "relative_url":"/hotel",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE HOTEL
# auth 
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$22",
        "relative_url":"/hotel",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE HOTEL
# auth 
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$23",
        "relative_url":"/hotel",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET HOTEL
# auth 
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
# auth 
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$25",
        "relative_url":"/hotel-service",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE HOTEL SERVICE
# auth 
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$26",
        "relative_url":"/hotel-service",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE HOTEL SERVICE
# auth 
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$27",
        "relative_url":"/hotel-service",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET HOTEL SERVICE
# auth 
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$28",
        "relative_url":"/hotel-service",
        "request_type": 'get',
        "execution_order": 1
    },

######## CREATE CONFIG
# get configs
# auth
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$29",
        "relative_url":"/config",
        "request_type": 'post',
        "execution_order": 1
    },

######## UPDATE CONFIG
# auth
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$30",
        "relative_url":"/config",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE CONFIG
# auth
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$31",
        "relative_url":"/config",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET CONFIG
# auth
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$32",
        "relative_url":"/config",
        "request_type": 'get',
        "execution_order": 1
    },



#################### ANALYTICS SERVER #####################

######## CREATE ANALYTIC
# auth 
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$41",
        "relative_url":"/analytic",
        "request_type": 'post',
        "execution_order": 1
    },

######## DELETE ANALYTIC
# auth 
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$42",
        "relative_url":"/analytic",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET ANALYTIC
# auth 
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
# auth 
    {
        "step_id":"",
        "service_id":"#12",
        "workflow_id":"$61",
        "relative_url":"/audit",
        "request_type": 'post',
        "execution_order": 1
    },

######## DELETE AUDIT
# auth 
    {
        "step_id":"",
        "service_id":"#12",
        "workflow_id":"$62",
        "relative_url":"/audit",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET AUDIT
# auth 
    {
        "step_id":"",
        "service_id":"#12",
        "workflow_id":"$63",
        "relative_url":"/audit",
        "request_type": 'get',
        "execution_order": 2
    },


#################### AUTH SERVER #####################

######## CREATE CREDENTIAL
# get credential
# auth 
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$81",
        "relative_url":"/auth/credential",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE CREDENTIAL
# auth 
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$82",
        "relative_url":"/auth/credential",
        "request_type": 'put',
        "execution_order": 2
    },


######## DELETE CREDENTIAL
# auth 
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$83",
        "relative_url":"/auth/credential",
        "request_type": 'delete',
        "execution_order": 2
    },


######## GET CREDENTIAL
# auth 
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$84",
        "relative_url":"/auth/credential",
        "request_type": 'get',
        "execution_order": 2
    },


######## CREATE SESSION
# get session
# auth 
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$85",
        "relative_url":"/auth/session",
        "request_type": 'post',
        "execution_order": 1
    },


######## GET SESSION
# auth 
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$86",
        "relative_url":"/auth/session",
        "request_type": 'get',
        "execution_order": 2
    },


######## DELETE SESSION
# auth 
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$87",
        "relative_url":"/auth/credential",
        "request_type": 'delete',
        "execution_order": 2
    },


######## CREATE RESET-TOKEN
# get reset-token
# auth 
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$88",
        "relative_url":"/auth/reset-token",
        "request_type": 'post',
        "execution_order": 2
    },

######## DELETE RESET-TOKEN
# auth 
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$89",
        "relative_url":"/auth/reset-token",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET RESET-TOKEN
# auth 
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$90",
        "relative_url":"/auth/reset-token",
        "request_type": 'get',
        "execution_order": 2
    },



#################### BOOKING SERVER #####################

######## CREATE GUEST
# guest
# auth 
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$101",
        "relative_url":"/guest",
        "request_type": 'post',
        "execution_order": 3
    },

######## GET GUEST
# auth 
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$102",
        "relative_url":"/guest",
        "request_type": 'get',
        "execution_order": 1
    },

######## DELETE GUEST
# auth 
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$103",
        "relative_url":"/guest",
        "request_type": 'delete',
        "execution_order": 2
    },

######## CREATE BOOKING
# create guest
# get booking
# auth 
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$104",
        "relative_url":"/booking",
        "request_type": 'post',
        "execution_order": 3
    },

######## GET BOOKING
# auth 
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$105",
        "relative_url":"/booking",
        "request_type": 'get',
        "execution_order": 1
    },

######## DELETE BOOKING
# auth 
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$106",
        "relative_url":"/booking",
        "request_type": 'delete',
        "execution_order": 2
    },

######## CREATE INVOICE
# get invoice
# auth 
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$107",
        "relative_url":"/invoice",
        "request_type": 'post',
        "execution_order": 3
    },

######## GET INVOICE
# auth 
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$108",
        "relative_url":"/invoice",
        "request_type": 'get',
        "execution_order": 2
    },

######## DELETE INVOICE
# auth 
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$109",
        "relative_url":"/invoice",
        "request_type": 'delete',
        "execution_order": 2
    },



#################### ROOM SERVER #####################

######## CREATE ROOM
# get room
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$121",
        "relative_url":"/room",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE ROOM
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$122",
        "relative_url":"/room",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE ROOM
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$123",
        "relative_url":"/room",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET ROOM
# get amenity
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$124",
        "relative_url":"/room",
        "request_type": 'get',
        "execution_order": 2
    },

######## CREATE AMENITY
# get amenity
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$125",
        "relative_url":"/amenity",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE AMENITY
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$126",
        "relative_url":"/amenity",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE AMENITY
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$127",
        "relative_url":"/amenity",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET AMENITY
# get amenity picture
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$128",
        "relative_url":"/amenity",
        "request_type": 'get',
        "execution_order": 2
    },

######## CREATE AMENITY PICTURE
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$129",
        "relative_url":"/amenity/picture",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE AMENITY PICTURE
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$130",
        "relative_url":"/amenity/picture",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE AMENITY PICTURE
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$131",
        "relative_url":"/amenity/picture",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET AMENITY PICTURE
# auth 
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$132",
        "relative_url":"/amenity/picture",
        "request_type": 'get',
        "execution_order": 2
    },


#################### PAYMENT GATEWAY SERVER #####################

######## CREATE TRANSACTION
# get transaction
# auth 
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$141",
        "relative_url":"/transaction",
        "request_type": 'post',
        "execution_order": 3
    },

######## DELETE TRANSACTION
# auth 
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$142",
        "relative_url":"/transaction",
        "request_type": 'delete',
        "execution_order": 3
    },

######## GET TRANSACTION
# auth 
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$143",
        "relative_url":"/transaction",
        "request_type": 'get',
        "execution_order": 2
    },

######## CREATE BANK
# auth 
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$144",
        "relative_url":"/bank",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE BANK
# auth 
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$145",
        "relative_url":"/bank",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE BANK
# auth 
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$146",
        "relative_url":"/bank",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET BANK
# auth 
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$147",
        "relative_url":"/bank",
        "request_type": 'get',
        "execution_order": 1
    },


#################### REVIEW SERVER #####################

######## CREATE REVIEW
# get review
# auth 
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$161",
        "relative_url":"/review",
        "request_type": 'post',
        "execution_order": 3
    },

######## UPDATE REVIEW
# auth 
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$162",
        "relative_url":"/review",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE REVIEW
# auth 
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$163",
        "relative_url":"/review",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET REVIEW
# auth 
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$164",
        "relative_url":"/review",
        "request_type": 'get',
        "execution_order": 1
    },



#################### TENANT SERVER #####################

######## CREATE TENANT
# get tenant
# auth 
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$181",
        "relative_url":"/tenant",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE TENANT
# auth 
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$182",
        "relative_url":"/tenant",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE TENANT
# auth 
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$183",
        "relative_url":"/tenant",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET TENANT
# auth 
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
# auth 
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$185",
        "relative_url":"/billing",
        "request_type": 'post',
        "execution_order": 3
    },

######## DELETE BILLING
# auth 
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$186",
        "relative_url":"/billing",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET BILLING
# auth 
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$187",
        "relative_url":"/billing",
        "request_type": 'get',
        "execution_order": 2
    },


#################### USER SERVER #####################

######## CREATE USER
# get user
# auth 
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$201",
        "relative_url":"/user",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE USER
# auth 
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$202",
        "relative_url":"/user",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE USER
# auth 
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$203",
        "relative_url":"/user",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET USER
# auth 
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$204",
        "relative_url":"/user",
        "request_type": 'get',
        "execution_order": 2
    },

######## CREATE USER PROFILE
# get user profile
# auth 
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$205",
        "relative_url":"/user/profile",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE USER PROFILE
# auth 
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$206",
        "relative_url":"/user/profile",
        "request_type": 'put',
        "execution_order": 2
    },

######## DELETE USER PROFILE
# auth 
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$207",
        "relative_url":"/user/profile",
        "request_type": 'delete',
        "execution_order": 2
    },

######## GET USER PROFILE
# auth 
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$208",
        "relative_url":"/user/profile",
        "request_type": 'get',
        "execution_order": 2
    },




]