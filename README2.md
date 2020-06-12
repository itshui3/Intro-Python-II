### Day 1 MVP

* Create the REPL command parser in `adv.py` which allows the player to move to rooms
  in the four cardinal directions.
* Fill out Player and Room classes in `player.py` and `room.py`

### Day 2 MVP

* Make rooms able to hold multiple items
* Make the player able to carry multiple items
* Add items to the game that the user can carry around
* Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser

## Stretch Goals

In arbitrary order:

* Add more rooms

* Add scoring

* Subclass items into treasures

* Add a subclass to `Item` called `LightSource`.

  * During world creation, add a `lamp` `LightSource` to a convenient `Room`.

  * Override `on_drop` in `LightSource` that tells the player "It's not wise to
  drop your source of light!" if the player drops it. (But still lets them drop
  it.)

  * Add an attribute to `Room` called `is_light` that is `True` if the `Room` is
  naturally illuminated, or `False` if a `LightSource` is required to see what
  is in the room.

  * Modify the main loop to test if there is light in the `Room` (i.e. if
    `is_light` is `True` **or** there is a `LightSource` item in the `Room`'s
    contents **or** if there is a `LightSource` item in the `Player`'s contents).

  * If there is light in the room, display name, description, and contents as
    normal.

  * If there isn't, print out "It's pitch black!" instead.

  * Hint: `isinstance` might help you figure out if there's a `LightSource`
    among all the nearby `Item`s.

  * Modify the `get`/`take` code to print "Good luck finding that in the dark!" if
  the user tries to pick up an `Item` in the dark.

* Add methods to notify items when they are picked up or dropped

* Add light and darkness to the game

* Add more items to the game.

* Add a way to win.

* Add more to the parser.

  * Remember the last `Item` mentioned and substitute that if the user types
    "it" later, e.g.

    ```
    take sword
    drop it
    ```

  * Add `Item`s with adjectives, like "rusty sword" and "silver sword".

    * Modify the parser to handle commands like "take rusty sword" as well as
      "take sword".

      * If the user is in a room that contains both the rusty sword _and_ silver
        sword, and they type "take sword", the parser should say, "I don't know
        which you mean: rusty sword or silver sword."

* Modify the code that calls `on_take` to check the return value. If `on_take`
  returns `False`, then don't continue picking up the object. (I.e. prevent the
  user from picking it up.)

  * This enables you to add logic to `on_take` to code things like "don't allow
    the user to pick up the dirt unless they're holding the shovel.

* Add monsters.

* Add the `attack` verb that allows you to specify a monster to attack.

* Add an `on_attack` method to the monster class.

* Similar to the `on_take` return value modification, above, have `on_attack`
  prevent the attack from succeeding unless the user possesses a `sword` item.