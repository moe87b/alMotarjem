from firebase import firebase  
firebase = firebase.FirebaseApplication('https://almotarjem-eca52.firebaseio.com/', None)  
data =  'test'
result = firebase.post('/almotarjem-eca52/',data)  
print(type(result))  