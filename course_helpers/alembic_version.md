classDiagram
direction BT
class alembic_version {
   varchar(32) version_num
}
class bookings {
   integer user_id
   integer room_id
   date date_from
   date date_to
   integer price
   integer id
}
class facilities {
   varchar(100) title
   integer id
}
class hotels {
   varchar(100) title
   varchar location
   integer id
}
class rooms {
   integer hotel_id
   varchar title
   varchar description
   integer price
   integer quantity
   integer id
}
class rooms_facilities {
   integer room_id
   integer facility_id
   integer id
}
class users {
   varchar(200) email
   varchar(200) hashed_password
   integer id
}

bookings  -->  rooms : room_id:id
bookings  -->  users : user_id:id
rooms  -->  hotels : hotel_id:id
rooms_facilities  -->  facilities : facility_id:id
rooms_facilities  -->  rooms : room_id:id
