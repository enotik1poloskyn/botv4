def unic_id ():
    unic_id = input("Enter your id: ")
    dump = "0"
    with open('unic_id.txt','r') as fhand:
        for line in fhand.readlines():
            dump = line.rstrip().split()
        while unic_id in dump:
            unic_id = input("Error, id occupied: ")
    fhand.close
    with open('unic_id.txt','a') as fhand:
        fhand.write(" "+unic_id)
    fhand.close
    return unic_id

def ask():
    print("Do you meet us ever?")
    answer = str.lower(input("Answer: "))
    while answer !="no" and answer !="yes":
        answer = str.lower(input("Again: "))
    if answer == "yes":
        return False
    else:
        return True

def check_user():
    unic_id = str.lower(input("Your id: "))
    dump = "0"
    with open('unic_id.txt','r') as fhand:
        for line in fhand.readlines():
            dump = line.rstrip().split()
        while unic_id not in dump:
            unic_id = input("Error, no such id in the system: ")
    fhand.close
    return unic_id