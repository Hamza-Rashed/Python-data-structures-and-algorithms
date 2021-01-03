from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import Node, Queue, Animal, Cat, Dog, AnimalShelter

def test_cat():
    cat = Cat("Frodo")
    assert cat.data == 'Frodo'
    assert cat.type == 'cat'
    assert cat.next == None

def test_dog():
    dog = Dog("Sam")
    assert dog.data == 'Sam'
    assert dog.type == 'dog'
    assert dog.next == None


def test_shelter_enqueue():
    shelter = AnimalShelter()

    shelter.enqueue(Cat("1"))
    assert shelter.queue1.front.data == "1"
    assert shelter.queue1.rear.data == "1"
    shelter.enqueue(Dog("2"))
    assert shelter.queue1.rear.data == "2"
    shelter.enqueue(Cat("3"))
    assert shelter.queue1.rear.data == "3"
    shelter.enqueue(Dog("4"))
    assert shelter.queue1.rear.data == "4"
    assert shelter.queue1.front.data == "1"

def test_shelter_enqueue_notcar_or_dog():
    shelter = AnimalShelter()
    assert shelter.enqueue(Node('1')) == "Animal must be cat or dog"

def test_shelter_dequeue():
    shelter = AnimalShelter()

    shelter.enqueue(Cat("1"))
    shelter.enqueue(Dog("2"))
    shelter.enqueue(Cat("3"))
    shelter.enqueue(Cat("a"))
    shelter.enqueue(Dog("4"))

    pet_adopted = shelter.dequeue('cat')
    assert pet_adopted.type == 'cat'
    assert pet_adopted.data == '1'

    pet_adopted = shelter.dequeue('cat')
    assert pet_adopted.type == 'cat'
    assert pet_adopted.data == '3'

    pet_adopted = shelter.dequeue('dog')
    assert shelter.queue1.front.data == "a"
    assert pet_adopted.type == 'dog'
    assert pet_adopted.data == '2'

def test_shelter_dequeue_empty():
    shelter = AnimalShelter()
    pet_adopted = shelter.dequeue('dog')
    assert pet_adopted == None

def test_shelter_dequeue_not_in_list():
    shelter = AnimalShelter()
    shelter.enqueue(Cat("1"))
    shelter.enqueue(Cat("2"))
    pet_adopted = shelter.dequeue('dog')
    assert pet_adopted == None

def test_shelter_dequeue_not_in_list2():
    shelter = AnimalShelter()
    shelter.enqueue(Cat("1"))
    shelter.enqueue(Dog("2"))
    pet_adopted = shelter.dequeue('parrot')
    assert pet_adopted == None

def test_shelter_dequeue_capital():
    shelter = AnimalShelter()
    shelter.enqueue(Cat("1"))
    shelter.enqueue(Dog("2"))
    pet_adopted = shelter.dequeue('Dog')
    assert pet_adopted.data == '2'