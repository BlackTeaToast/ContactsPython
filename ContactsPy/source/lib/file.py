from person import Person
import xml.dom.minidom
from xml.dom.minidom import Element, Text, Node, Document

def writeFile(persons):
    
    doc = Document()
     
    root = doc.createElement("PersonList")
    doc.appendChild(root)

    id = 0;
         
    for person in persons:

        personList = doc.createElement("Person")
        personList.setAttribute("id", str(id))
        id += 1
        root.appendChild(personList)
        
        print person
        # Create Element
        tempChild = doc.createElement("name")
        personList.appendChild(tempChild)
     
        # Write Text
        nodeText = doc.createTextNode(person.name)
        tempChild.appendChild(nodeText)

        # Create Element
        tempChild = doc.createElement("gender")
        personList.appendChild(tempChild)
     
        # Write Text
        nodeText = doc.createTextNode(person.gender)
        tempChild.appendChild(nodeText)

        # Create Element
        tempChild = doc.createElement("phone")
        personList.appendChild(tempChild)
     
        # Write Text
        nodeText = doc.createTextNode(person.phone)
        tempChild.appendChild(nodeText)

        # Create Element
        tempChild = doc.createElement("email")
        personList.appendChild(tempChild)
     
        # Write Text
        nodeText = doc.createTextNode(person.email)
        tempChild.appendChild(nodeText)
     
    doc.writexml( open(('data.xml'), 'w'),
                   indent="  ",
                   addindent="  ",
                   newl='\n')
     
    doc.unlink()
