import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = '(hbnb) '
    def do_create(self, line):
        """
        It creates a new instance of BaseModel and saves it to json file
        """
        try:
            if not line:
                print("** class name missing **")
            args = line.split()
            class_name = args[0]
            if class_name == "BaseModel":
                self.model = BaseModel() #new instance of the BaseModel
                self.model.save() #save it
                print(self.model.id) #print id
            elif class_name == "User":
                user = User()
                user.save()
                print(user.id)
            elif class_name == "Place":
                place = Place()
                place.save()
                print(place.id)
            elif class_name == "State":
                state = State()
                state.save()
                print(state.id)
            elif class_name == "City":
                city = City()
                city.save()
                print(city.id)
            elif class_name == "Amenity":
                amenity = User()
                amenity.save()
                print(amenity.id)
            elif class_name == "Review":
                review = User()
                review.save()
                print(review.id)
            else:
                print("** class doesn't exist **")
        except(IndexError):
            pass
       
    def do_show(self, line):
        """
        prints the string representation of an instance based on the class name and id
        """
        if not line:
           print("** class name missing **")
        try:
            args = line.split()
            class_name = args[0]
            instances = models.storage.all()
            if class_name == "BaseModel" or "User" or "Place" or "State" or "City" or "Amenity" or "Review":
                if len(args) < 2:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
            key = class_name + "." + args[1]
            if key not in instances:
                print("** no instance found **")
            else:
                print(str(instances[key]))
        except(IndexError):
            pass
    def do_destroy(self, line):
        """
        deletes an instance based on the class name and id
        """
        try:
            if not line:
                print("** class name missing **")
            args = line.split()
            class_name = args[0]
            if class_name == "BaseModel" or "User" or "Place" or "State" or "City" or "Amenity" or "Review":
                if len(args) < 2:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
            key = class_name + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                instance = models.storage.all()
                obj_id = args[1]
                obj = instance.pop(f"{class_name}.{obj_id}", None)
                models.storage.save()
           
        except(IndexError):
            pass
                
 
    def do_all(self, line):
        """
        prints the string representation of all instances based on or not on the class name
        """
        try:
            instances = models.storage.all()
            args = line.split()
    
            if not line or args == 0:
                for instance in instances.values():
                    print(str(instance))
            if line:
                for instance in instances.values():
                        print(str(instance))
            
            
          
        except(IndexError):
            pass
    def do_update(self, line):
        """
        updates an instance based on the class name and id by adding or updating attribute
        """
        try:
            if not line:
                print("** class name missing **")
            args = line.split()
            class_name = args[0]
            obj_id = args[1]
            instance = models.storage.all()
            obj = instance.get(f"{class_name}.{obj_id}")
            key = class_name + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
                return
            if class_name == "BaseModel" or "User" or "Place" or "State" or "City" or "Amenity" or "Review":
                if len(args) < 2:
                    print("** instance id missing **")
                    return
                if len(args) == 2:
                    print("** atribute name misiing **")
                    return
                if len(args) == 3:
                    print("** value missing **")
                    return
                attr_name = args[2]
                attr_val = args[3]
                if attr_name in ["id", "created_at", "update_at"]:
                    print("can't update id, created_at and updated_at attributes")
                else:
                    setattr(obj, attr_name, attr_val)
                    obj.save()
            else:
                print("** class doesn't exist **")
                return
        except(IndexError):
            pass

    def do_quit(self,line):
        """
        Quit command to exit the program
        """
        return True
    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
if __name__ == '__main__':
    HBNBCommand().cmdloop()
