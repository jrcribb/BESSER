from besser.BUML.metamodel.structural import NamedElement, DomainModel, Type, Class, \
        Property, PrimitiveDataType, Multiplicity, Association, BinaryAssociation, Generalization, \
        GeneralizationSet, AssociationClass 

# Primitive Data Types 
date_type = PrimitiveDataType("date")
str_type = PrimitiveDataType("str")
int_type = PrimitiveDataType("int")

# Library class definition 
Library_name: Property = Property(name="name", type=str_type, visibility="public")
Library_address: Property = Property(name="address", type=str_type, visibility="public")
Library: Class = Class(name="Library", attributes={Library_name, Library_address})

# Book class definition 
Book_tittle: Property = Property(name="tittle", type=str_type, visibility="public")
Book_pages: Property = Property(name="pages", type=int_type, visibility="public")
Book_edition: Property = Property(name="edition", type=date_type, visibility="public")
Book: Class = Class(name="Book", attributes={Book_tittle, Book_pages, Book_edition})

# Literature class definition 
Literature: Class = Class(name="Literature", attributes=set())

# Science class definition 
Science: Class = Class(name="Science", attributes=set())

# Fantasy class definition 
Fantasy: Class = Class(name="Fantasy", attributes=set())

# Author class definition 
Author_name: Property = Property(name="name", type=str_type, visibility="public")
Author_email: Property = Property(name="email", type=str_type, visibility="public")
Author: Class = Class(name="Author", attributes={Author_name, Author_email})

# Relationships
writtenBy: BinaryAssociation = BinaryAssociation(name="writtenBy", ends={
        Property(name="writtenBy", type=Book, multiplicity=Multiplicity(0, "*")),
        Property(name="writtenBy", type=Author, multiplicity=Multiplicity(1, "*"))})
has: BinaryAssociation = BinaryAssociation(name="has", ends={
        Property(name="has", type=Library, multiplicity=Multiplicity(1, 1)),
        Property(name="has", type=Book, multiplicity=Multiplicity(1, 1))})

# Generalizations
gen_Book_Literature: Generalization = Generalization(general=Book, specific=Literature)
gen_Book_Science: Generalization = Generalization(general=Book, specific=Science)
gen_Book_Fantasy: Generalization = Generalization(general=Book, specific=Fantasy)


# Domain Model
domain: DomainModel = DomainModel(name="Domain Model", types={Library, Book, Literature, Science, Fantasy, Author}, associations={writtenBy, has}, generalizations={gen_Book_Literature, gen_Book_Science, gen_Book_Fantasy})