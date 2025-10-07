policy_data = [

####################### ACCESS CONTROL SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#4",
        "roles":['#e'],
        "uri":"/role",
        "actions":['post','put','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#4",
        "roles":['#a'],
        "uri":"/role",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#4",
        "roles":['#e']
        "uri":"/policy",
        "actions":['post','put','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#4",
        "roles":['#a']
        "uri":"/policy",
        "actions":['get']
    },

####################### HOTEL SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#a']
        "uri":"/hotel",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#c']
        "uri":"/hotel",
        "actions":['put']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#e']
        "uri":"/hotel",
        "actions":['post','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#a']
        "uri":"/hotel-service",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#c']
        "uri":"/hotel-service",
        "actions":['put']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#e']
        "uri":"/hotel-service",
        "actions":['post','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#c','#e']
        "uri":"/config",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#e']
        "uri":"/config",
        "actions":['post','put','delete']
    },

####################### ANALYTIC SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#11",
        "roles":['#c','#e']
        "uri":"/analytic/event-log",
        "actions":['get','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#11",
        "roles":['#a']
        "uri":"/analytic/event-log",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#11",
        "roles":["#c",'#e']
        "uri":"/analytic/metric",
        "actions":['get','put','delete']
    },

####################### AUDIT LOGGING SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#12",
        "roles":['#a']
        "uri":"/audit",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#12",
        "roles":['#c','#e']
        "uri":"/audit",
        "actions":['get','delete']
    },

####################### AUTH SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#a']
        "uri":"/auth/credential",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b']
        "uri":"/auth/credential",
        "actions":['put']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b','#e']
        "uri":"/auth/credential",
        "actions":['get','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#a']
        "uri":"/auth/session",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b','#e']
        "uri":"/auth/session",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b','#e']
        "uri":"/auth/reset-token",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b']
        "uri":"/auth/reset-token",
        "actions":['delete']
    },

####################### BOOKING SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#b','#c','#e']
        "uri":"/guest",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#b']
        "uri":"/guest",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d','#c']
        "uri":"/guest",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d']
        "uri":"/booking",
        "actions":['post','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d','#c','#e']
        "uri":"/booking",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d']
        "uri":"/invoice",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d','#c','#e']
        "uri":"/invoice",
        "actions":['get','delete']
    },

####################### ROOM SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#e','#a','#c']
        "uri":"/room",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#e','#c']
        "uri":"/room",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#c']
        "uri":"/room",
        "actions":['post','put']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#e','#a','#c']
        "uri":"/amenity",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#e','#c']
        "uri":"/amenity",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#c']
        "uri":"/amenity",
        "actions":['post','put']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#a']
        "uri":"/amenity/picture",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#c']
        "uri":"/amenity/picture",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#c','#e']
        "uri":"/amenity/picture",
        "actions":['delete']
    },

####################### ORCHESTRATION SERVER ##########################

####################### PAYMENT GATEWAY SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#b','#e']
        "uri":"/transaction",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#b']
        "uri":"/transaction",
        "actions":['post','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#b','#e']
        "uri":"/bank",
        "actions":['get','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#e']
        "uri":"/bank",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#b']
        "uri":"/bank",
        "actions":['put']
    },

####################### REVIEW SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#2",
        "roles":['#a']
        "uri":"/review",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#2",
        "roles":['#d']
        "uri":"/review",
        "actions":['post','put']
    },

    {
        "policy_id":"$",
        "service_id":"#2",
        "roles":['#c','#d','#e']
        "uri":"/review",
        "actions":['delete']
    },

####################### TENANT SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#5",
        "roles":['#e','#f']
        "uri":"/tenant",
        "actions":['get','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#5",
        "roles":['#e']
        "uri":"/tenant",
        "actions":['post','put']
    },

    {
        "policy_id":"$",
        "service_id":"#5",
        "roles":['#e','#f']
        "uri":"/billing",
        "actions":['get','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#5",
        "roles":['#e']
        "uri":"/billing",
        "actions":['post']
    },

####################### USER SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#10",
        "roles":['#b','#e','#f']
        "uri":"/user",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#10",
        "roles":['#b']
        "uri":"/user",
        "actions":['post','put','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#10",
        "roles":['#b','#e','#f']
        "uri":"/user/profile",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#10",
        "roles":['#b']
        "uri":"/user/profile",
        "actions":['post','put','delete']
    }






]