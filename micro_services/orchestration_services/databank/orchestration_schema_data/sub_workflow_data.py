sub_workflow_object = [
    
############### CREATE USER ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$1',
        "assistance_workflow_id":'$16',
        "execution_order": 1
    },

############### CREATE GUEST ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$2',
        "assistance_workflow_id":'$15',
        "execution_order": 1
    },

############### CREATE TENANT ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$3',
        "assistance_workflow_id":'$48',
        "execution_order": 1
    },

############### CREATE SUPER ADMIN ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$4',
        "assistance_workflow_id":'$19',
        "execution_order": 1
    },

############### CREATE ADMIN ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$5',
        "assistance_workflow_id":'$17',
        "execution_order": 1
    },

############### UPDATE USER ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$8',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### UPDATE TENANT ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$9',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### UPDATE ADMIN ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$10',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### DELETE USER ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$11',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### DELETE TENANT ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$12',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### DELETE SUPER ADMIN ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$13',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### DELETE ADMIN ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$14',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### GET GUESTS ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$15',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### GET USER ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$16',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### GET ADMIN ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$17',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### GET HOTEL ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$18',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### GET SUPER ADMINS ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$19',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### GET BOOKED ROOMS ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$21',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### GET OFFLINE ROOMS ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$22',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### CREATE HOTEL SERVICES ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$25',
        "assistance_workflow_id":'$24',
        "execution_order": 1
    },
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$25',
        "assistance_workflow_id":'$6',
        "execution_order": 2
    },

############### UPDATE HOTEL SERVICES ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$26',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### DELETE HOTEL SERVICES ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$27',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### GET BOOKING ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$28',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### CREATE BOOKING ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$29',
        "assistance_workflow_id":'$2',
        "execution_order": 1
    },
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$29',
        "assistance_workflow_id":'$28',
        "execution_order": 2
    },
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$29',
        "assistance_workflow_id":'$6',
        "execution_order": 3
    },

############### DELETE BOOKING ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$30',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### QUICK BOOKING ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$31',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### CREATE HOTEL ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$32',
        "assistance_workflow_id":'$18',
        "execution_order": 1
    },
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$32',
        "assistance_workflow_id":'$6',
        "execution_order": 2
    },

############### CREATE ROOM ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$33',
        "assistance_workflow_id":'$49',
        "execution_order": 1
    },
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$33',
        "assistance_workflow_id":'$6',
        "execution_order": 2
    },

############### UPDATE HOTEL ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$34',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### UPDATE ROOM ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$35',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### DELETE HOTEL ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$36',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### DELETE ROOM ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$37',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############# CREATE PAYMENT-METHOD #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$38',
        "assistance_workflow_id":'$50',
        "execution_order": 1
    },
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$38',
        "assistance_workflow_id":'$6',
        "execution_order": 2
    },

############# UPDATE PAYMENT-METHOD #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$39',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############# DELETE PAYMENT-METHOD #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$40',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############# CREATE TRANSACTION #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$41',
        "assistance_workflow_id":'$51',
        "execution_order": 1
    },
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$41',
        "assistance_workflow_id":'$38',
        "execution_order": 2
    },
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$41',
        "assistance_workflow_id":'$6',
        "execution_order": 3
    },

############# DELETE TRANSACTION #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$42',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############# CREATE USER REVIEW  #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$43',
        "assistance_workflow_id":'$46',
        "execution_order": 1
    },
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$43',
        "assistance_workflow_id":'$6',
        "execution_order": 2
    },

############# UPDATE USER REVIEW  #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$44',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############# DELETE USER REVIEW  #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$45',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############# GET USER REVIEW  #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$46',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############### GET ROOM ################
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$49',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############# GET PAYMENT-METHOD #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$50',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },

############# GET TRANSACTION #############
    {
        "sub_workflow_id":'#1',
        "master_workflow_id":'$51',
        "assistance_workflow_id":'$6',
        "execution_order": 1
    },




]








