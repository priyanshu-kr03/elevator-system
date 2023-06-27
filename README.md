# elevator-system
In this project the business logic for a simplified elevator is implemented.
Three api has been implamented
* Add Building configuration (elevator/building-configuration/) (Post)
    In this we add name of building, number of floors and number of lift
    sample request body
        {
          "name": "Urbana",
          "num_floors": 63,
          "num_lifts": 12
        }

* Get Lift details of any particular building (elevator/elevators-status/<building-id>) (GET)
* Request elevator in a building
    In this we add building_id, floor, direction(up/down 1 for Up and 2 for down)
    sample request body
      {
          "building": "69b87886-aa16-463d-9529-4a4f72cff3aa",
          "floor": 0,
          "direction": 2
      }
All the logics are explained in the code base
