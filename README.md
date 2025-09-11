
############### Micro-services addresses ##########################

V0 => orchestrator_services_url = 'http://redjungle-00.lab:7001'
V1 => auth_services_url = 'http://redjungle-00.lab:7010'
V2 => access_control_services_url = 'http://redjungle-00.lab:7020'
V3 => super_admin_services_url = 'http://redjungle-00.lab:7030'
V4 => admin_services_url = 'http://redjungle-00.lab:7040'
V5 => hotel_management_services_url = 'http://redjungle-00.lab:7050'
V6 => payment_gateway_services_url = 'http://redjungle-00.lab:7060'
V7 => booking_services_url = 'http://redjungle-00.lab:7070'
V8 => user_info_services_url = 'http://redjungle-00.lab:7080'
V9 => analytics_services_url = 'http://redjungle-00.lab:7090'

###################################################################


################## Functions of each Micro service ################

Orchestration_server:
- The black shirt manager of inter server communication

Auth server:
- Issueing & validating tokens { JWTs & OAuth tokens }
- Credential management
- Rate limiting & Session ids

Admin server:
- hotel management
- user management
- system wide configs
- reporting

Booking server:
- CRUD of reservations

Payment Gatway server:
- Transaction processing

Hotel management server:
- Hotel level data { Accomodation options available & pricing }

Analytics server:
- Various data aggregation by authorization

Access control server:
- Which auth tokens can do what 

Super admin server:
- Multi hotel config
- Global policy changes
- Operations that affect hotels under the chain umbrella

User info data
- User data
- Personal info
- Roles & permitions





















