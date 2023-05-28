# WardrobePlanner

1. Make sure you have Python 3.10.4 or newer installed and install these Python modules:

   1. mysql-connector-python – 8.0.33

   2. requests – 2.31.0
    
   3. geopy - 2.3.0
    
   4. art – 5.9

2. Use the wardrobeDB.sql file to locally create a MySQL database to work with the app.
3. Put the appropriate data in the WardrobePlanner/classes/config.py file (Host, User, Password)
4. Run main()

- Default version of the database

By default, the database comes with 6 pre-existing users that you can use to log into the app, or you can create your own user.
You can also add them as friends in the app.

In this version of the app you need to know the exact username of another user to add them as a friend.

- Pre-existing users:

1. username: Anna,
password:  MyPassword123

2. username: Maria,
password: Diffi456

3. username: Jenny,
password: SomE56

4. username: Lucy,
password: ProT897

5. username: Kim,
password: kimkim

6. username: Olga,
password: W0rdPass

- Users 1 to 4 all have items in their wardrobes, friends and set hometowns.
- User 5 has no hometown or friends but they have items in their wardrobe.
- User 6 has a hometown but they have no friends or items.