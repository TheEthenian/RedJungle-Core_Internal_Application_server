step_object = [
    
############### CREATE USER ################
    # get user ...
    {
        "step_id":"#a",
        "service_id":"#10",
        "workflow_id":"$1",
        "relative_url":"/create",
        "execution_order": 2
    },

############### CREATE GUEST ################
    # get guest ...
    {
        "step_id":"#c",
        "service_id":"#9",
        "workflow_id":"$2",
        "relative_url":"/guest/create",
        "execution_order": 2
    },

############### CREATE TENANT ################
    # get tenant ...
    {
        "step_id":"#f",
        "service_id":"#5",
        "workflow_id":"$3",
        "relative_url":"/tenant/create",
        "execution_order": 2
    },

############### CREATE SUPER ADMIN ################
    #get super admin ...
    {
        "step_id":"#h",
        "service_id":"#5",
        "workflow_id":"$4",
        "relative_url":"/super-admin/create",
        "execution_order": 2
    },

############### CREATE ADMIN ################
    #get admin ...
    {
        "step_id":"#k",
        "service_id":"#6",
        "workflow_id":"$5",
        "relative_url":"admin/create",
        "execution_order": 2
    },

############### AUTHORISE USER ################

    {
        "step_id":"#a",
        "service_id":"#4",
        "workflow_id":"$6",
        "relative_url":"/check_authorization",
        "execution_order": 1
    },

############### LOGIN USER ################

    {
        "step_id":"#a",
        "service_id":"#3",
        "workflow_id":"$7",
        "relative_url":"/get",
        "execution_order": 1
    },

############### UPDATE USER ################
    ## Authorize
    {
        "step_id":"#m",
        "service_id":"#10",
        "workflow_id":"$8",
        "relative_url":"/update",
        "execution_order": 2
    },

############### UPDATE TENANT ################
    ## Authorize
    {
        "step_id":"#p",
        "service_id":"#5",
        "workflow_id":"$9",
        "relative_url":"/tenant/update",
        "execution_order": 2
    },

############### UPDATE ADMIN ################
    ## Authorize
    {
        "step_id":"#r",
        "service_id":"#6",
        "workflow_id":"$10",
        "relative_url":"/admin/update",
        "execution_order": 2
    },

############### DELETE USER ################
    ## Authorize
    {
        "step_id":"#t",
        "service_id":"#3",
        "workflow_id":"$11",
        "relative_url":"/authenticate",
        "execution_order": 2
    },

############### DELETE TENANT ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#5",
        "workflow_id":"$12",
        "relative_url":"/tenant/delete",
        "execution_order": 2
    },

############### DELETE SUPER ADMIN ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#5",
        "workflow_id":"$13",
        "relative_url":"/super-admin/delete",
        "execution_order": 2
    },

############### DELETE ADMIN ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#6",
        "workflow_id":"$14",
        "relative_url":"/admin/delete",
        "execution_order": 2
    },

############### GET GUESTS ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#9",
        "workflow_id":"$15",
        "relative_url":"/guest/get",
        "execution_order": 2
    },

############### GET USER ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#10",
        "workflow_id":"$16",
        "relative_url":"/get",
        "execution_order": 2
    },

############### GET ADMIN ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#6",
        "workflow_id":"$17",
        "relative_url":"/admin/get",
        "execution_order": 2
    },

############### GET HOTEL ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#6",
        "workflow_id":"$18",
        "relative_url":"/hotel/get",
        "execution_order": 2
    },

############### GET SUPER ADMINS ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#5",
        "workflow_id":"$19",
        "relative_url":"/super-admin/get",
        "execution_order": 2
    },

############### GET AVAILABLE ROOM ################
    {
        "step_id":"#w",
        "service_id":"#7",
        "workflow_id":"$20",
        "relative_url":"/room/available",
        "execution_order": 1
    },

############### GET BOOKED ROOMS ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#7",
        "workflow_id":"$21",
        "relative_url":"/room/booked",
        "execution_order": 2
    },

############### GET OFFLINE ROOMS ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#7",
        "workflow_id":"$22",
        "relative_url":"/room/offline",
        "execution_order": 2
    },

############### GET INDIVIDUAL ROOM ################
    {
        "step_id":"#w",
        "service_id":"#7",
        "workflow_id":"$23",
        "relative_url":"/room/available",
        "execution_order": 1
    },

############### GET HOTEL SERVICES ################
    {
        "step_id":"#w",
        "service_id":"#6",
        "workflow_id":"$24",
        "relative_url":"/hotel-service/get",
        "execution_order": 1
    },

############### CREATE HOTEL SERVICES ################
    # get services ...
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#6",
        "workflow_id":"$25",
        "relative_url":"/hotel-service/create",
        "execution_order": 3
    },

############### UPDATE HOTEL SERVICES ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#6",
        "workflow_id":"$26",
        "relative_url":"/hotel-service/update",
        "execution_order": 2
    },

############### DELETE HOTEL SERVICES ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#6",
        "workflow_id":"$27",
        "relative_url":"/hotel-service/delete",
        "execution_order": 2
    },

############### GET BOOKING ################
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#9",
        "workflow_id":"$28",
        "relative_url":"/booking/get",
        "execution_order": 2
    },

############### CREATE BOOKING ################
    ## create guest ...
    # get booking ...
    ## Authorize
    {
        "step_id":"#w",
        "service_id":"#9",
        "workflow_id":"$29",
        "relative_url":"/booking/create",
        "execution_order": 4
    },

############### DELETE BOOKING ################
    ## authorize
    {
        "step_id":"#w",
        "service_id":"#9",
        "workflow_id":"$30",
        "relative_url":"/booking/delete",
        "execution_order": 2
    },

############### QUICK BOOKING ################
    ## authorize
    {
        "step_id":"#w",
        "service_id":"#9",
        "workflow_id":"$31",
        "relative_url":"/booking/quick",
        "execution_order": 2
    },

############### CREATE HOTEL ################
    # get hotel ...
    ## authorize
    {
        "step_id":"#w",
        "service_id":"#6",
        "workflow_id":"$32",
        "relative_url":"/hotel/create",
        "execution_order": 3
    },

############### CREATE ROOM ################
    # get room ...
    ## authorize
    {
        "step_id":"#w",
        "service_id":"#7",
        "workflow_id":"$33",
        "relative_url":"/room/create",
        "execution_order": 3
    },

############### UPDATE HOTEL ################
    ## authorize
    {
        "step_id":"#w",
        "service_id":"#6",
        "workflow_id":"$34",
        "relative_url":"/hotel/update",
        "execution_order": 2
    },

############### UPDATE ROOM ################
    ## authorize
    {
        "step_id":"#w",
        "service_id":"#7",
        "workflow_id":"$35",
        "relative_url":"/room/update",
        "execution_order": 2
    },

############### DELETE HOTEL ################
    ## authorize
    {
        "step_id":"#w",
        "service_id":"#6",
        "workflow_id":"$36",
        "relative_url":"/hotel/delete",
        "execution_order": 2
    },

############### DELETE ROOM ################
    ## authorize
    {
        "step_id":"#w",
        "service_id":"#7",
        "workflow_id":"$37",
        "relative_url":"/room/delete",
        "execution_order": 2
    },

############# CREATE PAYMENT-METHOD #############
    # get payment_method ...
    #authorize
    {
        "step_id":"#w",
        "service_id":"#8",
        "workflow_id":"$38",
        "relative_url":"/payment-method/create",
        "execution_order": 3
    },

############# UPDATE PAYMENT-METHOD #############
    #authorize
    {
        "step_id":"#w",
        "service_id":"#8",
        "workflow_id":"$39",
        "relative_url":"/payment-method/update",
        "execution_order": 2
    },

############# DELETE PAYMENT-METHOD #############
    #authorize
    {
        "step_id":"#w",
        "service_id":"#8",
        "workflow_id":"$40",
        "relative_url":"/payment-method/delete",
        "execution_order": 2
    },

############# CREATE TRANSACTION #############
    # get transaction ...
    #create_payment_method ...
    # authorize
    {
        "step_id":"#w",
        "service_id":"#8",
        "workflow_id":"$41",
        "relative_url":"/transaction/create",
        "execution_order": 4
    },


############# DELETE TRANSACTION #############
    #authorize
    {
        "step_id":"#w",
        "service_id":"#8",
        "workflow_id":"$42",
        "relative_url":"/transaction/delete",
        "execution_order": 2
    },

############# CREATE USER REVIEW  #############
    # get user review ...
    #authorize
    {
        "step_id":"#w",
        "service_id":"#2",
        "workflow_id":"$43",
        "relative_url":"/create",
        "execution_order": 3
    },

############# UPDATE USER REVIEW  #############
    #authorize
    {
        "step_id":"#w",
        "service_id":"#2",
        "workflow_id":"$44",
        "relative_url":"/update",
        "execution_order": 2
    },

############# DELETE USER REVIEW  #############
    #authorize
    {
        "step_id":"#w",
        "service_id":"#2",
        "workflow_id":"$45",
        "relative_url":"/delete",
        "execution_order": 2
    },

############# GET USER REVIEW  #############
    #authorize
    {
        "step_id":"#w",
        "service_id":"#2",
        "workflow_id":"$46",
        "relative_url":"/get",
        "execution_order": 2
    },

############# GET PUBLIC REVIEWS  #############
    {
        "step_id":"#w",
        "service_id":"#2",
        "workflow_id":"$47",
        "relative_url":"/get",
        "execution_order": 1
    },

############### GET TENANT ################
    {
        "step_id":"#f",
        "service_id":"#5",
        "workflow_id":"$48",
        "relative_url":"/tenant/get",
        "execution_order": 1
    },

############### GET ROOM ################
    ## authorize ...
    {
        "step_id":"#w",
        "service_id":"#7",
        "workflow_id":"$49",
        "relative_url":"/room/get",
        "execution_order": 2
    },

############# GET PAYMENT-METHOD #############
    #authorize
    {
        "step_id":"#w",
        "service_id":"#8",
        "workflow_id":"$50",
        "relative_url":"/payment-method/get",
        "execution_order": 2
    },

############# GET TRANSACTION #############
    #authorize
    {
        "step_id":"#w",
        "service_id":"#8",
        "workflow_id":"$51",
        "relative_url":"/transaction/get",
        "execution_order": 2
    },







]



















