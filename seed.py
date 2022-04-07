from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

pet1 = Pet(name='Fluffy', species='Dog', photo_url='https://thumbs.dreamstime.com/b/dog-golden-retriever-jumping-autumn-leaves-autumnal-sunlight-77861618.jpg', age=3, notes='Very cute', available=True)

pet2 = Pet(name='Bella', species='Dog', photo_url='https://cdn.pixabay.com/photo/2017/09/25/13/12/cocker-spaniel-2785074__480.jpg', age=2, notes='Very cute', available=True)

pet3 = Pet(name='Lucy', species='Cat', photo_url='https://thumbs.dreamstime.com/b/pet-cat-green-cats-eyes-gray-big-102425920.jpg', age=1, notes='Very cute', available=False)


pet4 = Pet(name='Molly', species='Cat', photo_url='https://media.istockphoto.com/photos/cat-with-blue-eyes-looks-at-camera-picture-id1067347086?k=20&m=1067347086&s=612x612&w=0&h=Wxch207ChCoqnlqa5zvuy17J_YyApm42L6rUN3hml54', age=3, notes='Very cute', available=True)

pet5 = Pet(name='Lola', species='Porcupine', photo_url='https://cdn.pixabay.com/photo/2018/08/06/23/32/nature-3588682__340.jpg', age=2, notes='Very cute', available=True)

pet6 = Pet(name='Spike', species='Porcupine', photo_url='https://static7.depositphotos.com/1005563/721/i/600/depositphotos_7210512-stock-photo-hedgehog.jpg', age=2, notes='Very cute', available=True)

db.session.add_all([pet1, pet2, pet3, pet4, pet5, pet6])
db.session.commit()
