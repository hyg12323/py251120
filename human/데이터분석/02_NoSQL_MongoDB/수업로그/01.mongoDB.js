show dbs

use local

use testdb

show collections

show collections

db.stats()

db.createCollection("user")

show collections

db.user.drop()

db.collection2.drop()


db.createCollection("log", { capped : true, size : 5242880, max : 5000 } )

db.log.isCapped()

db.collection1.isCapped()

db.collection1.drop()

db.dropDatabase()

use human
db.createCollection("users")

db.users.insertOne(
      { subject: "coding", author: "human", views: 50 }
)


db.users.insertMany(
    [
      { subject: "coffee", author: "xyz", views: 50 },
      { subject: "Coffee Shopping", author: "efg", views: 5 },
      { subject: "Baking a cake", author: "abc", views: 90  },
      { subject: "baking", author: "xyz", views: 100 },
      { subject: "Café Con Leche", author: "abc", views: 200 },
      { subject: "Сырники", author: "jkl", views: 80 },
      { subject: "coffee and cream", author: "efg", views: 10 },
      { subject: "Cafe con Leche", author: "xyz", views: 10 },
      { subject: "coffees", author: "xyz", views: 10 },
      { subject: "coffee1", author: "xyz", views: 10 }
    ]
  )
  
 db.users.drop()

 db.users.find()
 db.createCollection("log", { capped : true, size : 5242880, max : 5000 } )
 
 
db.createCollection("users")
db.createUsersCollection("users", { capped : true, size : 100000, max :5000} )


db.users.insertMany(
    [
 
	{ name:"David", age:45, address:"서울" },
	{ name:"DaveLee", age:25, address:"경기도" },
	{ name:"Andy", age:50, hobby:"골프", address:"경기도" },
	{ name:"Kate", age:35, address:"수원시" },
	{ name:"Brown", age:8 }
    ]
  )
  
 db.users.find()

 db.users.find({ },{name:1, address:1})
 
  db.users.find({ },{name:1, address:1, _id: 0})
  
   db.users.find({address:"서울"})
   
   db.users.find({name:"DaveLee"})
   
db.users.find({name:"Kate"})
 
db.users.find({ address: "서울", age: 40 })

- db.users.find({ age: { $gt: 25 } })

db.users.find({age:{ $gt:25 }})
db.users.find({age:50,address:"경기도"})
db.users.find(
{age:{$lt:30}}
 )
db.users.find({$or: [{name:"Brown"},{age: 35}]})

// 1. users Collection 에서 name 이 DaveLee 인 Document의 name, age, address, _id 출력
db.users.find({name : "DaveLee"},
               {name:1 , age:1, address:1})
               
// 2. users Collection 에서 name 가 Kate 인 Document의 name, age, address 출력   
db.users.find({name: "Kate"},
               {name:1, age:1, address:1, _id:0})
               
 db.users.countDocuments()
 db.users.find()
 db.users.count( { address:{ $exists: true } } )
 
 db.users.distlnct("address")
 db.users.find().limit(2)
 
 db.users.find()
 
 db.users.insertMany([
   { name: "유진", age: 25, hobbies: ["독서", "영화", "요리"] },
   { name: "동현", age: 30, hobbies: ["축구", "음악", "영화"] },
   { name: "혜진", age: 35, hobbies: ["요리", "여행", "독서"] }
])
 
 MongoDB: db.users.updateOne(   { name: "민준" },    { $set: { name: "민준", age: 22, hobbies: ["음악", "여행"] }},    { upsert: true } ) 
 
db.users.find( { hobbies: { $all: [ "축구", "음악" ] } } )
 db.users.find( { hobbies: { $nin: [ "축구", "요리" ] } } )
 
 
    db.users.updateMany( { age: { $gt: 25 } }, { $set: { address: "서울" } } )

db.users.updateMany( { address: "서울" } , { $inc: { age: 3 } } )
db.users.find()

db.users.updateMany( { age: { $gt: 40 } }, 
                     { $set: { address: "수원시" } } )
                     
db.uses.updateOne({name : "유진"}, { $unset: { age: 1}})
db.users

db.users.deleteMany( { age:{ $lt: 30 } })

 