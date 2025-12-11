show dbs

use saple_mfilx

db.users.count()

db.users.countDocuments()

db.users.countDocumentsCount()

use sample 

db.sample.find().count()


use human

db.createCollection("users")

db.users.insertMany([
   { name: "유진", age: 25, hobbies: ["독서", "영화", "요리"] },
   { name: "동현", age: 30, hobbies: ["축구", "음악", "영화"] },
   { name: "혜진", age: 35, hobbies: ["요리", "여행", "독서"] }
])


use human

db.users.drop()
db.createCollection("users")

db.users.insertMany([
   { name: "유진", age: 25, hobbies: ["독서", "영화", "요리"] },
   { name: "동현", age: 30, hobbies: ["축구", "음악", "영화"] },
   { name: "혜진", age: 35, hobbies: ["요리", "여행", "독서"] }
])

db.users.find()

db.movies.find()

use test

db.daveshop.find()