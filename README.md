# AirBnB clone - The console

![alt text](https://camo.githubusercontent.com/59589bd21e8ec09ef94f2d9bb80d36d144bc487fe4737f8b213d005f3273921b/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67)

## Description

This is the console use as command interpreter later in the AirBnB projects, using it we can manage the different instances of our classes,
using JSON file to store our objects after serializing them.

## Starting the console

First step, clone this repository in order to obtain all the files in your local machine :

```bash
git clone https://github.com/SimonBr017/AirBnB_clone.git
```

Using the console is quite simple, all you need to do is launch the python script this way :

For non-interactive mode :
```bash
echo "help EOF" | ./console.py
```
For interactive mode :
```bash
./console.py
```

## Usage examples

After launching the console, you will be able to call any function that is implemented (see section below), here some examples :

```
(hbnb) create User
48f6153b-bb95-4249-880a-1a2ef9952f5c
```
**Here we create one User instance, generating it's ID at the same time**

```
(hbnb) all
["[User] (48f6153b-bb95-4249-880a-1a2ef9952f5c) {'id': '48f6153b-bb95-4249-880a-1a2ef9952f5c', 'created_at': datetime.datetime(2021, 6, 30, 14, 39, 23, 915529), 'updated_at': datetime.datetime(2021, 6, 30, 14, 39, 23, 915541)}"]
```
**Using the all function without argument, we print all the existing instances**

```
(hbnb) update User 48f6153b-bb95-4249-880a-1a2ef9952f5c first_name "Betty"
[User] (48f6153b-bb95-4249-880a-1a2ef9952f5c) {'id': '48f6153b-bb95-4249-880a-1a2ef9952f5c', 'created_at': datetime.datetime(2021, 6, 30, 14, 39, 23, 915529), 'updated_at': datetime.datetime(2021, 6, 30, 14, 39, 23, 915541), 'first_name': 'Betty'}
```
**Here we update our existing instance calling it and it's ID. In order to print the changes, we use the show function**

There is another way to call functions, here a little example :

```
(hbnb) User.count()
1
```
**Here we call the count function to know the number of instances, using the \<className\>.count we will obtain the number of instances of the specified class**
## Commands list

- **help \<Cmd\>** : Using help without arguments will print all the documented commands. Using with specified command, it will print what the command does.
- **create \<className\>** : Creates a new instance of \<className\>, saves it to the JSON file and prints the \<ID\>.
- **show \<className\> \<ID\>** : Prints the string representation of an instance based on the \<className\> and \<ID\>.
- **all \<className\>**: Prints all string representation of all instances based or not on the \<className\>, can be used without \<className\>.
- **destroy \<className\> \<ID\>** : Deletes an instance based on the \<className\> and \<ID\>.
- **update \<className\> \<ID\> \<attributeName\> \<attribueValue\>** : Updates an instance based on the \<className\> and \<ID\> by adding or updating attributes.
- **count \<className\>** : Retrieve the number of instances of \<className\>.

Functions that can be called using \<className\>.\<Cmd\> format :

-  **User.show(\<ID\>)**
-  **User.all()**
-  **User.count()**
-  **User.destroy(\<ID\>)**
-  **User.update(\<ID\>, \<attributeName\>, \<attributeValue\>)**
-  **User.update(\<ID\>, \<dictionaryRepresentation\>)**

## Authors

[BRARD Simon](https://github.com/SimonBr017)</br>
[LAPEYRE Nathan](https://github.com/Sarolus)
