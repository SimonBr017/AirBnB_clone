# AirBnB clone - The console

![alt text](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210630%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210630T121423Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b8727e0005f1235528803a0283610f3822e2977746c3fc52b05110cd3463af64)

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
```python
echo "help EOF" | ./console.py
```
For interactive mode :
```python
./console.py
```

## Usage examples

After launching the console, you will be able to call any function that is implemented (see section below), here some examples :

```python
(hbnb) create User
48f6153b-bb95-4249-880a-1a2ef9952f5c
```
**Here we create one User instance, generating it's ID at the same time**

```python
(hbnb) all
["[User] (48f6153b-bb95-4249-880a-1a2ef9952f5c) {'id': '48f6153b-bb95-4249-880a-1a2ef9952f5c', 'created_at': datetime.datetime(2021, 6, 30, 14, 39, 23, 915529), 'updated_at': datetime.datetime(2021, 6, 30, 14, 39, 23, 915541)}"]
```
**Using the all function without argument, we print all the existing instances**

```python
(hbnb) update User 48f6153b-bb95-4249-880a-1a2ef9952f5c first_name "Betty"
[User] (48f6153b-bb95-4249-880a-1a2ef9952f5c) {'id': '48f6153b-bb95-4249-880a-1a2ef9952f5c', 'created_at': datetime.datetime(2021, 6, 30, 14, 39, 23, 915529), 'updated_at': datetime.datetime(2021, 6, 30, 14, 39, 23, 915541), 'first_name': 'Betty'}
```
**Here we update our existing instance calling it and it's ID. In order to print the changes, we use the show function**

There is another way to call functions, here a little example :

```python
(hbnb) User.count()
1
```
**Here we call the count function to know the number of instances, using the \<className\>.count we will obtain the number of instances of the specified class**
## Commands list

- <span style="color:IndianRed">help \<Cmd\></span> : Using help without arguments will print all the documented commands. Using with specified command, it will print what the command does.
- <span style="color:IndianRed">create \<className\></span> : Creates a new instance of \<className\>, saves it to the JSON file and prints the \<ID\>.
- <span style="color:IndianRed">show \<className\> \<ID\></span> : Prints the string representation of an instance based on the \<className\> and \<ID\>.
- <span style="color:IndianRed">all \<className\></span> : Prints all string representation of all instances based or not on the \<className\>, can be used without \<className\>.
- <span style="color:IndianRed">destroy \<className\> \<ID\></span> : Deletes an instance based on the \<className\> and \<ID\>.
- <span style="color:IndianRed">update \<className\> \<ID\> \<attributeName\> \<attribueValue\></span> : Updates an instance based on the \<className\> and \<ID\> by adding or updating attributes.
- <span style="color:IndianRed">count \<className\></span> : Retrieve the number of instances of \<className\>.

Functions that can be called using \<className\>.\<Cmd\> format :

- <span style="color:IndianRed"> User.show(\<ID\>)</span>
- <span style="color:IndianRed"> User.all()</span>
- <span style="color:IndianRed"> User.count()</span>
- <span style="color:IndianRed"> User.destroy(\<ID\>)</span>
- <span style="color:IndianRed"> User.update(\<ID\>, \<attributeName\>, \<attributeValue\>)</span>
- <span style="color:IndianRed"> User.update(\<ID\>, \<dictionaryRepresentation\>)</span>

## Authors

[BRARD Simon](https://github.com/SimonBr017)</br>
[LAPEYRE Nathan](https://github.com/Sarolus)