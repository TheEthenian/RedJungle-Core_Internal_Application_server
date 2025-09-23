[Every request => access control server]
[Every request => orchestration server]
[Every request => redjungle/tenant_name/page]


admin_panel_ui => redjungle/tenant_name
super_admin_pannel_ui => redjungle/tenant_name


Create_user:
=> auth/admin/create/post >
=> auth/super_admin/create/post >
=> auth/new_guest/create/post >
=> auth/normal_guest/create/post >

Login:
=> auth/admin/login/post >
=> auth/super_admin/login/post >
=> auth/new_guest/login/post >
=> auth/normal_guest/login/post >

Billings:
=> payment_gateway/super_admin/post >
=> payment_gateway/new_guest/post > { guest }
=> payment_gateway/normal_guest/post > { user }

Reservations:
=> booking/new_guest/get > { guest }
=> booking/normal_guest/valid/get > { guest }
=> booking/normal_guest/expired/get > { guest }

=> booking/new_guest/delete > { guest }
=> booking/normal_guest/valid/delete > { guest }

Booking:
=> booking/new_guest/post > { guest }
=> booking/normal_guest/post > { user }

Home:
=> hotel_managent/rooms/get > { everyone }
=> hotel_managent/rooms/condition/get > { admin }
=> hotel_managent/rooms/create > { admin }
=> hotel_managent/rooms/update > { admin }
=> hotel_managent/rooms/delete > { admin }

Guest_comments:
=> hotel_review/post > { guests }
=> hotel_review/update > { guest }
=> hotel_review/delete > { guest }

Reviews:
=> hotel_review/get > { everyone }


