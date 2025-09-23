workflow_object = [

############## CREATE USERS ###################
    {
        "workflow_name":"create_user",
        "workflow_id":"$1",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"create_guest",
        "workflow_id":"$2",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"create_tenant",
        "workflow_id":"$3",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"create_superuser",
        "workflow_id":"$4",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"create_admin",
        "workflow_id":"$5",
        "sub_workflows": [],
        "steps":[]
    },

############## AUTHORIZATION ###################

    {
        "workflow_name":"authorize_user",
        "workflow_id":"$6",
        "sub_workflows": [],
        "steps":[]
    },

############## LOGIN ###################

    {
        "workflow_name":"login_user",
        "workflow_id":"$7",
        "sub_workflows": [],
        "steps":[]
    },

############## UPDATE USERS ###################

    {
        "workflow_name":"update_user",
        "workflow_id":"$8",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"update_tenant",
        "workflow_id":"$9",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"update_admin",
        "workflow_id":"$10",
        "sub_workflows": [],
        "steps":[]
    },

############## DELETE USERS ###################

    {
        "workflow_name":"delete_user",
        "workflow_id":"$11",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"delete_tenant",
        "workflow_id":"$12",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"delete_super_admin",
        "workflow_id":"$13",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"delete_admin",
        "workflow_id":"$14",
        "sub_workflows": [],
        "steps":[]
    },

############## GET PPRIVILAGED ###################

    {
        "workflow_name":"get_guest",
        "workflow_id":"$15",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_user",
        "workflow_id":"$16",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_admin",
        "workflow_id":"$17",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_hotel",
        "workflow_id":"$18",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_super_admin",
        "workflow_id":"$19",
        "sub_workflows": [],
        "steps":[]
    },

############## GET HOTEL DATA ###################

    {
        "workflow_name":"get_available_room",
        "workflow_id":"$20",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_booked_rooms",
        "workflow_id":"$21",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_offline_rooms",
        "workflow_id":"$22",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_individual_room",
        "workflow_id":"$23",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_hotel_services",
        "workflow_id":"$24",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"create_hotel_service",
        "workflow_id":"$25",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"update_hotel_service",
        "workflow_id":"$26",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"delete_hotel_service",
        "workflow_id":"$27",
        "sub_workflows": [],
        "steps":[]
    },

############## CUSTOMER BOOKING ###################

    {
        "workflow_name":"get_booking",
        "workflow_id":"$28",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"create_booking",
        "workflow_id":"$29",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"delete_booking",
        "workflow_id":"$30",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"quick_booking",
        "workflow_id":"$31",
        "sub_workflows": [],
        "steps":[]
    },

############## MANAGE HOTEL DATA ###################

    {
        "workflow_name":"create_hotel",
        "workflow_id":"$32",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"create_room",
        "workflow_id":"$33",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"update_hotel",
        "workflow_id":"$34",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"update_room",
        "workflow_id":"$35",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"delete_hotel",
        "workflow_id":"$36",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"delete_room",
        "workflow_id":"$37",
        "sub_workflows": [],
        "steps":[]
    },

################### BILLING #####################

    {
        "workflow_name":"create_payment_method",
        "workflow_id":"$38",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"update_payment_method",
        "workflow_id":"$39",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"delete_payment_method",
        "workflow_id":"$40",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"create_transaction_user",
        "workflow_id":"$41",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"delete_billing",
        "workflow_id":"$42",
        "sub_workflows": [],
        "steps":[]
    },

################### MANAGE REVIEW #####################

    {
        "workflow_name":"create_reviews",
        "workflow_id":"$43",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"update_reviews",
        "workflow_id":"$44",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"delete_reviews",
        "workflow_id":"$45",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_user_review",
        "workflow_id":"$46",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_public_reviews",
        "workflow_id":"$47",
        "sub_workflows": [],
        "steps":[]
    },


################# ADDITIONS ##################


    {
        "workflow_name":"get_tenant",
        "workflow_id":"$48",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_room",
        "workflow_id":"$49",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_payment_method",
        "workflow_id":"$50",
        "sub_workflows": [],
        "steps":[]
    },
    {
        "workflow_name":"get_transaction",
        "workflow_id":"$51",
        "sub_workflows": [],
        "steps":[]
    },






]





