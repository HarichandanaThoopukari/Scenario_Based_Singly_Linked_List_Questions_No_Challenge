class Node:
    def __init__(self,stid,name,marks):
        self.stid=stid
        self.name=name
        self.marks=marks
        self.next=None
class singlylinkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,stid,name,marks):
        newnode=Node(stid,name,marks)
        if self.head is None:
            self.head=newnode
            return
        newnode.next=self.head
        self.head=newnode
    def insert_at_end(self,stid,name,marks):
        newnode=Node(stid,name,marks)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
    def insert_at_any_pos(self,stid,name,marks,pos):
        if pos<=0:
            print("Invalid Position")
            return
        if pos==1:
            self.insert_at_begin(stid,name,marks)
            return
        i=1
        temp=self.head
        while i<pos-1 and temp is not None:
            temp=temp.next
            i+=1
        
        if temp is None:
            print("Insufficient Elements")
            return
        newnode=Node(stid,name,marks)
        newnode.next=temp.next
        temp.next=newnode
    def count(self):
        ct=0
        temp=self.head
        while temp is not None:
            ct+=1
            temp=temp.next
        return ct
    def insert_at_mid(self,stid,name,marks):
        n=self.count()
        mid=n//2+1
        self.insert_at_any_pos(stid,name,marks,mid)
        return
    def delete_at_begin(self):
        if self.head is None:
            print("Student List is Empty")
            return
        self.head=self.head.next
    def delete_at_end(self):
        if self.head is None:
            print("Student List is Empty")
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        prev=None
        while temp.next is not None:
            prev=temp
            temp=temp.next
        prev.next=None
    def delete_at_any_pos(self,pos):
        if pos<=0:
            print("Invalid Position")
            return
        if pos==1:
            self.delete_at_begin()
            return
        i=1
        temp=self.head
        prev=None
        while i<pos-1 and temp is not None:
            prev=temp
            temp=temp.next
            i+=1
        if temp is None:
            print("Insuficient Elements")
            return
        prev.next=temp.next
    def delete_at_mid(self):
        n=self.count()
        mid=n//2+1
        self.delete_at_any_pos(mid)
        return
    def remove_using_id(self,studentid):
        if self.head is None:
            print("Students list is Empty")
            return

        temp=self.head
        prev=None

        while temp is not None:
            if temp.stid==studentid:
                if prev is None:
                    self.head=temp.next
                else:
                    prev.next=temp.next

                print("Student Removed")
                return

            prev=temp
            temp=temp.next

        print("Student Not found")
                
                
    def search(self,key_id):
        temp=self.head
        while temp is not None:
            if temp.stid==key_id:
                print("Student Found")
                return
            temp=temp.next
        return-1
    def display(self):
        if self.head is None:
            print("Students List is Empty")
            return
        temp=self.head
        while temp is not None:
            print(temp.stid,temp.name,temp.marks)
            
            temp=temp.next
    def max_marks(self):
        if self.head is None:
            print("Students List is Empty")
        m=0
        temp=self.head
        while temp is not None:
            if temp.marks>m:
                m=temp.marks
                s=temp.name
                i=temp.stid
            temp=temp.next
        print("Highest score:",i,s,m)
        return 
            
            
    def reverse(self):
        prev=None
        temp=self.head
        while temp is not None:
            nextnode=temp.next
            temp.next=prev
            prev=temp
            temp=nextnode
        self.head=prev
        
ll=singlylinkedlist()
while True:
    print("1. Register a student at the beginning")
    print("2. Register a student at the end")
    print("3. Register a student at a specified position")
    print("4. Remove a student using the Student ID")
    print("5. Search for a student using the Student ID")
    print("6. Display all registered students")
    print("7. Display the total number of registered students")
    print("8. Find and display the student who has the highest marks")
    print("9.Reverse the registration order")
    print("10. Exit")
    choice= int(input())
    match choice:
        case 1:
            stid=int(input("Enter Student ID:"))
            name=input("Enter Student Name:")
            marks=int(input("Enter Student Marks:"))
            ll.insert_at_begin(stid,name,marks)
        case 2:
            stid=int(input("Enter Student ID:"))
            name=input("Enter Student Name:")
            marks=int(input("Enter Student Marks:"))
            ll.insert_at_end(stid,name,marks)
        case 3:
            stid=int(input("Enter Student ID:"))
            name=input("Enter Student Name:")
            marks=int(input("Enter Student Marks:"))
            pos=int(input("Enter Position to Register:"))
            ll.insert_at_any_pos(stid,name,marks,pos)
        case 4:
            studentid=int(input("enter Student id to remove from the list:"))
            ll.remove_using_id(studentid)
                
        case 5:
            key_id=int(input("Enter id to Search:"))
            ll.search(key_id)
        case 6:
            ll.display()
        case 7:
            print("Total Number of Regidtered Students ",ll.count())
        case 8:
            ll.max_marks()
        case 9:
            ll.reverse()
            ll.display()
        case 10:
            print("program is terminated")
            break
        case 11:
            print("Invalid Choice")
                
                
                
                
                
                
                
                
                
    
            
    

            
            
            
                
        
        
            
            
        
        
        
        
        
            
        
        
    