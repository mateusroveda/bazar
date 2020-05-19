from bazar.database.Migrations.User import User
from bazar.Console.helpers import Hash

create = User(
    user='admin',
    email='admin@bazar.local', 
    password=Hash.create('admin')  
)